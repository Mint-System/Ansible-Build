#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2018, Florian Paul Hoberg <florian.hoberg@credativ.de>
# Written by Florian Paul Hoberg <florian.hoberg@credativ.de>

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: yum_versionlock / dnf_versionlock
short_description: Locks/prevents packages from beeing updated/installed by yum or dnf
description:
    - This module manages versionlock in yum or dnf environment to prevent it from beeing installed/updated.
      To run this module you need to install rpm package 'yum-plugin-versionlock' or 'dnf-versionlock' depending of the package manager used.
    - 'present' state will include the package in the locked list to prevent updates
    - 'excluded' state will include the package in the exclusion list to prevent installations & updates.
    - A package can be added in both lists using the state 'present' and 'excluded'
options:
    state:
        description:
            - Add/exclude/remove a package to versionlock to prevent it from beeing installed/updated
            - Clear yum versionlock database (2.10)
        version_added: "2.7"
    package:
        description:
            - Wildcard package name (e.g. 'httpd')
            - 'package' accept wildcard format.
        version_added: "2.7"
    repo_mgr:
        description:
            - define the package manager to use to run the versionlock commands
        default: based on the name of the module name (yum_versionlock or dnf_versionlock)
        version_added: "2.10"
# informational: requirements for nodes
notes:
    - Since version 2.10 the package is only require with the state: present/excluded/absent.
    - The version 2.10 includes new states:
    -- state: exclude - This prevent packages to be installed on the server
    -- state: clear - This will clean the versionlock database
    - The module will also return result from --check ansible option
requirements:
    - yum / dnf
    - yum-versionlock / dnf-versionlock
author:
    - Florian Paul Hoberg <florian.hoberg@credativ.de>
'''
EXAMPLES = '''
- name: Clear the dnf versionlock database
  yum_versionlock:
    state: clear
    repo_mgr: dnf
- name: Prevent Apache / httpd from beeing updated
  yum_versionlock:
    state: present
    package: httpd
- name: Prevent nginx from beeing installed/updated
  yum_versionlock:
    state: excluded
    package: nginx
- name: Ensure python3* packages are not locked/excluded
  yum_versionlock:
    state: absent
    package: python3*
'''

# Import 'os.path' to check versionlock config file
# Import 're' to do search and strings substitution
import os.path, re
from ansible.module_utils.basic import AnsibleModule

# Define a variable to set the language to 'C' as default
ENV_LOCALE = {'LC_ALL': 'C'}


def get_state_versionlock(module, repo_cfg):
    """ Check for plugin dependency """
    state = os.path.exists(repo_cfg)
    if state:
        config_file = open(repo_cfg,"r")
        for line in config_file.readlines():
            if "enabled" in line:
                enabled_state = line.split()[2]
        if enabled_state != '1' and enabled_state != 'True':
            module.warn("Warn: Plugin is installed but disabled ("+enabled_state+") in " + repo_cfg)
        config_file.close
    return state


def get_packages(module, repo_mgr, list_type, package):
    """ Get an overview of all packages available/installed """
    rc_code, out, err = module.run_command("/usr/bin/%s -q list %s %s"
                                           % (repo_mgr, list_type, package), environ_update=ENV_LOCALE)
    if rc_code is 0:
        return out.splitlines()
    else:
        if rc_code == 1 and str(err) == 'Error: No matching Packages to list\n':
            return out.splitlines()
        else:
            module.fail_json(msg="Unable to collect " + repo_mgr + " list " + list_type + " : " + str(err) + " - " + str(out))


def fct_versionlock(module, repo_mgr, action, package=''):
    """ Get an overview of all packages on versionlock """
    if repo_mgr != 'dnf':
        quiet_opt = '-q'
    else:
        quiet_opt = ''
    rc_code, out, err = module.run_command("/usr/bin/%s %s versionlock %s %s"
                                           % (repo_mgr, quiet_opt, action, package), environ_update=ENV_LOCALE)
    if rc_code is 0:
        regex_exclude = re.compile(r'^(!)?(\d+:)?(\w+-)+(\d+:)?\d\S\S+')
        out_array = out.splitlines()
        versionlock_packages = [i for i in out_array if regex_exclude.search(i)]
        return versionlock_packages
    else:
        module.fail_json(msg="Error: " + str(err) + str(out))


def check_pkg_versionlock(package, versionlock_packages):
    versionlock_pkg = dict()
    versionlock_pkg['matching'] = []
    versionlock_pkg['different'] = []
    package_regex = re.sub('\*', '.*', package)
    regex_search = re.compile('!?(\d+:)?%s-(\d+:)?[.\w]+\.\*' %package_regex)
    for locked in versionlock_packages:
        if regex_search.search(locked):
            versionlock_pkg['matching'].append(locked)
        else:
            versionlock_pkg['different'].append(locked)
    return versionlock_pkg


def check_state_pkg(package, list_to_check, versionlock_packages, check_type):
    """ Verify that all desired installed packages are locked """
    state_pkg = dict()
    state_pkg['present'] = []
    state_pkg['missing'] = []
    missing_pkg_version = None
    for is_checked in list_to_check:
        if is_checked != 'Installed Packages' and is_checked != 'Available Packages':
            # Split to concatenate name & version
            pkg_split = is_checked.split()
            if missing_pkg_version:
                pkg_name = missing_pkg_version
                pkg_version = pkg_split[0]
                missing_pkg_version = None
            else:
                pkg_name = pkg_split[0].split('.')[0]
                try:
                    pkg_version = pkg_split[1]
                except IndexError:
                    missing_pkg_version = pkg_split[0].split('.')[0]
            if pkg_version:
                pkg_vers = pkg_name + '-' + pkg_version
                if check_type == 'installed':
                    regex_search = re.compile('^(\d+:)?%s-(\d+:)?%s\.\*'%(pkg_name,pkg_version))
                else:
                    regex_search = re.compile('^\!(\d+:)?%s-(\d+:)?%s\.\*'%(pkg_name,pkg_version))
                    # Init flag is_present
                is_present = False
                # search for the installed package in versionlock list
                for locked in versionlock_packages:
                    if regex_search.search(locked):
                        is_present = True
                if is_present:
                    state_pkg['present'].append(pkg_vers)
                else:
                    state_pkg['missing'].append(pkg_vers)
    return state_pkg


def main():
    """ Start main program to add/exclude/delete a package in versionlock"""
    default_mgr = __file__.split('_')[1]
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(required=True, type='str', choices=['present', 'excluded', 'absent', 'clear']),
            package=dict(required=False, type='str'),
            repo_mgr=dict(required=False, type='str', choices=['dnf', 'yum'], default=default_mgr),
        ),
        supports_check_mode=True,
        required_one_of=[['state']],
    )

    state = module.params['state']
    package = module.params['package']
    repo_mgr = module.params['repo_mgr']

    result = dict(
        changed=False,
        status=dict(),
        diff=dict(),
    )

    debug = dict()

    # Check for the versionlock config file and if plugins is enabled
    if repo_mgr == 'yum':
        repo_plugin_folder = "/etc/yum/pluginconf.d"
        # In RHEL8 / Centos8, dnf create a link for the yum folder.
        # But the running command is dnf as the package yum_versionlock doesn't exist anymore.
        if os.path.islink(repo_plugin_folder):
            repo_plugin_folder = "/etc/dnf/plugins"
            repo_mgr = 'dnf'
    elif repo_mgr == 'dnf':
        repo_plugin_folder = "/etc/dnf/plugins"
    repo_cfg = repo_plugin_folder + "/versionlock.conf"
    versionlock_plugin = get_state_versionlock(module, repo_cfg)
    debug['is_versionlock_installed?'] = versionlock_plugin
    debug['Config_file'] = repo_cfg
    if versionlock_plugin is False:
        module.fail_json(msg="Error: Config file '" + repo_cfg + "' is missing. Please install " + repo_mgr + "-versionlock")
    if repo_mgr == 'yum':
        versionlock_prefix = '0:'
    elif repo_mgr == 'dnf':
        versionlock_prefix = ''

    # Get an overview of all packages that have a version lock
    versionlock_packages = fct_versionlock(module, repo_mgr, 'list')
    # Raw version will be used for the --diff option which only work with strings
    versionlock_packages_raw = '\n'.join(versionlock_packages) + '\n'
    debug['repo_manager_used'] = repo_mgr
    debug['versionlock_packages'] = versionlock_packages

    # Simply check if we should only clear the DB
    if state == 'clear':
        if versionlock_packages:
            result['changed'] = True
            if not module.check_mode:
                result['status']['out'] = fct_versionlock(module, repo_mgr, 'clear')
    else:
        # Check if package is defined
        if package == None:
            module.fail_json(msg="Error: 'package' option is required (except for 'clear' state)")
        list_available = get_packages(module, repo_mgr, 'available', package)
        list_installed = get_packages(module, repo_mgr, 'installed', package)
        length_available = len(list_available)
        # Add a package to versionlock
        if state == "present":
            locked_pkg = check_state_pkg(package, list_installed, versionlock_packages, 'installed')
            debug['locked_pkg_status'] = locked_pkg
            if locked_pkg['missing']:
                result['changed'] = True
                after_str = versionlock_packages_raw
                for array_field in locked_pkg['missing']:
                    after_str = after_str + versionlock_prefix + str(array_field) + ".*\n"
                result['diff']['before'] = versionlock_packages_raw
                result['diff']['after'] = after_str
                if not module.check_mode:
                    result['status']['out'] = fct_versionlock(module, repo_mgr, 'add', package)
        # Remove a package from versionlock
        elif state == "absent":
            included_versionlock = check_pkg_versionlock(package, versionlock_packages)
            debug['versionlock_status'] = included_versionlock
            if included_versionlock['matching']:
                result['changed'] = True
                after_str = versionlock_packages_raw
                for array_field in included_versionlock['matching']:
                    after_str = re.sub('!?([0-9]+:)?%s\.\*\n' %array_field, '', after_str)
                result['diff']['before'] = versionlock_packages_raw
                result['diff']['after'] = after_str
                if not module.check_mode:
                    debug['out'] = fct_versionlock(module, repo_mgr, 'delete', package)
        elif state == "excluded":
            available_pkgs = check_state_pkg(package, list_available, versionlock_packages, 'excluded')
            installed_pkgs = check_state_pkg(package, list_installed, versionlock_packages, 'excluded')
            debug['available_pkg_status'] = available_pkgs
            debug['installed_pkg_status'] = installed_pkgs
            if length_available != 0 or available_pkgs['missing'] or installed_pkgs['missing']:
                result['changed'] = True
                after_str = versionlock_packages_raw
                for array_field in installed_pkgs['missing'] + available_pkgs['missing'] :
                    after_str = after_str + '!' + versionlock_prefix + str(array_field) + '.*\n'
                result['diff']['before'] = versionlock_packages_raw
                result['diff']['after'] = after_str
                if not module.check_mode:
                    result['status']['out'] = fct_versionlock(module, repo_mgr,'exclude', package)

    result['debug'] = debug
    module.exit_json(**result)

if __name__ == '__main__':
    main()
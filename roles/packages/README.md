<img src="/logos/packages.png" alt="packages logo" width="100" height="100">

# Packages role

Set env vars and install packages.

This role supports the following package types:

* apt
* dnf
* yum
* snap

## Usage

Configure the role.

```yml
dnf_repos:
  - name: epel-release
yum_repos:
  - name: restic
    url: https://copr.fedorainfracloud.org/coprs/copart/restic/repo/epel-7/copart-restic-epel-7.repo
apt_repos:
  - name: https://tommie.github.io/innernet-debian/debian
    branch: contrib
    key: https://tommie.github.io/innernet-debian/repository.asc

group_packages:
  - name: zsh
  - name: restic
  - name: vim
    version: 2:8.0.1453-1ubuntu1.3
host_packages:
  - name: cifs_utils
pip_packages:
  - name: docker
script_packages:
  - dest: /usr/local/bin/hello-mom
    content: |
      echo "Hello Mom!"
  - dest: /usr/local/bin/hello-dad
    src: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}/hello-dad.sh"
```

Include it in your playbook.

```yml
- hosts: packages
  roles:
  - role: packages
```

Or include it in another role.

```yml
- name: Install required docker packages
  include_role:
    name: packages
  vars:
    group_packages:
      - "{{ docker_package }}"
```

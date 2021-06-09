# Ansible package role

Set env vars and install packages.

## Usage

Configure the role.

**vars.yml**

```yml
dnf_repos:
  - name: epel-release
yum_repos:
  - name: restic
    url: https://copr.fedorainfracloud.org/coprs/copart/restic/repo/epel-7/copart-restic-epel-7.repo
packages:
  - name: zsh
  - name: restic
  - name: vim
    version: 2:8.0.1453-1ubuntu1.3
```

Include it in your playbook.

```yml
- hosts: package
  roles:
  - role: package
```

Or include it in another role.

```yml
- name: Install required docker packages
  include_role:
    name: package
  vars:
    packages:
      - "{{ docker_package }}"
```

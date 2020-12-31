# Ansible package role

Set env vars and install packages.

## Usage

Configure the role.

**vars.yml**

```yml
config_system_locale: pt_PT.UTF-8 # default: en_US.UTF-8
config_system_language: pt_PT.UTF-8 # default: en_US.UTF-8
packages:
  - name: zsh
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

# Ansible package role

Install and pin packages.

## Usage

Configure the role.

**vars.yml**

```yml
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
    tags: package
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
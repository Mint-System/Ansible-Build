# Ansible package role

Install and pin packages.

## Usage

Configure the role.

**vars.yml**

```yml
packages:
  - name: vim=2:8.0.1453-1ubuntu1.1
  - name: bacula-console-qt
    state: absent
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
# Ansible Cleanup role

Cleanup Ansible roles.

## Usage

Include it in your playbook.

```yml
- hosts: clean
  roles:
  - { role: clean, tags: ["clean"] }
```

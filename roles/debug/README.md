# Ansible Debug role

Debug Ansible variables.

## Usage

Update the `main.yml`.

Include it in your playbook.

```yml
- hosts: debug
  roles:
  - { role: debug, tags: ["debug"] }
```
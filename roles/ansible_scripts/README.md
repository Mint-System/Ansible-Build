# Ansible Scripts role

Install Ansible scripts.

## Usage

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: ansible_scripts
```

## Docs

### Install command line tools

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/master/roles/ansible_scripts/files/install | bash` in your terminal.

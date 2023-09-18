# Odoo Scripts role

Install Odoo scripts.

## Usage

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo_scripts
```

## Docs

### Install without Ansible

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/master/roles/odoo_scripts/files/install | bash` in your terminal.

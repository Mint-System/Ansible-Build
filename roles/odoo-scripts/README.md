# Ansible Odoo Scripts role

Install Odoo scripts.

## Requires

The Ansible Odoo Scripts role requires the following roles:

* odoo

## Usage

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo
    tags: odoo
  - role: odoo-scripts
    tags: odoo-scripts
```

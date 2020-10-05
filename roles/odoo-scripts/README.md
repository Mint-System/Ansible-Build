# Ansible Odoo Scripts role

Install Odoo scripts.

## Usage

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo-scripts
```

## Docs

### Install without Ansible

Download the script files from folder `files` and copy them to `/usr/local/bin`.

Ensure that the files are executable `chmod +x /usr/local/bin/odoo-backup`
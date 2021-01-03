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

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-playbooks/master/roles/odoo-scripts/files/install | sh` in your terminal.

Download the script files from folder `files` and copy them to `/usr/local/bin`.

Ensure that the files are executable `chmod +x /usr/local/bin/odoo-backup`
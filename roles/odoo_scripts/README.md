<img src="/logos/odoo_scripts.png" alt="odoo_scripts logo" width="100" height="100">

# Odoo Scripts role

Install Odoo scripts.

## Usage

Configure the role.

```yml
odoo_backup_set: # See restic_backup_set var in role restic
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo_scripts
```

The following tags are available:

* odoo_scripts
* odoo_backup
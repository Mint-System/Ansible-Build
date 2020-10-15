# Ansible Odoo Enterprise role

Checkout the Odoo Enterprise git repository.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_enterprise_git_repo:
odoo_enterprise_git_key_file:
odoo_enterprise_git_remote:
odoo_enterprise_git_commit:
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo-enterprise
```

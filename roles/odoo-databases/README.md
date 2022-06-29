# Odoo Databases role

Configure Odoo databases.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_databases:
  - name: erp
    state: present
  - name: erp-dev
    state: absent
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo-scripts
```
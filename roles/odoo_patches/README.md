# Odoo patches role

Apply custom Odoo patches.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_patches:
  - name: odoo14_delivery_patch
```

And include it in your playbook.

```yml
- hosts: odoo_patches
  roles:
  - role: odoo_patches
```

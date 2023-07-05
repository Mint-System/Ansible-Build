# Odoo patches role

Apply custom Odoo patches.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_patches:
  - name: odoo16_microsoft_outlook_expires_in_patch
```

And include it in your playbook.

```yml
- hosts: odoo_patches
  roles:
  - role: odoo_patches
```

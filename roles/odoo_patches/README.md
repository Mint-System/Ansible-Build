# Odoo patches role

Apply custom Odoo patches.

#DEPRECATED: This role is no longer maintained.

## Usage

Configure the role.

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

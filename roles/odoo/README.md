# Ansible Odoo role

Deploys Odoo Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_image: odoo:13
odoo_hostname: odoo01
odoo_port: 8069
odoo_data_dir: /usr/share/odoo01
odoo_volume_name: odoo_data01
odoo_postgres_hostname: postgres01
odoo_postgres_user: example
odoo_postgres_password: "{{ vault_postgres_password }}"
odoo_master_password_hash: "{{ vault_odoo_master_password_hash }}"
odoo_conf: |
  dbfilter = ^%d$
odoo_apps:
  - name: show_db_name
    url: https://github.com/Mint-System/Odoo-App-Show-DB-Name/archive/v1.0.1.zip
  - name: web_enterprise
    file: web_enterprise-13.0.1.0.zip
  - name: theme_clean
    includes:
    - theme_clean
    - theme_common
    - website_animate
    url: https://apps.odoo.com/loempia/download/theme_clean/13.0.1.1.zip?deps
odoo_backup_sets: # See restic_backup_sets var in role restic-client
```

And include it in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo
    tags: odoo
```

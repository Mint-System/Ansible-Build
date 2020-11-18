# Ansible Odoo apps role

Install Odoo apps.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_data_dir: /usr/share/odoo01
odoo_apps:
  - name: show_db_name
    url: https://github.com/Mint-System/Odoo-App-Show-DB-Name/archive/v1.0.2.zip
  - name: web_enterprise
    file: web_enterprise-13.0.1.0.zip
  - name: theme_common
    file: theme_common-14.0.0.1.1.zip
  - name: theme_treehouse
    file: theme_treehouse-14.0.2.0.0.zip
    depends:
      - theme_common
```

And include it in your playbook.

```yml
- hosts: odoo-apps
  roles:
  - role: odoo-apps
```

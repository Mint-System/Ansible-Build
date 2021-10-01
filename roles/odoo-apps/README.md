# Ansible Odoo apps role

Install Odoo apps from file, url, public or private GitHub repo.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_hostname: odoo01
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_apps_tmp_dir: /tmp # default: /var/tmp
odoo_apps_remove_unmanaged_folders: false # default: true
odoo_apps:
  - name: show_db_name
    url: https://github.com/Mint-System/Odoo-App-Show-DB-Name/archive/v1.0.2.zip
  - name: theme_common
    file: theme_common-14.0.0.1.1.zip
  - name: theme_treehouse
    file: theme_treehouse-14.0.2.0.0.zip
    depends:
      - theme_common
  - name: demand_planner
    url: https://github.com/Mint-System/Demand-Planner/archive/refs/tags/v14.0.1.0.0.zip
    github_token: "{{ vault_github_token }}"
odoo_patches:
  - name: odoo14_delivery_patch
    host: odoo01
odoo_pip_packages:
  - name: python-jose
```

And include it in your playbook.

```yml
- hosts: odoo-apps
  roles:
  - role: odoo-apps
```

The following tags are available:

* odoo-apps
* odoo-patches
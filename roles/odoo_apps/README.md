# Odoo apps role

Install Odoo apps from file, url, public or private GitHub repos.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_hostname: odoo01
odoo_replicas: 2 # default: 1
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"

odoo_apps_tmp_dir: /tmp # default: /var/tmp
odoo_apps_remove_unmanaged_folders: false # default: true
odoo_apps_base_url: https://cloud.example.com/download?files= # + {{ item.name }}-{{ item.version }}.zip
odoo_apps:
  - name: show_db_name
    file: show_db_name-14.0.1.0.2.zip
  - name: sale_order_notes
    version: 14.0.1.0.0
  - name: sale_blanket_order_notes
    version: 14.0.1.1.0
    depends:
      - sale_order_notes

odoo_repo_key_file: /home/bot/.ssh/id_ed25519
odoo_repos:
  - name: partner-contact
    url: git@github.com:OCA/partner-contact.git
    version: 16.0
  - name: web
    url: git@github.com:OCA/web.git
    version: "d83e8543db74363b71ce71b32243766b986da335"
  - name: mint-system-server-tools
    url: git@github.com:Mint-System/Odoo-Apps-Server-Tools.git
    version: 16.0
    pull: true

odoo_pip_packages:
  - name: python-jose
  - name: mock==3.0.5
```

And include it in your playbook.

```yml
- hosts: odoo_apps
  roles:
  - role: odoo_apps
```

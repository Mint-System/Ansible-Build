# Ansible Odoo role

Deploy Odoo Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
odoo_image: odoo:13
odoo_hostname: odoo01
odoo_replicas: 3 # default: 1
odoo_description: Odoo13:erp.example.com # default: Odoo
odoo_ports:
 - "8069:8069" # default: "127.0.0.1:8069:8069"
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_volume_name: odoo_data01 # default: "{{ odoo_hostname}}"
odoo_timezone: Europe/Paris # default: Europe/Berlin
odoo_postgres_hostname: postgres01
odoo_postgres_user: example
odoo_postgres_password: "{{ vault_postgres_password }}"
odoo_master_password_hash: "{{ vault_odoo_master_password_hash }}"
odoo_conf: |
  dbfilter = ^%d$
odoo_backup_sets: # See restic_backup_sets var in role restic-client
```

And include it in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo
```

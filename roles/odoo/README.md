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
odoo_postgres_user: example # default: odoo
odoo_postgres_password: # default: "{{ vault_postgres_password }}"
odoo_master_password: # default: "{{ vault_odoo_master_password }}"
odoo_conf_limit_request: 4096 # default: 8192
odoo_conf_limit_time_cpu: 300 # default: 600
odoo_conf_limit_time_real: 600 # default: 1200
odoo_conf: | # default: proxy_mode = True
  proxy_mode = False
odoo_backup_set: # See restic_backup_set var in role restic-client
```

And include it in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo
```

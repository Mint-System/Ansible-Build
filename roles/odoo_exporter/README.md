<img src="/logos/odoo_exporter.png" alt="odoo_exporter logo" width="100" height="100">

# Odoo Exporter role

 Add nginx config for Odoo exporter path.
 
## Usage

Configure the role.

```yml
# https://www.odoo-wiki.org/prometheus-exporter.html
odoo_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
odoo_exporter_basic_auth_username: odoo-exporter
odoo_exporter_basic_auth_password: # default: "{{ vault_odoo_exporter_basic_auth_password }}"
```

Ensure the nginx proxy includes the odoo-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    tls: true
    exporter: odoo
    options: |
      include /etc/nginx/conf.d/proxies/odoo-exporter.nginx;
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo_exporter
```
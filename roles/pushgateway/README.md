# Pushgateway role

Deploy Pushgateway container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/prom/pushgateway
pushgateway_image: prom/pushgateway:v1.11.0
pushgateway_hostname: pushgw01
pushgateway_description: Pushgateway # default: Pushgateway
pushgateway_volume_name: pushgw_data01 # default: "{{ pushgateway_hostname }}"
pushgateway_data_dir: /usr/share/pushgw # default: "/usr/share/{{ pushgateway_hostname }}"
pushgateway_port: 127.0.0.1:9091 # default: 127.0.0.1:9091
pushgateway_etc_hosts: # defaults: {}
  "server.example.com": 10.42.5.2
pushgateway_proxy_basic_auth_username: metric # default: pushgateway
pushgateway_proxy_basic_auth_password: # default: "{{ vault_pushgateway_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    monitor: /
    exporter: node,cadvsior,nextcloud,bigbluebutton,postgres,restic,mysqld,odoo
    options: |
      include /etc/nginx/conf.d/proxies/node-exporter.nginx;
      include /etc/nginx/conf.d/proxies/cadvisor.nginx;
      include /etc/nginx/conf.d/proxies/nextcloud-exporter.nginx;
      include /etc/nginx/conf.d/proxies/bigbluebutton-exporter.nginx;
      include /etc/nginx/conf.d/proxies/postgres-exporter.nginx;
      include /etc/nginx/conf.d/proxies/mysqld-exporter.nginx;
      include /etc/nginx/conf.d/proxies/odoo-exporter.nginx;
      include /etc/nginx/conf.d/proxies/n8n-exporter.nginx;
```


And include it in your playbook.

```yml
- hosts: pushgateway
  roles:
  - role: pushgateway
```

## Docs

Pushgateway is used to monitor cronjobs

### Deploy Pushgateway container

Select multiple inventories when deploying.

```bash
task play -i inventories/odoo -i inventories/nextcloud -i inventories/setup plays/setup.yml -l pushgateway -t pushgateway
```

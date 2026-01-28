<img src="/logos/alertmanager.png" alt="alertmanager logo" width="100" height="100">

# Alertmanager role

Deploy Alertmanager container.

## Usage

Configure the role.

```yml
alertmanager_image: prom/alertmanager:v0.27.0
alertmanager_hostname: alertmanager01
alertmanager_description: Alertmanager
alertmanager_web_external_url: https://monitoring.example.com/alertmanager
alertmanager_basic_auth_username: alertmanager
alertmanager_basic_auth_password: # default: "{{ vault_alertmanager_basic_auth_password }}"
alertmanager_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
alertmanager_config:
  route:
    group_by: ['alertname']
    group_wait: 30s
    group_interval: 5m
    repeat_interval: 1h
    receiver: 'web.hook'
  receivers:
    - name: 'web.hook'
      webhook_configs:
        - url: 'http://127.0.0.1:5001/'
  inhibit_rules:
    - source_match:
        severity: 'critical'
      target_match:
        severity: 'warning'
      equal: ['alertname', 'dev', 'instance']
```

And include it in your playbook.

```yml
- hosts: alertmanager
  roles:
  - role: alertmanager
```

## Docs

### Alertmanager config

Alertmanager is configured using the `alertmanager_config` variable. It accepts a alertmanager configuration as described [here](https://prometheus.io/docs/alerting/latest/configuration/)

### Nginx config

Ensure the nginx proxy includes the exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    tls: true
    monitor: /
    exporter: node,cadvsior,nextcloud,bigbluebutton,postgres,restic,mysqld,odoo,alertmanager
    options: |
      include /etc/nginx/conf.d/proxies/node-exporter.nginx;
      include /etc/nginx/conf.d/proxies/cadvisor.nginx;
      include /etc/nginx/conf.d/proxies/nextcloud-exporter.nginx;
      include /etc/nginx/conf.d/proxies/bigbluebutton-exporter.nginx;
      include /etc/nginx/conf.d/proxies/postgres-exporter.nginx;
      include /etc/nginx/conf.d/proxies/mysqld-exporter.nginx;
      include /etc/nginx/conf.d/proxies/odoo-exporter.nginx;
      include /etc/nginx/conf.d/proxies/alertmanager.nginx;
```
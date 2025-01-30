# Prometheus role

Deploy Prometheus container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/prom/prometheus
prometheus_image: prom/prometheus:v2.54.1
prometheus_hostname: prom01
prometheus_description: Monitoring # default: Prometheus
prometheus_volume_name: prom_data01 # default: "{{ prometheus_hostname }}"
prometheus_data_dir: /usr/share/prom # default: "/usr/share/{{ prometheus_hostname }}"
prometheus_hosts: # default: groups['all']
  - server1.example.com
  - server2.example.com
  - server3.example.com
prometheus_port: 127.0.0.1:9999 # default: 127.0.0.1:9090
prometheus_retention_time: "30d" # default: "15d"
prometheus_etc_hosts: # defaults: {}
  "server.example.com": 10.42.5.2

prometheus_node_exporter_basic_auth_username: node-exporter
prometheus_node_exporter_basic_auth_password: # default: "{{ vault_prometheus_node_exporter_basic_auth_password }}"
prometheus_cadvisor_basic_auth_username: cadvisor
prometheus_cadvisor_basic_auth_password: # default: "{{ vault_prometheus_cadvisor_basic_auth_password }}"
prometheus_nextcloud_exporter_basic_auth_username: nextcloud-exporter
prometheus_nextcloud_exporter_basic_auth_password: # default: "{{ vault_prometheus_nextcloud_exporter_basic_auth_password }}"
prometheus_bigbluebutton_exporter_basic_auth_username: bigbluebutton-exporter
prometheus_bigbluebutton_exporter_basic_auth_password: # default: "{{ vault_prometheus_bigbluebutton_exporter_basic_auth_password }}"
prometheus_postgres_exporter_basic_auth_username: postgres-exporter
prometheus_postgres_exporter_basic_auth_password: # default: "{{ vault_prometheus_postgres_exporter_basic_auth_password }}"
prometheus_restic_exporter_basic_auth_username: restic-exporter
prometheus_restic_exporter_basic_auth_password: # default: "{{ vault_prometheus_restic_server_basic_auth_password }}"
prometheus_mysqld_exporter_basic_auth_username: mysqld-exporter
prometheus_mysqld_exporter_basic_auth_password: # default: "{{ vault_prometheus_mysqld_exporter_basic_auth_password }}"
prometheus_odoo_exporter_basic_auth_username: odoo-exporter
prometheus_odoo_exporter_basic_auth_password: # default: "{{ vault_prometheus_odoo_exporter_basic_auth_password }}"
prometheus_n8n_exporter_basic_auth_username: n8n-exporter
prometheus_n8n_exporter_basic_auth_password: # default: "{{ vault_prometheus_n8n_exporter_basic_auth_password }}"
prometheus_meilisearch_exporter_api_key: "{{ vault_prometheus_meilisearch_exporter_api_key }}"
prometheus_uptime_kuma_exporter_password: "{{ vault_prometheus_uptime_kuma_exporter_password }}"
```

Ensure the targets nginx proxy includes the exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    monitor: /
    exporter: node,cadvsior,nextcloud,bigbluebutton,postgres,restic,mysqld,odoo,n8n
    options: |
      include /etc/nginx/conf.d/proxies/node-exporter.nginx;
      include /etc/nginx/conf.d/proxies/cadvisor.nginx;
      include /etc/nginx/conf.d/proxies/nextcloud-exporter.nginx;
      include /etc/nginx/conf.d/proxies/bigbluebutton-exporter.nginx;
      include /etc/nginx/conf.d/proxies/postgres-exporter.nginx;
      include /etc/nginx/conf.d/proxies/restic-exporter.nginx;
      include /etc/nginx/conf.d/proxies/mysqld-exporter.nginx;
      include /etc/nginx/conf.d/proxies/odoo-exporter.nginx;
      include /etc/nginx/conf.d/proxies/n8n-exporter.nginx;
```


And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: prometheus
```

## Docs

### Predefined scrape configs

The `prometheus.yml` template contains predefined srcape jobs that lookup proxy configurations of `prometheus_hosts` in the Ansible inventory.

* **prometheus**: Target is `localhost:9090`.
* **node-exporter https**: Targets are `nginx_proxies` with exporter `node`.
* **cadvisor https**: Targets are `nginx_proxies` with exporter `cadvisor`.
* **nextcloud https**: Targets are `nginx_proxies` with exporter `nextcloud`.
* **bigbluebutton http**: Targets are `nginx_proxies` with exporter `bigbluebutton`.
* **postgres https**:Targets are `nginx_proxies` with exporter `postgres`.
* **restic https**: Targets are `nginx_proxies` with exporter `restic`.
* **mysqld https**: Targets are `nginx_proxies` with exporter `mysqld`.
* **odoo https**: Targets are `nginx_proxies` with exporter `odoo`.
* **n8n https**: Targets are `nginx_proxies` with exporter `n8n`.
* **blackbox**: Targets are `nginx_proxies` with `monitor` not false and host is `blackbox01:9115`.

### Custom scrapers

override the variable `prometheus_custom_scrapers` 
example:
```
prometheus_custom_scrapers: |
  - job_name: n8n business metrics https
    metrics_path: "/webhook/metrics"
    scrape_interval: 60s
    honor_labels: true
    scheme: https
    basic_auth:
      username: {{ prometheus_n8n_business_metrics_username }}
      password: {{ prometheus_n8n_business_metrics_password }}
    static_configs:
      - targets: ['n8n.example.com']
```

### Deploy Prometheus container

Select multiple inventories when deploying.

```bash
ansible-playbook -i inventories/odoo -i inventories/nextcloud -i inventories/setup plays/setup.yml -l prometheus -t prometheus
```

### Clear Prometheus data

Remove container and volume.

```bash
docker rm -f prom01
docker volume rm prom01
```

Then redeploy.
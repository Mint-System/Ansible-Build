# Prometheus role

Deploy Prometheus container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/prom/prometheus
prometheus_image: prom/prometheus:v2.54.1
prometheus_hostname: prom01
prometheus_description: Monitoring # default: Prometheus
prometheus_volume_name: prom_data01 # default: "{{ prometheus_hostname }}"
prometheus_data_dir: /usr/share/prom # default: "/usr/share/{{ prometheus_hostname }}"
prometheus_port: 127.0.0.1:9999 # default: 127.0.0.1:9090
prometheus_retention_time: "30d" # default: "15d"
prometheus_node_exporter_basic_auth_password: "{{ vault_prometheus_node_exporter_basic_auth_password }}"
prometheus_cadvisor_basic_auth_username: cadvisor
prometheus_cadvisor_basic_auth_password: "{{ vault_prometheus_cadvisor_basic_auth_password }}"
prometheus_nextcloud_exporter_basic_auth_username: nextcloud-exporter
prometheus_nextcloud_exporter_basic_auth_password: "{{ vault_prometheus_nextcloud_exporter_basic_auth_password }}"
prometheus_bigbluebutton_exporter_basic_auth_username: bigbluebutton-exporter
prometheus_bigbluebutton_exporter_basic_auth_password: "{{ vault_prometheus_bigbluebutton_exporter_basic_auth_password }}"
prometheus_postgres_exporter_basic_auth_username: postgres-exporter
prometheus_postgres_exporter_basic_auth_password: "{{ vault_prometheus_postgres_exporter_basic_auth_password }}"
prometheus_mysqld_exporter_basic_auth_username: mysqld-exporter
prometheus_mysqld_exporter_basic_auth_password: "{{ vault_prometheus_mysqld_exporter_basic_auth_password }}"
prometheus_restic_server_basic_auth_username: restic-server
prometheus_restic_server_basic_auth_password: "{{ vault_prometheus_restic_server_basic_auth_password }}"
prometheus_etc_hosts: # defaults: {}
  "server.example.com": 10.42.5.2
```

On hosts define these vars for https job targets.

```yml
prometheus_target_scheme: https
prometheus_target_port: 443
```

Or for http job targets.

```yml
prometheus_target_scheme: http
prometheus_target_port: 80
```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: prometheus
```

## Docs

### Predefined srape configs

The `prometheus.yml` template contains predefined srcape jobs that lookup hosts in the Ansible inventory.

* **prometheus**: Target is `localhost:9090`.
* **cadvisor https**: Targets are hosts with a `cadvisor_hostname` and https scheme.
* **cadvisor http**: Targets are hosts with a `cadvisor_hostname` and http scheme.
* **node-exporter https**: Targets are hosts with a `node_exporter_hostname` and https scheme.
* **node-exporter http**: Targets are hosts with a `node_exporter_hostname` and http scheme.
* **nextcloud https**: Targets are hosts with a `nextcloud_exporter_hostname` and http scheme.
* **bigbluebutton https**: Targets are hosts with a `bigbluebutton_exporter_hostname` and https scheme.
* **postgres https**: Targets are hosts with a `postgres_exporter_hostname` and https scheme.
* **restic-server https**: Targets are hosts with a `restic_server_hostname` and https scheme.
* **blackbox**: Targets are `nginx_proxies` with `monitor` not false and host is `blackbox01:9115`.
* **odoo https**: Targets are `nginx_proxies` with `monitor_odoo` set true.
* **mysqld https**: Targets are hosts with a `mysqld_exporter_hostname` and http scheme.

### Deploy Prometheus container

Select multiple inventories when deploying.

```bash
ansible-playbook -i inventories/odoo -i inventories/nextcloud -i inventories/setup play_setup.yml -l prometheus -t prometheus
```

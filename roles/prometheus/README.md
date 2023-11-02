# Prometheus role

Deploy Prometheus container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/prom/prometheus
prometheus_image: prom/prometheus:v2.37.1
prometheus_hostname: prom01
prometheus_description: Monitoring # default: Prometheus
prometheus_volume_name: prom_data01 # default: "{{ prometheus_hostname }}"
prometheus_data_dir: /usr/share/prom # default: "/usr/share/{{ prometheus_hostname }}"
prometheus_port: 127.0.0.1:9999 # default: 127.0.0.1:9090
prometheus_retention_time: "30d" # default: "15d"
prometheus_node_exporter_basic_auth_username: node-exporter
prometheus_node_exporter_basic_auth_password: "{{ vault_prometheus_node_exporter_basic_auth_password }}"
prometheus_cadvisor_basic_auth_username: cadvisor
prometheus_cadvisor_basic_auth_password: "{{ vault_prometheus_cadvisor_basic_auth_password }}"
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

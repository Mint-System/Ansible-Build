# Ansible Prometheus role

Deploys Prometheus container.

And the inventory group *exporter*.

## Usage

Configure the role.

**vars.yml**

```yml
prometheus_image: prom/prometheus:v2.17.1
prometheus_hostname: prom01
prometheus_volume_name: prom_data01
prometheus_data_dir: /usr/share/prom01
prometheus_node_exporter_basic_auth_username: node-exporter
prometheus_node_exporter_basic_auth_password: "{{ vault_prometheus_node_exporter_basic_auth_password }}"
prometheus_cadvisor_basic_auth_username: cadvisor
prometheus_cadvisor_basic_auth_password: "{{ vault_prometheus_cadvisor_basic_auth_password }}"
prometheus_scrape_configs:
  - job_name: prometheus
    scrape_interval: 10s
    honor_labels: true
    static_configs:
      - targets:
          - localhost:9090
  - job_name: cadvisor https
    metrics_path: "/cadvisor/metrics"
    scrape_interval: 10s
    honor_labels: true
    scheme: https
    basic_auth:
      username: "{{ prometheus_cadvisor_basic_auth_username }}"
      password: "{{ prometheus_cadvisor_basic_auth_password }}"
    static_configs:
      - targets:
          - server.example.com
```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: prometheus
    tags: prometheus
```

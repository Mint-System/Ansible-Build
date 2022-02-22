# Ansible Prometheus role

Deploy Prometheus container.

## Usage

Configure the role.

**vars.yml**

```yml
prometheus_image: prom/prometheus:v2.17.1
prometheus_hostname: prom01
prometheus_description: Monitoring # default: Prometheus
prometheus_volume_name: prom_data01
prometheus_data_dir: /usr/share/prom # default: "/usr/share/{{ prometheus_hostname }}"
prometheus_port: 127.0.0.1:9999 # default: 127.0.0.1:9090
prometheus_rention_time: "60d" # default: "30d"
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
  - job_name: cadvisor http
    metrics_path: "/cadvisor/metrics"
    scrape_interval: 15s
    honor_labels: true
    scheme: http
    basic_auth:
      username: "{{ prometheus_cadvisor_basic_auth_username }}"
      password: "{{ prometheus_cadvisor_basic_auth_password }}"
    static_configs:
      - targets: "{{ groups['all'] | map('extract', hostvars) | 
          json_query('[? cadvisor_hostname && prometheus_target_scheme==`http`].[ansible_host,prometheus_target_port]') | 
          map('join', ':') | list }}"
  - job_name: node-exporter https
    metrics_path: "/node-exporter/metrics"
    scrape_interval: 15s
    honor_labels: true
    scheme: https
    basic_auth:
      username: "{{ prometheus_node_exporter_basic_auth_username }}"
      password: "{{ prometheus_node_exporter_basic_auth_password }}"
    static_configs:
      - targets: "{{ groups['all'] | map('extract', hostvars) | 
          json_query('[? node_exporter_hostname && prometheus_target_scheme==`https`].[ansible_host,prometheus_target_port]') | 
          map('join', ':') | list }}"
prometheus_etc_hosts: # defaults: {}
  "leto.mint-system.com": 10.42.5.2
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

# Ansible Prometheus role

Deploys Prometheus container.

## Requires

The Ansible Prometheus role requires the following roles:

* docker
* docker-network
* cadvisor and/or node-exporter

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
```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: prometheus
    tags: prometheus
```

# Docs

The Prometheus role extracts all hosts from the inventory group *exporter* and uses them as targets. Only if the exporter host has an node-exporter or cadvisor container configured it will be used as target.
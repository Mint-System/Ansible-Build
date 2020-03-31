# Ansible Prometheus role

Deploys Prometheus container.

## Requires

The Ansible Prometheus role requires the following roles:

* docker
* docker-network
* cadvisor and/or node-exporter
* inventory group *exporter*

## Usage

Configure the role.

**vars.yml**

```yml
prometheus_image: prom/prometheus:v2.17.1
prometheus_hostname: prom01
prometheus_volume_name: prom_data01
prometheus_data_dir: /usr/share/prom01
```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: cadvisor
    tags: cadvisor
  - role: node-exporter
    tags: node-exporter
  - role: prometheus
    tags: prometheus
```

# Docs

The Prometheus role extracts all hosts from the inventory group *exporter* and uses them as targets. Only if the exporter host has an node-exporter or cadvisor image configured it will be used as target.
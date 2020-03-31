# Ansible Grafana role

Deploys Grafana container.

## Requires

The Ansible Grafana role requires the following roles:

* docker
* docker-network
* prometheus

## Usage

Configure the role.

**vars.yml**

```yml
grafana_image: grafana/grafana:6.7.1
grafana_hostname: graf01
grafana_data_dir: /usr/share/graf01
grafana_volume_name: grafana_data01
grafana_admin_user: admin
grafana_admin_password: "{{ vault_grafana_admin_password }}"
grafana_prometheus_hostname: prom01
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
  - role: grafana
    tags: grafana
```

<img src="/logos/node_exporter.png" alt="node_exporter logo" width="100" height="100">

# Node Exporter role

Deploy node-exporter container and install custom metric script.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/prom/node-exporter
node_exporter_image: prom/node-exporter:v1.0.1
node_exporter_hostname: node01
node_exporter_description: Host metrics for server1 # default: "Node Exporter {{ inventory_hostname_short }}"
node_exporter_nginx_enabled: false # default: true
node_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
node_exporter_requires_package: python2-passlib # default: python3-passlib
node_exporter_proxy_basic_auth_username: exporter # default: node-exporter
node_exporter_proxy_basic_auth_password: # default: "{{ vault_node_exporter_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the node-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    tls: true
    exporter: node
    options: |
      include /etc/nginx/conf.d/proxies/node-exporter.nginx;
```

And include it in your playbook.

```yml
- hosts: node_exporter
  roles:
  - role: node_exporter
```

The following tags are available:

* node_exporter
* node_exporter_nginx_config

## Docs

### Host filesystem mount

By default to node-exporter mounts the host filesystem to `/hostfs`.

### Request metrics manually

Show the metrics output for a selected `host` with this command:

```bash
host=server1
task run $host -i inventories/setup -m shell -a "curl -s 'https://node-exporter:{{ hostvars[inventory_hostname]['vault_node_exporter_proxy_basic_auth_password'] }}@{{ hostvars[inventory_hostname]['ansible_host'] }}/node-exporter/metrics'"
```

### Show metrics locally

Use this command to show the metrics of the Node Exporter container:

```bash
curl http://node01:9100/metrics
```
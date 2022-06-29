# Node Exporter role

Deploy node-exporter container and install custom metric script.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/prom/node-exporter
node_exporter_image: prom/node-exporter:v1.0.1
node_exporter_hostname: node01
node_exporter_description: Host metrics for server1 # default: "Node Exporter {{ inventory_hostname_short }}"
node_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
node_exporter_requires_package: python2-passlib # default: python3-passlib
node_exporter_proxy_basic_auth_username: exporter # default: node-exporter
node_exporter_proxy_basic_auth_password: "{{ vault_node_exporter_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the node-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/node-exporter.nginx;
```

And include it in your playbook.

```yml
- hosts: node-exporter
  roles:
  - role: node-exporter
```

The following tags are available:

* node-exporter
* node-exporter-nginx-config

## Docs

By default to node-exporter mounts the host filesystem to `/hostfs`.
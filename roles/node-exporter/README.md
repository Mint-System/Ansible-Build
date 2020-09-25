# Ansible Node Exporter role

Deploys node-exporter container and install custom metric script.

## Usage

Configure the role.

**vars.yml**

```yml
node_exporter_image: prom/node-exporter:v1.0.1
node_exporter_hostname: node01
node_exporter_description: Host metric for server1 # default: Node Exporter
node_exporter_nginx_data_dir: /usr/share/nginx01/proxies
node_exporter_requires_package: python2-passlib # default: python3-passlib
```

Ensure the nginx proxy includes the node-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/node-exporter.nginx;
      include /etc/nginx/conf.d/proxies/cadvisor.nginx;
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
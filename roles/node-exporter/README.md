# Ansible Node Exporter role

Deploys node-exporter container.

## Usage

Configure the role.

**vars.yml**

```yml
node_exporter_image: prom/node-exporter:v0.18.1
node_exporter_hostname: node01
node_exporter_nginx_data_dir: /usr/share/nginx01
```

Ensure the nginx proxy includes the node-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/*.nginx;
```

And include it in your playbook.

```yml
- hosts: node-exporter
  roles:
  - role: node-exporter
    tags: node-exporter
```

## Docs

By default to node-exporter mounts the host filesystem to `/hostfs`.
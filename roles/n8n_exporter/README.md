<img src="/logos/n8n_exporter.png" alt="n8n_exporter logo" width="100" height="100">

# N8N Exporter role

Add nginx config for N8N exporter path.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/n8nio/n8n
n8n_exporter_basic_auth_username: # default: n8n-exporter
n8n_exporter_basic_auth_password: # default: "{{ vault_n8n_exporter_basic_auth_password }}"
n8n_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
```

Ensure the nginx proxy includes the n8n-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    tls: true
    exporter: n8n
    options: |
      include /etc/nginx/conf.d/proxies/n8n-exporter.nginx;
```

Include the role in your playbook.

```yml
- hosts: n8n
  roles:
  - role: n8n_exporter
```
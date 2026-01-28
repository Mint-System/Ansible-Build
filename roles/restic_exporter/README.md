<img src="/logos/restic_exporter.png" alt="restic_exporter logo" width="100" height="100">

# Restic Exporter role

Add nginx config for Restic exporter path.

## Usage

Configure the role.

```yml
restic_exporter_requires_package: python2-passlib # default: python3-passlib
restic_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
restic_exporter_basic_auth_username: exporter # default: restic-exporter
restic_exporter_basic_auth_password: # default: "{{ vault_restic_exporter_basic_auth_password }}"
```

Ensure the nginx proxy includes the restic-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    tls: true
    exporter: restic
    options: |
      include /etc/nginx/conf.d/proxies/restic-exporter.nginx;
```

Include the role in your playbook.

```yml
- hosts: restic
  roles:
  - role: restic_exporter
```
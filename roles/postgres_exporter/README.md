<img src="/logos/postgres_exporter.png" alt="postgres_exporter logo" width="100" height="100">

# PostgreSQL exporter role

Deploy PostgreSQL exporter container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/prometheuscommunity/postgres-exporter
postgres_exporter_image: prometheuscommunity/postgres-exporter:v0.15.0
postgres_exporter_hostname: pgexport01
postgres_exporter_description: Database metric for postgres01 # default: "PostgreSQL Exporter {{ postgres_exporter_server }}"
postgres_exporter_data_dir: /usr/share/pgexport # default: "/usr/share/{{ postgres_exporter_hostname }}"
postgres_exporter_server: postgres01 # default: "{{ postgres_hostname }}"
postgres_exporter_username: # default: "{{ postgres_user }}"
postgres_exporter_password: # default: "{{ vault_postgres_password }}"
postgres_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
postgres_exporter_requires_package: python2-passlib # default: python3-passlib
postgres_exporter_proxy_basic_auth_username: exporter # default: postgres-exporter
postgres_exporter_proxy_basic_auth_password: # default: "{{ vault_postgres_exporter_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the postgres-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    exporter: postgres
    options: |
      include /etc/nginx/conf.d/proxies/postgres-exporter.nginx;
```

And include it in your playbook.

```yml
- hosts: postgres_exporter
  roles:
  - role: postgres_exporter
```

The following tags are available:

* postgres_exporter
* postgres_exporter_nginx_config

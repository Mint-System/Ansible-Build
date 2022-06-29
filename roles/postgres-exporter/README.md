# PostgreSQL exporter role

Deploy PostgreSQL exporter container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/prometheuscommunity/postgres-exporter
postgres_exporter_image: prometheuscommunity/postgres-exporter:master
postgres_exporter_hostname: pgexport01
postgres_exporter_description: Database metric for postgres01 # default: "PostgreSQL Exporter {{ postgres_hostname }}"
postgres_exporter_data_dir: /usr/share/pgexport # default: "/usr/share/{{ postgres_exporter_hostname }}"
postgres_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
postgres_exporter_requires_package: python2-passlib # default: python3-passlib
postgres_exporter_proxy_basic_auth_username: exporter # default: postgres-exporter
postgres_exporter_proxy_basic_auth_password: "{{ vault_postgres_exporter_proxy_basic_auth_password }}"
postgres_exporter_server: postgres01
postgres_exporter_username: "{{ postgres_user }}"
postgres_exporter_password: "{{ postgres_password }}"
```

Ensure the nginx proxy includes the postgres-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/postgres-exporter.nginx;
```

And include it in your playbook.

```yml
- hosts: postgres-exporter
  roles:
  - role: postgres-exporter
```

The following tags are available:

* postgres-exporter
* postgres-exporter-nginx-config

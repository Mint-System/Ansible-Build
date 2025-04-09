<img src="/logos/mysqld_exporter.png" alt="mysqld_exporter logo" width="100" height="100">

# MySQL exporter role

Deploy MySQL exporter container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/prom/mysqld-exporter/
mysqld_exporter_image: prom/mysqld-exporter:v0.16.0
mysqld_exporter_hostname: myexport01
mysqld_exporter_description: Database metric for mysql01 # default: "MySQL Exporter {{ mysqld_exporter_server }}"
mysqld_exporter_data_dir: /usr/share/myexport # default: "/usr/share/{{ mysqld_exporter_hostname }}"
mysqld_exporter_server: mysql01
mysqld_exporter_username: "{{ mysql_user }}"
mysqld_exporter_password: "{{ mysql_password }}"
mysqld_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
mysqld_exporter_requires_package: python2-passlib # default: python3-passlib
mysqld_exporter_proxy_basic_auth_username: exporter # default: mysqld-exporter
mysqld_exporter_proxy_basic_auth_password: # default: "{{ vault_mysqld_exporter_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the mysqld-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    exporter: mysqld
    options: |
      include /etc/nginx/conf.d/proxies/mysqld-exporter.nginx;
```

And include it in your playbook.

```yml
- hosts: mysqld_exporter
  roles:
  - role: mysqld_exporter
```

The following tags are available:

* mysqld_exporter
* mysqld_exporter_nginx_config

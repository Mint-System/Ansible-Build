# Nextcloud exporter role

Deploy Nextcloud exporter container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/xperimental/nextcloud-exporter
nextcloud_exporter_image: xperimental/nextcloud-exporter:latest
nextcloud_exporter_hostname: nexport01
nextcloud_exporter_description: Host metric for server1 # default: "Nextcloud Exporter {{ nextcloud_hostname }}"
nextcloud_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
nextcloud_exporter_requires_package: python2-passlib # default: python3-passlib
nextcloud_exporter_proxy_basic_auth_username: exporter # default: nextcloud-exporter
nextcloud_exporter_proxy_basic_auth_password: "{{ vault_node_exporter_proxy_basic_auth_password }}"
nextcloud_exporter_server: http://nextcloud01
nextcloud_exporter_username: "{{ nextcloud_admin_user }}"
nextcloud_exporter_password: "{{ nextcloud_admin_password }}"
```

Ensure the nginx proxy includes the nextcloud-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/nextcloud-exporter.nginx;
```

And include it in your playbook.

```yml
- hosts: nextcloud-exporter
  roles:
  - role: nextcloud-exporter
```

The following tags are available:

* nextcloud-exporter
* nextcloud-exporter-nginx-config

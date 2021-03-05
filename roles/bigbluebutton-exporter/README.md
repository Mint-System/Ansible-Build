# Ansible BigBlueButton exporter role

Deploy BigBlueButton exporter container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/greenstatic/bigbluebutton-exporter
bigbluebutton_exporter_image: greenstatic/bigbluebutton-exporter:v0.6.0
bigbluebutton_exporter_hostname: bbbexport01
bigbluebutton_exporter_description: Host metric for server1 # default: BigBlueButton exporter
bigbluebutton_exporter_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
bigbluebutton_exporter_requires_package: python2-passlib # default: python3-passlib
bigbluebutton_exporter_proxy_basic_auth_username: exporter # default: bigbluebutton-exporter
bigbluebutton_exporter_proxy_basic_auth_password: "{{ vault_bigbluebutton_exporter_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the bigbluebutton-exporter config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/bigbluebutton-exporter.nginx;
```

And include it in your playbook.

```yml
- hosts: bigbluebutton-exporter
  roles:
  - role: bigbluebutton-exporter
```

The following tags are available:

* bigbluebutton-exporter
* bigbluebutton-exporter-nginx-config

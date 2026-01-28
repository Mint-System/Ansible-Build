<img src="/logos/alloy.png" alt="alloy logo" width="100" height="100">

# Alloy role

Deploy Alloy container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/grafana/alloy
alloy_image: grafana/alloy:v1.12.0
alloy_hostname: alloy01
alloy_description: conainter monitoring for server1 # default: "alloy {{ inventory_hostname_short }}"
alloy_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
alloy_requires_package: python2-passlib # default: python3-passlib
alloy_basic_auth_username: exporter # default: alloy
alloy_basic_auth_password: # default: "{{ vault_alloy_basic_auth_password }}"
```

Ensure the nginx proxy includes the alloy config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    tls: true
    exporter: alloy
    options: |
      include /etc/nginx/conf.d/proxies/alloy.nginx;
```

And include it in your playbook.

```yml
- hosts: alloy
  roles:
  - role: alloy
```

The following tags are available:

* alloy
* alloy_nginx_config

## Docs

### Show metrics locally

Use this command to show the metrics of the Alloy container:

```bash
curl http://alloy01:12345/metrics
```
# Ansible Loki role

Deploy Loki container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/grafana/loki/
loki_image: grafana/loki:2.3.0
loki_hostname: loki01
loki_description: log index for grafana # default: Loki
loki_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
loki_data_dir: /usr/share/loki # default: "/usr/share/{{ loki_hostname }}"
loki_requires_package: python2-passlib # default: python3-passlib
loki_proxy_basic_auth_username: log # default: loki
loki_proxy_basic_auth_password: "{{ vault_loki_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the loki config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/loki.nginx;
```

And include it in your playbook.

```yml
- hosts: loki
  roles:
  - role: loki
```

The following tags are available:

* loki
* loki-nginx-config

## Docs


### Send test request to push api

Send test data to push api with with curl using basic auth.

```
curl -v -H "Content-Type: application/json" -XPOST -s "http://localhost:3100/loki/api/v1/push" --data-raw \
  '{"streams": [{ "stream": { "foo": "bar2" }, "values": [ [ "1570818238000000000", "fizzbuzz" ] ] }]}'
```
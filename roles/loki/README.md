# Loki role

Deploy Loki container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/grafana/loki/
loki_image: grafana/loki:3.3.2
loki_hostname: loki01
loki_description: log index for grafana # default: Loki
loki_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
loki_data_dir: /usr/share/loki # default: "/usr/share/{{ loki_hostname }}"
loki_requires_package: python2-passlib # default: python3-passlib
loki_proxy_basic_auth_username: log # default: loki
loki_proxy_basic_auth_password: # default: "{{ vault_loki_proxy_basic_auth_password }}"
```

Ensure the nginx proxy includes the loki config:

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      include /etc/nginx/conf.d/proxies/loki.nginx;
```
or if loki runs on a dedicated domain

```yml
nginx_proxies:
  - src_hostname: server.example.com
    ssl: true
    options: |
      options: |
      location / {
        auth_basic "{{ loki_proxy_basic_auth_username }}";
        auth_basic_user_file /etc/nginx/conf.d/proxies/loki.htpasswd;
        proxy_pass http://{{ loki_hostname }}:3100;
      }
```

And include it in your playbook.

```yml
- hosts: loki
  roles:
  - role: loki
```

The following tags are available:

* loki
* loki_nginx_config

## Docs

### Add Loki datasource to Grafana

In the grafana dashboard add a new connection and select "Loki".

Enter URL <http://loki01:3100> of your container instance.

Save and test the connection.

### Send test request to push api

Send test data to push api with with curl.

```bash
curl -H "Content-Type: application/json" -XPOST -s "https://monitor.example.com/loki/api/v1/push" \
  --data-raw \
  '{"streams": [{ "stream": { "foo": "bar2" }, "values": [ [ "1570818238000000000", "fizzbuzz" ] ] }]}'
```


Send test data to push api with with curl with basic auth.

```bash
curl -H "Content-Type: application/json" -XPOST -s "https://monitor.example.com/loki/api/v1/push" \
  -u loki:$BASIC_AUTH_PASSWORD \
  --data-raw \
  '{"streams": [{ "stream": { "foo": "bar2" }, "values": [ [ "1570818238000000000", "fizzbuzz" ] ] }]}'
```

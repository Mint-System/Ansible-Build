# Nginx role

Deploy Nginx proxy with Certbot.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/nginx/
nginx_image: nginx:1.25.2-alpine
nginx_hostname: nginx01
nginx_data_dir: /usr/share/nginx # default: "/usr/share/{{ nginx_hostname }}"
nginx_ports:
  - 8080:80 # default: 80:80
  - 8443:443 # default: 443:443
nginx_http_options: |
  map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
  }
nginx_limit_req_zones:
  - name: one
    size: 20m # default 10m
    rate: 10r/s
nginx_proxies:
  - src_hostname: www.example.com
    dest_hostname: webserver
    dest_replicas: 3 # default: 1
    dest_port: 8080 # default: 80
    limit_req_zone: one
    options: |
      add_header Strict-Transport-Security "max-age=15552000; includeSubdomains;"
    ssl: true # default: false
  - src_hostname: example.com
    ssl: true # default: false
    redirect_hostname: www.example.com
  - src_hostname: example.org
    redirect_hostname: www.example.com
    cache: true
    server_names:
      - example.org
      - www.example.org
  - src_hostname: login.example.com
    ssl: true # default: false
    monitor: true # default: false
    locations:
      - path: /
        dest_hostname: frappe-bench
        dest_port: 8000
        proxy_params: |
          proxy_set_header Host frappe-bench:8000;
        options: |
          client_max_body_size 128M;
        limit_req_zone: one
      - path: /auth
        dest_hostname: authserver
        dest_port: 8080 # default: 80
        options: |
          proxy_buffer_size 128k;
          proxy_buffers 4 256k;
          proxy_busy_buffers_size 256k;
          client_max_body_size 256M;
  - src_hostname: old.example.com
    redirect_url: https://www.example.com/new
  - src_hostname: intern.example.com
    dest_hostname: intern01
    dest_port: 8080
    locations:
      - path: /static
        root: intern.example.com
  - src_hostname: odoo.example.com
    dest_hostname: odoo01
    dest_port: 8069 # default: 80
    ssl: true  # default: false
    monitor: true # default: false
    upstreams:
      - name: odoo
        server: odoo17:8069
      - name: odoochat
        server: odoo17:8072
    options: |
      location /longpolling {
        proxy_pass http://odoochat;
        include /etc/letsencrypt/proxy-params.conf;
      }
      client_max_body_size 32M;
    proxy_params: |
      include /etc/letsencrypt/proxy-params.conf;
      if ($request_method = OPTIONS) {
        add_header Access-Control-Allow-Origin "http://localhost:8080";
        add_header Access-Control-Allow-Credentials true;
        add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS";
        add_header Access-Control-Allow-Headers "Accept,Authorization,Cache-Control,Content-Type,DNT,If-Modified-Since,Keep-Alive,Origin,User-Agent,X-Requested-With";
        add_header Access-Control-Max-Age 1728000;
        add_header Content-Type "text/plain charset=UTF-8";
        add_header Content-Length 0;
        return 204;
      }
      add_header Access-Control-Allow-Origin "http://localhost:8080";
      add_header Access-Control-Allow-Credentials true;
      proxy_cookie_path / "/; secure; HttpOnly; SameSite=None";
nginx_cache_enabled: true # default: false
```

And include it in your playbook.

```yml
- hosts: nginx
  roles:
  - role: nginx
```

The following tags are available:

* nginx
* nginx_config

## Docs

### Install Nginx command line tools

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/master/roles/nginx/files/install | sh` in your terminal.

# Nginx role

Deploy Nginx proxy with Certbot.

## Usage

Configure the role.

**vars.yml**

```yml
nginx_image: nginx:1.19.2-alpine
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
nginx_proxies:
  - src_hostname: www.example.com
    dest_hostname: webserver
    dest_replicas: 3 # default: 1
    dest_port: 8080 # default: 80
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
    redirect: false # default: true
    dest_hostname: intern01
    dest_port: 8080
    locations:
      - path: /static
        root: intern.example.com
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
* nginx-config

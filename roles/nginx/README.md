# Ansible Nginx role

Deploy Nginx proxy with Certbot.

## Usage

Configure the role.

**vars.yml**

```yml
nginx_image: nginx:1.19.2-alpine
nginx_hostname: nginx01
nginx_data_dir: /usr/share/nginx # default: "/usr/share/{{ nginx_hostname }}"
postgres_ports:
  - 8080:8080 # default: 80:80
  - 8443:8443 # default: 443:443
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
    server_names:
      - example.org
      - www.example.org
  - src_hostname: login.example.com
    ssl: true # default: false
    monitor: true # default: false
    locations:
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

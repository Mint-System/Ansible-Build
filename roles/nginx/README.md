# Ansible Nginx role

Deploys Nginx proxy with Let's Encrypt certificates and ModSecurity

## Requires

The Ansible Nginx role requires the following roles:

* docker
* docker-network
* modsecurity

## Usage

Configure the role.

**vars.yml**

```yml
certbot_image: certbot/certbot
certbot_hostname: cert01
certbot_data_dir: /usr/share/certbot01
certbot_email: info@example.com
certbot_stat_filter: "results[*] | [?stat.exists==`false`].item"

nginx_image: nginx:1.15-alpine
nginx_hostname: proxy01
nginx_data_dir: /usr/share/nginx01
nginx_proxies:
  - src_hostname: www.example.com
    src_port: 443
    dest_hostname: webserver
    dest_port: 80
    options: |
      add_header Strict-Transport-Security "max-age=15552000; includeSubdomains;"
    ssl: true
  - src_hostname: example.com
    redirect_hostname: www.example.com
  - src_hostname: example.org
    redirect_hostname: www.example.com
    server_names:
      - example.org
      - www.example.org
  - src_hostname: login.example.com
    src_port: 443
    ssl: true
    locations:
      - path: /
        dest_hostname: authserver
        dest_port: 8080
        options: |
          proxy_buffer_size 128k;
          proxy_buffers 4 256k;
          proxy_busy_buffers_size 256k;
```

And include it in your playbook.

```yml
- hosts: proxy
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: modsecurity
    tags: modsecurity
  - role: nginx
    tags: nginx
```

## Docs

Supported source ports are: 80 and 443.

## Troublshooting

### Connection refused

Error log:

```
2020/04/10 09:01:33 [error] 6#6: *30 connect() failed (111: Connection refused) while connecting to upstream, client: 84.72.20.219, server: nextcloud.mint-system.ch, request: "GET / HTTP/1.1", upstream: "http://172.19.0.8:80/", host: "nextcloud.mint-system.ch"
```

Solution: Restart the Nginx Docker container.

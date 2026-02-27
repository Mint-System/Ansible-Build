---
title: Nginx maintenance redirect script
---

# Run 08

Replace the `==` marked instructions in this file while you work on the task.

## Context

Read the `AGENTS.md` and `README.md` to get understanding of the project.

## Task

Create a script `nginx-maintance-redirect <path> <enable/disable>`

Example: `nginx-maintenance-redirect upgrade.ocad.com enable`

The script adds a redirect to `/etc/nginx/conf.d/static/maintenance.html`.

```
[bia /usr/share/nginx27/proxies]$ cat upgrade.ocad.com.conf
server {
    listen 80;
    server_name upgrade.ocad.com;
    location / {
        return 301 https://$host$request_uri;
        }

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
}

server {
    listen 443 ssl;
    server_name upgrade.ocad.com;
    ssl_certificate /etc/letsencrypt/live/upgrade.ocad.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/upgrade.ocad.com/privkey.pem;
    include /etc/nginx/conf.d/options-ssl-nginx.conf;
    ssl_dhparam /etc/nginx/conf.d/ssl-dhparams.pem;

    location / {
        include /etc/nginx/conf.d/proxy-params.conf;

                proxy_pass http://odoo17:8069;
        }

    location /websocket {
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        include /etc/nginx/conf.d/proxy-params.conf;

        proxy_pass http://odoo17:8072;
        }
    }
```


For the path `/usr/share/nginx27/proxies` use a variable `{{ nginx_data_dir }}/proxies`.

This script will be integrate into ans bile role like this:

```
- name: Copy {{ nginx_hostname }} templated scripts
  ansible.builtin.template:
    src: "{{ item }}"
    dest: /usr/local/bin/{{ item }}
    mode: +x
  loop:
    - nginx-maintance-redirect
```

## Worklog

==Fill this in as you work on the task==

## Summary

==Fill this once you completed the task==

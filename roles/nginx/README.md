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
certbot_email: info@mexample.com
certbot_stat_filter: "results[*] | [?stat.exists==`false`].item"

nginx_image: nginx:1.15-alpine
nginx_hostname: proxy01
nginx_data_dir: /usr/share/nginx01
nginx_proxies:
  - src_hostname: www.example.com
    src_port: 443
    dest_hostname: webserver
    dest_port: 80
````

And include it in your playbook.

```yml
- hosts: proxy
  roles:
  - { role: docker, tags: ["docker"] }
  - { role: docker-network, tags: ["docker-network"] }
  - { role: modsecurity, tags: ["modsecurity"] }
  - { role: nginx, tags: ["nginx"] }
```
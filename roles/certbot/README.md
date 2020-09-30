# Ansible Certbot role

Deploys Let's Encrypt certificates.

## Usage

Configure the role.

**vars.yml**

```yml
certbot_image: certbot/certbot
certbot_hostname: cert01
certbot_data_dir: /usr/share/certbot01
certbot_email: info@example.com
nginx_image: nginx:1.19.2-alpine
nginx_hostname: proxy01
nginx_data_dir: /usr/share/nginx01
nginx_proxies: # See nginx role for reference
```

And include it in your playbook.

```yml
- hosts: certbot
  roles:
  - role: certbot
```

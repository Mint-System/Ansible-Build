# Ansible Certbot role

Deploy Let's Encrypt certificates.

## Usage

Configure the role.

**vars.yml**

```yml
certbot_image: certbot/certbot
certbot_hostname: cert01
certbot_data_dir: /usr/share/cert # default: "/usr/share/{{ certbot_hostname }}"
certbot_email: info@example.com
nginx_image: nginx:1.19.2-alpine
nginx_hostname: nginx01
nginx_data_dir: /usr/share/nginx # default: "/usr/share/{{ nginx_hostname }}"
nginx_proxies: # See nginx role for reference
```

And include it in your playbook.

```yml
- hosts: certbot
  roles:
  - role: certbot
```

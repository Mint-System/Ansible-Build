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
certbot_preferred_challenges: "dns" # default: "http"
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

## Docs

For wildcard certificates set `certbot_preferred_challenges: http`. This will intentionally fail the certbot challenge and give you a manuall command, which must be executed on the server.

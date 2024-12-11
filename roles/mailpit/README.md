# Mailpit role

Deploy Mailpit container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/axllent/mailpit
mailpit_image: axllent/mailpit:latest
mailpit_description: Odoo Mail Catcher # default: Mailpit
mailpit_hostname: mailpit01
mailpit_data_dir: /usr/share/mailpit_data01 # default: "/usr/share/{{ mailpit_hostname }}"
mailpit_timezone: Europe/Paris # default: Europe/Zurich
mailpit_webroot: /mailpit/ # default: /
mailpit_users: # default: []
  - username: admin
    password: "{{ vault_mailpit_user_admin_password }}"
```

And include it in your playbook.

```yml
- hosts: mailpit
  roles:
  - role: mailpit
```

## Docs

### Nginx config

Setup this Nginx configuration for the `mailpit01` host:

```yaml
nginx_proxies:
  - src_hostname: www.example.com
    dest_hostname: webserver
    locations:
      - path: /mailpit
        dest_hostname: mailpit01
        dest_port: 8025
        options: |
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection $connection_upgrade; 
```

### Odoo config

To setup a outgoing mailpit connection simply use the hostname `mailpitXX` and port `1025`. 
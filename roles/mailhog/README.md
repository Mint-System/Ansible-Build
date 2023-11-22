# MailHog role

Deploy MailHog container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://registry.hub.docker.com/r/mailhog/mailhog/
mailhog_image: mailhog/mailhog:latest
mailhog_description: MailDev # default: MailHog
mailhog_hostname: mailhog01
mailhog_data_dir: /usr/share/mailhog_data01 # default: "/usr/share/{{ mailhog_hostname }}"
mailhoq_web_path: mailhog # default: ""
mailhog_users: # default: []
  - username: admin
    password: "{{ vault_mailhog_user_admin_password }}"
```

And include it in your playbook.

```yml
- hosts: mailhog
  roles:
  - role: mailhog
```

## Docs

### Nginx config

Setup this Nginx configuration for the `mailhog01` host:

```yaml
nginx_proxies:
  - src_hostname: www.example.com
    dest_hostname: webserver
    locations:
      - path: /mailhog
        dest_hostname: mailhog01
        dest_port: 8025
        options: |
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection $connection_upgrade; 
```

### Odoo config

To setup a outgoing mailhog connection simply use the hostname `mailogXX` and port `1025`. 
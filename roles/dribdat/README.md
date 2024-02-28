# dribdat role

Deploy dribdat container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/loleg/dribdat
dribdat_image: loleg/dribdat:latest
dribdat_description: dribdat Server # default: dribdat
dribdat_hostname: drib01
dribdat_volume_name: drib01_data # default: "{{ dribdat_hostname }}"
dribdat_server_name: hack.example.com
dribdat_secret: # default: "{{ vault_dribdat_secret }}"
dribdat_not_register: "true" # default: "false"
dribdat_postgres_hostname: postgres01
dribdat_postgres_database: drib # default: dribdat
dribdat_postgres_user: drub # default: dribdat
dribdat_postgres_password: # default: "{{ vault_dribdat_postgres_password }}"
dribdat_mail_server: mail.example.com
dribdat_mail_port: "587"
dribdat_mail_username: hack@example.com
dribdat_mail_password: # default: "{{ vault_dribdat_mail_password }}"
dribdat_mail_default_sender: hack@example.com
dribdat_mail_use_tls: "true"  # default: "false"
dribdat_mail_use_ssl: # default: "false"
dribdat_oauth_type: "gitlab"
dribdat_oauth_id: "2cd1a9807..."
dribdat_oauth_secret: # default: "{{ vault_dribdat_oauth_secret }}"
dribdat_s3_key: EXO78add691ee4d39b2318c75ed
dribdat_s3_secret: # default: "{{ vault_dribdat_s3_secret }}"
dribdat_s3_bucket: hack.example.com
dribdat_s3_region: ch-dk-2
dribdat_s3_https: https://sos-ch-dk-2.exo.io/hack.example.com
dribdat_s3_endpoint: https://sos-ch-dk-2.exo.io
dribdat_volume_backup_set: # See restic_backup_set var in role restic_client
```

And include it in your playbook.

```yml
- hosts: dribdat
  roles:
  - role: dribdat
```

## Docs

### Nginx config

Setup this Nginx configuration for the `drib01` host:

```yaml
nginx_http_options: |
  map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
  }
nginx_proxies:
  - src_hostname: hack.example.com
    dest_hostname: drib01
    dest_port: 5000
    ssl: true
    monitor: false
    options: |
      proxy_set_header Host $host;
      include /etc/letsencrypt/proxy-params.conf;
```

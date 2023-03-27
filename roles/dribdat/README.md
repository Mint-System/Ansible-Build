# dribdat role

Deploy dribdat container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/loleg/dribdat
dribdat_image: loleg/dribdat:stable
dribdat_description: dribdat Server # default: dribdat
dribdat_hostname: drib01
dribdat_volume_name: drib01_data # default: "{{ dribdat_hostname }}"
dribdat_server_name: hack.example.com
dribdat_secret: # deafult: "{{ vault_dribdat_secret }}"
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
dribdat_volume_backup_set: # See restic_backup_set var in role restic-client
```

And include it in your playbook.

```yml
- hosts: dribdat
  roles:
  - role: dribdat
```

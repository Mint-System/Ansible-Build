# Matomo role

Deploy Matomo container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/matomo
matomo_image: matomo:php:8.2-apache
matomo_build_image: true # default: false
matomo_hostname: mat01
matomo_description: MA # default: Matomo
matomo_volume_name: mat_data01 # default: "{{ matomo_hostname }}"
matomo_volume_backup_set: # See restic_backup_set var in role restic_client
matomo_db_hostname: mysql01
matomo_db_user: matomo
matomo_db_name: matomo
matomo_db_password: # default: "{{ vault_matomo_db_password }}"
```

And include it in your playbook.

```yml
- hosts: matomo
  roles:
  - role: matomo
```

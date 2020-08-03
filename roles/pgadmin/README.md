# Ansible pgAdmin role

Deploys pgAdmin database container

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/dpage/pgadmin4/
pgadmin_image: dpage/pgadmin4:4.24
pgadmin_hostname: pgadmin01
pgadmin_volume_name: pgadmin_data01
pgadmin_user: admin@example.com
pgadmin_password: "{{ vault_pgadmin_password }}"
```

And include it in your playbook.

```yml
- hosts: pgadmin
  roles:
  - role: pgadmin
    tags: pgadmin
```

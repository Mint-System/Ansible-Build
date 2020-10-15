# Ansible pgAdmin role

Deploy pgAdmin container

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/dpage/pgadmin4/
pgadmin_image: dpage/pgadmin4:4.24
pgadmin_hostname: pgadmin01
pgadmin_description: Admin for postgres01  # default: pgAdmin
pgadmin_volume_name: pgadmin_data01
pgadmin_data_dir: /usr/share/pgadmin01
pgadmin_user: admin@example.com
pgadmin_password: "{{ vault_pgadmin_password }}"
pgadmin_servers:
  - name: Example Database
    host: postgres01
    username: example
    password: "{{ vault_pgadmin_example_password }}"
```

And include it in your playbook.

```yml
- hosts: pgadmin
  roles:
  - role: pgadmin
```

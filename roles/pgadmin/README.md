# pgAdmin role

Deploy pgAdmin container

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/dpage/pgadmin4/
pgadmin_image: dpage/pgadmin4:7.6
pgadmin_hostname: pgadmin01
pgadmin_description: Admin for postgres01 # default: pgAdmin
pgadmin_volume_name: pgadmin_data01 # default: "{{ pgadmin_hostname }}"
pgadmin_data_dir: /usr/share/pgadmin # default: /usr/share/{{ pgadmin_hostname }}
pgadmin_user: admin@example.com
pgadmin_password: "{{ vault_pgadmin_password }}"
pgadmin_servers:
  - name: Example Database Server
    host: postgres01
    username: example
pgadmin_script_name: /pgadmin4 # default: ""
```

And include it in your playbook.

```yml
- hosts: pgadmin
  roles:
  - role: pgadmin
```

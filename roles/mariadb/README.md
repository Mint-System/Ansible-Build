# MariaDB role

Deploy MariaDB database container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/_/mariadb
mariadb_image: mariadb:10.7.1
mariadb_hostname: mariadb01
mariadb_description: database for frappe # default: MariaDB
mariadb_volume_name: mariadb_data01 # default: "{{ mariadb_hostname }}"
mariadb_root_password: # default: "{{ vault_mariadb_root_password }}"
mariadb_database: example
mariadb_user: example
mariadb_password: # default: "{{ vault_mariadb_password }}"
mariadb_command: --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci # default: ""
```

Backup databases.

```yml
mariadb_backup_set: # See restic_backup_set var in role restic_client
  - id: "mariadb dump frappe"
    type: mariadb-dump
    container: mariadb01
    databases: frappe 
    tags:
      - mariadb
      - mariadb01
    hour: "1"
```

And include it in your playbook.

```yml
- hosts: mariadb
  roles:
  - role: mariadb
```

## Docs

### Set max connections

Add the `--max_connections=#` param to the MAriaDB command.

```yml
mariadb_command: --max-connections=1000
```

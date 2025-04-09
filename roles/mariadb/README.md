<img src="/logos/mariadb.png" alt="mariadb logo" width="100" height="100">

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
mariadb_backup_set: # See restic_backup_set var in role restic
```

And include it in your playbook.

```yml
- hosts: mariadb
  roles:
  - role: mariadb
```

The following tags are available:

* mariadb
* mariadb_backup

## Docs

### Set max connections

Add the `--max_connections=#` param to the MAriaDB command.

```yml
mariadb_command: --max-connections=1000
```

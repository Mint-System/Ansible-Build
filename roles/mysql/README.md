# Ansible MySQL role

Deploy MySQL database container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/mysql
mysql_image: mysql:5
mysql_hostname: mysql01
mysql_description: database for moodle # default: MySQL
mysql_volume_name: mysql_data01 # default: "{{ mysql_hostname }}"
mysql_root_password: "{{ vault_mysql_root_password }}"
mysql_database: example
mysql_user: example
mysql_password:  "{{ vault_mysql_password }}"
```

Backup databases.

```yml
mysql_backup_set: # See restic_backup_set var in role restic-client
  - id: "mysql dump wordpress"
    type: mysql-dump
    container: mysql01
    databases: moodle 
    tags:
      - mysql
      - mysql01
    hour: "1"
```

And include it in your playbook.

```yml
- hosts: mysql
  roles:
  - role: mysql
```

# MySQL role

Deploy MySQL database container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/_/mysql
mysql_image: mysql:5
mysql_hostname: mysql01
mysql_description: database for moodle # default: MySQL
mysql_volume_name: mysql_data01 # default: "{{ mysql_hostname }}"
mysql_data_dir: /usr/share/mysql # default: "/usr/share/{{ mysql_hostname }}"
mysql_root_password: # default: "{{ vault_mysql_root_password }}"
mysql_database: example
mysql_user: example
mysql_password: # default: "{{ vault_mysql_password }}"
mysql_memory_limit: 4294967296 # default: 2147483648 (2 GB)
```

Backup databases.

```yml
mysql_backup_set: # See restic_backup_set var in role restic
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

## Docs

### Install command line tools

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/mysql/files/install | bash` in your terminal.

### Execute sql query in container

Enter the mysql cli with `docker exec -it mysql01 sh -c 'mysql -u root -p"$MYSQL_ROOT_PASSWORD"'` and run the query:

```sql
show global variables like 'log_bin';
```

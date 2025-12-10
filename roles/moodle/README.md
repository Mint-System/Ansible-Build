<img src="/logos/moodle.png" alt="moodle logo" width="100" height="100">

# Moodle role

Deploy Moodle Docker container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/bitnami/moodle
moodle_image: bitnami/moodle:4.0
moodle_hostname: moodle01
moodle_volume_name: moodle_data01 # default: "{{ moodle_hostname }}"
moodle_username: admin
moodle_password: "{{ vault_moodle_password }}"
moodle_email: moodle@example.com
moodle_site_name: "School of Example"
moodle_skip_install: "true" # default: "false"
moodle_database_type: mysqli # default: mariadb
moodle_mysql_client_flavor: mysql # default: mariadb
moodle_mysql_database_root_password: "{{ vault_moodle_mysql_database_root_password }}"
moodle_database_host: postgres05
moodle_database_name: moodle
moodle_database_user: moodle
moodle_database_password: "{{ vault_moodle_database_password }}"
moodle_smtp_host: mail.example.com
moodle_smtp_port: "933" # default: "587
moodle_smtp_user: bot@example.com
moodle_smtp_password: "{{ vault_moodle_smtp_password }}" 
moodle_smtp_protocol: ssl # default: tls
moodle_php_max_upload_filesize: 128M # default 32M
moodle_volume_backup_set: # See restic_backup_set var in role restic
```

And include it in your playbook.

```yml
- hosts: moodle
  roles:
  - role: moodle
```

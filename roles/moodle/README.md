# Ansible Moodle role

Deploys Moodle Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/venatorfox/moodle/
moodle_image: venatorfox/moodle:MOODLE_38_STABLE
moodle_hostname: moodle01
moodle_volume_name: moodle_data01
moodle_admin_email: admin@example.com
moodle_admin_user: admin
moodle_admin_password: "{{ vault_moodle_admin_password }}"
moodle_db_type: pgsql
moodle_db_hostname: postgres05
moodle_db_user: moodle
moodle_db_password: "{{ vault_postgres_password }}"
moodle_db_name: moodle
moodle_ssl: "true"
moodle_url: "https://moodle.example.com"
moodle_fullname: "School of Example"
moodle_shortname: "ScEx"
moodle_summary: "This is the LMS for School of Example"
```

And include it in your playbook.

```yml
- hosts: moodle
  roles:
  - role: moodle
    tags: moodle
```

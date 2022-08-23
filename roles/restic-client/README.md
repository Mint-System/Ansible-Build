# Restic client role

Configures Restic client backup jobs.

## Usage

Configure the role.

**vars.yml**

```yml
restic_client_user: restic-user # default: restic
restic_client_password: "{{ vault_restic_client_password }}"
restic_repo: "restic.example.com/{{ inventory_hostname }}"
restic_repo_password: "{{ vault_restic_repo_password }}"
restic_backup_set:
  - id: "docker volume backup moodle01"
    type: docker-volume
    container: moodle01
    tags:
      - moodle
      - moodle01
    hour: "1"
 - id: "docker volume backup postgres_data01"
   type: docker-volume
   volume: postgres_data01
   tags:
    - postgres
    - postgres01
   hour: "1"
- id: "data dir backup bookstack01"
  type: file
  path: /usr/share/bookstack01
  tags:
    - bookstack
    - bookstack01
  hour: "1"
  status: absent
- id: "odoo backup odoo01"
  type: odoo-backup
  host: http://localhost:8070
  database: odoo
  tags:
    - odoo
    - odoo01
  hour: "1"
- id: "docker odoo backup odoo02"
  type: docker-odoo-backup
  container: odoo02
  database: odoo2
  tags:
    - odoo
    - odoo02
  hour: "2"
- id: "postgres dump backup postgres01"
  type: postgres-dump
  container: postgres01
  databases: odoo
  tags:
    - postgres
    - postgres01
  hour: "1"
  disabled: true
- id: "postgres dump backup postgres01 all"
  type: postgres-dump
  container: postgres01
  tags:
    - postgres
    - postgres01
  hour: "1"
- id: "mysql dump backup mysql01"
  type: mysql-dump
  container: mysql01
  databases: wordpress,wordpress2
  tags:
    - mysql
    - mysql01
  hour: "1"
  disabled: true
- id: "postgres dump backup mysql01 all"
  type: mysql-dump
  container: mysql01
  tags:
    - mysql
    - mysql01
  hour: "1"
- id: "mariadb dump backup mariadb01"
  type: mariadb-dump
  container: mariadb01
  databases: frappe
  tags:
    - mariadb
    - mariadb01
  hour: "1"
restic_backup_rotation:
  daily: 7 # default: 7
  weekly: 4 # default: 4
  monthly: 1 # default: 1
```

And include it in your playbook.

```yml
- hosts: restic-client
  roles:
  - role: restic-client
```

## Docs

### Backup types

These backup types are available:

* mariadb-dump
* mysql-dump
* postges-dump
* docker-odoo-backup
* odoo-backup
* file
* docker-volume

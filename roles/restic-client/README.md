# Ansible Restic client role

Configures Restic client backup jobs.

## Usage

Configure the role.

**vars.yml**

```yml
restic_client_user: restic
restic_client_password: "{{ vault_restic_client_password }}"
restic_repo: restic.example.com:8080
restic_repo_password: "{{ vault_restic_repo_password }}"
restic_odoo_master_password: "{{ vault_restic_odoo_master_password }}"
restic_backup_sets:
 - id: "postgres volume"
   type: docker-volume
   volume: postgres_data01
   tags:
    - postgres
    - postgres01
   hour: "1"
   minute: "0"
- id: "bookstack data dir"
  type: file
  path: /usr/share/bookstack01
  tags:
    - bookstack
    - bookstack01
  hour: "1"
  minute: "10"
- id: "odoo backup"
  type: odoo-backup
  host: http://localhost:8070
  database: odoo
  tags:
    - odoo
    - odoo01
  hour: "1"
  minute: "30"
- id: "postgres dump postgres06"
  type: postgres-dump
  container: postgres01
  databases: odoo
  tags:
    - postgres
    - postgres01
  hour: "1"
  minute: "50"
  disabled: true
restic_backup_rotation:
  daily: 7
  weekly: 4
  monthly: 1
```

And include it in your playbook.

```yml
- hosts: restic-client
  roles:
  - role: restic-client
    tags: restic-client
```

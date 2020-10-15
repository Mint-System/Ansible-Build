# Ansible Restic client role

Configures Restic client backup jobs.

## Usage

Configure the role.

**vars.yml**

```yml
restic_client_user: restic-user # default: restic
restic_client_password: "{{ vault_restic_client_password }}"
restic_repo: "restic.example.com//{{ inventory_hostname }}"
restic_repo_password: "{{ vault_restic_repo_password }}"
restic_backup_sets:
 - id: "postgres volume"
   type: docker-volume
   volume: postgres_data01
   tags:
    - postgres
    - postgres01
   hour: "1"
- id: "bookstack data dir"
  type: file
  path: /usr/share/bookstack01
  tags:
    - bookstack
    - bookstack01
  hour: "1"
  disabled: absent
- id: "odoo backup"
  type: odoo-backup
  host: http://localhost:8070
  database: odoo
  tags:
    - odoo
    - odoo01
  hour: "1"
- id: "postgres dump odoo"
  type: postgres-dump
  container: postgres01
  databases: odoo
  tags:
    - postgres
    - postgres01
  hour: "1"
  disabled: true
- id: "postgres dump all"
  type: postgres-dump
  container: postgres01
  tags:
    - postgres
    - postgres01
  hour: "1"
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
```

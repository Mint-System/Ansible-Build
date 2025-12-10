<img src="/logos/postgres.png" alt="postgres logo" width="100" height="100">

# PostgreSQL role

Deploy PostgreSQL database container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/_/postgres
postgres_image: postgres:14-alpine
postgres_build_image: true # default: false
postgres_description: Database for website # default: PostgreSQL
postgres_hostname: postgres01
postgres_volume_name: postgres_data01 # default: "{{ postgres_hostname }}"
postgres_data_dir: /usr/share/postgres # default: "/usr/share/{{ postgres_hostname }}"
postgres_scripts_dir: /home/odoo-prod/bin # default: /usr/local/bin
postgres_volumes:
  - "{{ postgres_data_dir }}/reference-data/data:/mnt/reference-data" # default: "{{ postgres_volume_name }}:/var/lib/postgresql/data"
postgres_ports:
  - 127.0.0.1:5433:5432 # default: []
postgres_user: example
postgres_password: # default: "{{ vault_postgres_password }}"
postgres_configmap: # default: - name: "{{ postgres_user }}"
  - db: example-prod
  - db: example-int
postgres_wal_level: logical # default: replica
postgres_max_connections: 200 # default: 100
postgres_users:
  - name: dwh
    password: "{{ vault_postgres_users_dwh_password }}"
    grant_databases:
     - odoo-prod
     - odoo-int
     - odoo-dev
    connection_rules:
      - source: 95.15.213.106/24
        database: odoo-prod
      - source: 95.15.213.106/24
        database: odoo-int
    revoke_tables:
      - name: hr_employee
        database: odoo-prod
      - name: hr_employee
        database: odoo-int
postgres_backup_set: # See restic_backup_set var in role restic
```

And include it in your playbook.

```yml
- hosts: postgres
  roles:
  - role: postgres
```

The following tags are available:

* postgres
* postgres_backup

## Troubleshooting

### Lock file postmaster.pid is empty

**Problem**

The container does not start.

```
2025-04-24 07:40:10.592 UTC [1] FATAL:  lock file "postmaster.pid" is empty
2025-04-24 07:40:10.592 UTC [1] HINT:  Either another server is starting, or the lock file is the remnant of a previous server startup crash.
```

**Solution**

Navigate into the Postgres volume and remote the pid file.

```bash
rm postmaster.pid
docker restart postgres01
```

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
postgres_volumes:
  - "{{ postgres_data_dir }}/reference-data/data:/mnt/reference-data" # default: "{{ postgres_volume_name }}:/var/lib/postgresql/data"
postgres_ports:
  - 127.0.0.1:5433:5432 # default: []
postgres_user: example
postgres_password: # default: "{{ vault_postgres_password }}"
postgres_config_map: # default: - name: "{{ postgres_user }}"
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
```

Backup databases.

```yml
postgres_backup_set: # See restic_backup_set var in role restic
  - id: "{{ postgres_hostname }} dump"
    type: postgres-dump
    container: "{{ postgres_hostname }}"
    tags:
      - postgres
      - "{{ postgres_hostname }}"
    hour: "1"
```

And include it in your playbook.

```yml
- hosts: postgres
  roles:
  - role: postgres
```

### Kubernetes

Configure the manifest.

```yml
k8s_postgres_image: postgres:16-alpine
k8s_postgres_user: example
k8s_postgres_password: test
k8s_postgres_db: example
```

And include it in your localhost playbook.

```yml
- hosts: localhost
  roles:
  - role: postgres
```

## Docs

### Install command line tools

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/postgres/files/install | bash` in your terminal.

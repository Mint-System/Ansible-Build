# PostgreSQL role

Deploy PostgreSQL database container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/postgres
postgres_image: postgres:12-alpine
postgres_build_image: true # default: false
postgres_description: Database for website # default: PostgreSQL
postgres_hostname: postgres01
postgres_volume_name: postgres_data01 # default: "{{ postgres_hostname }}"
postgres_data_dir: postgres_conf01 # default: "/usr/share/{{ postgres_hostname }}"
postgres_ports:
  - 127.0.0.1:5433:5432 # default: []
postgres_user: example
postgres_password: # default: "{{ vault_postgres_password }}"
postgres_db: example # default: "{{ postgres_user }}"
postgres_users:
  - name: powerbi
    password: "{{ vault_postgres_users_powerbi_password }}"
    grant_databases:
     - odoo-main
     - odoo-int
     - odoo-dev
    connection_rules:
      - source: 95.15.213.106/24
        database: odoo-main
      - source: 95.15.213.106/24
        database: odoo-int
    revoke_tables:
      - name: hr_employee
        database: odoo-main
      - name: hr_employee
        database: odoo-int
```

Backup databases.

```yml
postgres_backup_set: # See restic_backup_set var in role restic_client
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

## Docs

### Install command line tools

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/master/roles/postgres/files/install | bash` in your terminal.

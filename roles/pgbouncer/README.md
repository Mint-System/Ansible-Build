<img src="/logos/pgbouncer.png" alt="pgbouncer logo" width="100" height="100">

# PgBouncer role

Deploy PgBouncer container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/edoburu/pgbouncer/
pgbouncer_image: edoburu/pgbouncer:v1.25.1-p0
pgbouncer_description: Database Proxy # default: PgBouncer
pgbouncer_hostname: pgbouncer01
pgbouncer_data_dir: /usr/share/pgbouncer # default: "/usr/share/{{ pgbouncer_hostname }}"
pgbouncer_ports:
  - 0.0.0.0:5433:5432 # default: []
pgbouncer_configmap: # default: "{{ postgres_configmap }}"
  - db: example-prod
  - db: example-int
pgbouncer_url: # default: "postgres://{{ postgres_user }}:{{ postgres_password }}@{{ postgres_hostname }}/{{ item.db }}"
```

And include it in your playbook.

```yml
- hosts: pgbouncer
  roles:
  - role: pgbouncer
```

## Docs

### Test tls connection

On your client run this command:

```bash
psql "postgresql://example:test@localhost:5433/example-prod?sslmode=require"
```

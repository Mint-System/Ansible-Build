# Scripts

The following Ansible roles contain command line tools that can be used independent of Ansible.

## [ansible_scripts](roles/ansible_scripts/README.md)

```bash
curl -L https://ansible.build/ansible_scripts/install | bash
```

- ansible-vault-get

## [cron](roles/cron/README.md)

```bash
curl -L https://ansible.build/cron/install | bash
```

- cron-job-run
- cron-job-list

## [certbot](roles/certbot/README.md)

```bash
curl -L https://ansible.build/certbot/install | bash
```

- docker-certbot-delete
- docker-certbot-create


## [docker_volume](roles/docker_volume/README.md)

```bash
curl -L https://ansible.build/docker_volume/install | bash -s -- --user
```

- docker-disk-usage
- docker-volume-backup
- docker-volume-export
- docker-volume-import
- docker-volume-list
- docker-volume-restore
- docker-volume-copy


## [grafana](roles/grafana/README.md)

```bash
curl -L https://ansible.build/grafana/install | bash
```

- grafana-backup


## [mysql](roles/mysql/README.md)

```bash
curl -L https://ansible.build/mysql/install | bash
```

- docker-mysql-backup
- docker-mysql-list
- docker-mysql-restore
- docker-mysql-drop


## [nginx](roles/nginx/README.md)

```bash
curl -L https://ansible.build/nginx/install | bash
```

- docker-nginx-enable
- docker-nginx-reload
- get-public-ip


## [node_exporter](roles/node_exporter/README.md)

```bash
curl -L https://ansible.build/node_exporter/install | bash
```

- write-node-exporter-metric


## [odoo](roles/odoo/README.md)

```bash
curl -L https://ansible.build/odoo/install | bash -s -- --user
```

- docker-odoo-backup
- docker-odoo-clear-assets
- docker-odoo-clear-views
- docker-odoo-cloc
- docker-odoo-drop
- docker-odoo-duplicate
- docker-odoo-init
- docker-odoo-list
- docker-odoo-patch
- docker-odoo-restore
- docker-odoo-shell
- docker-odoo-uninstall
- docker-odoo-update
- docker-odoo-user
- docker-odoo-neutralize
- docker-odoo-rename
- docker-odoo-upgrade
- odoo-backup
- odoo-drop
- odoo-duplicate
- odoo-restore

## [postgres](roles/postgres/README.md)

```bash
curl -L https://ansible.build/postgres/install | bash -s -- --user
```

- docker-postgres-backup
- docker-postgres-create
- docker-postgres-restore
- docker-postgres-list
- docker-postgres-drop
- docker-postgres-patch
- docker-postgres-duplicate
- docker-postgres-size
- docker-postgres-shell
- docker-postgres-upgrade
- docker-postgres-rename

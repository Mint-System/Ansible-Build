# Scripts

The following Ansible roles contain command line tools that can be used independent of Ansible.

## [ansible_scripts](role/ansible_scripts/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/ansible_scripts/files/install | bash
```

- ansible-vault-get
  
## [odoo_scripts](roles/odoo_scripts/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/odoo_scripts/files/install | bash
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
- odoo-user

## [nginx](roles/nginx/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/nginx/files/install | bash
```

- docker-nginx-enable
- docker-nginx-reload
- get-public-ip

## [node_exporter](roles/node_exporter/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/node_exporter/files/install | bash
```

- write-node-exporter-metric

## [mysql](roles/mysql/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/mysql/files/install | bash
```

- docker-mysql-backup
- docker-mysql-list
- docker-mysql-restore
- docker-mysql-drop

## [grafana](roles/grafana/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/grafana/files/install | bash
```

- grafana-backup

## [postgres](roles/postgres/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/postgres/files/install | bash
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

## [docker_volume](roles/docker_volume/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/docker_volume/files/install | bash
```

- docker-volume-backup
- docker-volume-restore
- docker-volume-copy

## [certbot](roles/certbot/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/certbot/files/install | bash
```

- docker-certbot-delete
- docker-certbot-create

## [restic](roles/restic/README.md)

```bash
curl -L https://raw.githubusercontent.com/mint-system/ansible-build/main/roles/restic/files/install | bash
```

- cron-job-run
- cron-job-list
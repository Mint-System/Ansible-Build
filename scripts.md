# Scripts

The following Ansible roles contain command line tools that can be used independent of Ansible.

## [ansible_scripts](roles/ansible_scripts/README.md)

```bash
curl -L https://ansible.build/ansible_scripts/install | bash -s -- --user
```

- [ansible-vault-get](https://github.com/Mint-System/Ansible-Build/blob/main/roles/ansible_scripts/files/ansible-vault-get)

## [cron](roles/cron/README.md)

```bash
curl -L https://ansible.build/cron/install | bash -s -- --user
```

- [cron-job-run](https://github.com/Mint-System/Ansible-Build/blob/main/roles/cron/files/cron-job-run)
- [cron-job-list](https://github.com/Mint-System/Ansible-Build/blob/main/roles/cron/files/cron-job-list)
- [write-node-exporter-metric](https://github.com/Mint-System/Ansible-Build/blob/main/roles/cron/files/write-node-exporter-metric)

## [certbot](roles/certbot/README.md)

```bash
curl -L https://ansible.build/certbot/install | bash -s -- --user
```

- [docker-certbot-delete](https://github.com/Mint-System/Ansible-Build/blob/main/roles/certbot/files/docker-certbot-delete)
- [docker-certbot-create](https://github.com/Mint-System/Ansible-Build/blob/main/roles/certbot/files/docker-certbot-create)

## [docker](roles/docker/README.md)

```bash
curl -L https://ansible.build/docker/install | bash -s -- --user
```

- [docker-export](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker/files/docker-export)
- [docker-import](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker/files/docker-import)

## [docker_volume](roles/docker_volume/README.md)

```bash
curl -L https://ansible.build/docker_volume/install | bash -s -- --user
```

- [docker-disk-usage](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker_volume/files/docker-disk-usage)
- [docker-volume-backup](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker_volume/files/docker-volume-backup)
- [docker-volume-export](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker_volume/files/docker-volume-export)
- [docker-volume-import](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker_volume/files/docker-volume-import)
- [docker-volume-list](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker_volume/files/docker-volume-list)
- [docker-volume-restore](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker_volume/files/docker-volume-restore)
- [docker-volume-copy](https://github.com/Mint-System/Ansible-Build/blob/main/roles/docker_volume/files/docker-volume-copy)


## [grafana](roles/grafana/README.md)

```bash
curl -L https://ansible.build/grafana/install | bash -s -- --user
```

- [grafana-backup](https://github.com/Mint-System/Ansible-Build/blob/main/roles/grafana/files/grafana-backup)


## [mysql](roles/mysql/README.md)

```bash
curl -L https://ansible.build/mysql/install | bash -s -- --user
```

- [docker-mysql-backup](https://github.com/Mint-System/Ansible-Build/blob/main/roles/mysql/files/docker-mysql-backup)
- [docker-mysql-list](https://github.com/Mint-System/Ansible-Build/blob/main/roles/mysql/files/docker-mysql-list)
- [docker-mysql-restore](https://github.com/Mint-System/Ansible-Build/blob/main/roles/mysql/files/docker-mysql-restore)
- [docker-mysql-drop](https://github.com/Mint-System/Ansible-Build/blob/main/roles/mysql/files/docker-mysql-drop)


## [nginx](roles/nginx/README.md)

```bash
curl -L https://ansible.build/nginx/install | bash -s -- --user
```

- [docker-nginx-enable](https://github.com/Mint-System/Ansible-Build/blob/main/roles/nginx/files/docker-nginx-enable)
- [docker-nginx-reload](https://github.com/Mint-System/Ansible-Build/blob/main/roles/nginx/files/docker-nginx-reload)
- [get-public-ip](https://github.com/Mint-System/Ansible-Build/blob/main/roles/nginx/files/get-public-ip)

## [odoo](roles/odoo/README.md)

```bash
curl -L https://ansible.build/odoo/install | bash -s -- --user
```

- [docker-odoo-backup](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-backup)
- [docker-odoo-clear-assets](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-clear-assets)
- [docker-odoo-clear-views](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-clear-views)
- [docker-odoo-cloc](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-cloc)
- [docker-odoo-drop](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-drop)
- [docker-odoo-duplicate](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-duplicate)
- [docker-odoo-init](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-init)
- [docker-odoo-list](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-list)
- [docker-odoo-patch](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-patch)
- [docker-odoo-restore](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-restore)
- [docker-odoo-shell](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-shell)
- [docker-odoo-uninstall](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-uninstall)
- [docker-odoo-update](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-update)
- [docker-odoo-user](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-user)
- [docker-odoo-neutralize](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-neutralize)
- [docker-odoo-rename](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-rename)
- [docker-odoo-upgrade](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/docker-odoo-upgrade)
- [odoo-backup](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/odoo-backup)
- [odoo-drop](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/odoo-drop)
- [odoo-duplicate](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/odoo-duplicate)
- [odoo-restore](https://github.com/Mint-System/Ansible-Build/blob/main/roles/odoo/files/odoo-restore)

## [postgres](roles/postgres/README.md)

```bash
curl -L https://ansible.build/postgres/install | bash -s -- --user
```

- [docker-postgres-backup](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-backup)
- [docker-postgres-create](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-create)
- [docker-postgres-restore](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-restore)
- [docker-postgres-list](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-list)
- [docker-postgres-drop](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-drop)
- [docker-postgres-patch](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-patch)
- [docker-postgres-duplicate](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-duplicate)
- [docker-postgres-size](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-size)
- [docker-postgres-shell](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-shell)
- [docker-postgres-upgrade](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-upgrade)
- [docker-postgres-rename](https://github.com/Mint-System/Ansible-Build/blob/main/roles/postgres/files/docker-postgres-rename)

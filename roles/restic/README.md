<img src="/logos/restic.png" alt="restic logo" width="100" height="100">

# Restic role

Configures Restic backup jobs.

## Usage

Configure the role.

```yml
restic_backup_dir: /srv/backup # default: /var/backup
restic_owner: backup # default: root
restic_group: backup # default: root
restic_repo: "restic.example.com/{{ inventory_hostname }}"
restic_repo_password: # default: "{{ vault_restic_repo_password }}"
restic_rest_user: rest-user # default: restic
restic_rest_password: # default "{{ vault_restic_rest_password }}"
restic_backup_set:

  - id: "docker volume backup jenkins01"
    upload: false
    type: docker-volume
    container: jenkins01
    exclude: workspace
    tags:
      - moodle
      - jenkins01
    hour: "1"

  - id: "docker volume backup postgres_data01"
    type: docker-volume
    container: postgres01
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
    state: absent

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
- hosts: restic
  roles:
  - role: restic
```

## Docs

### Show restic version

Show restic version for alls hosts.

```bash
ansible all -i inventories/setup -a "restic version"
```

### Setup a local repository

Set these env vars for local repsitory:

```yaml
restic_repo_type: local # default: rest
restic_repo: /home/backup
```

### Delete all snaphots

Run these commands to remove all snapshots:

```bash
restic forget --keep-last 1 --prune
restic forget --prune latest
```

### Backup types

These backup types are available:

* mariadb-dump
* mysql-dump
* postges-dump
* docker-volume
* docker-odoo-backup
* odoo-backup
* file

## Docs

### Change backup path

The backup paths can be changed manually. Ensure that you have set `restic_backup_dir: /mnt/db/backup`.

Navigate into the crontabs folder and replace the backup paths.

```bash
cd /var/spool/cron/crontabs/

# Change default paths
sed -i 's|/var/tmp|/var/backup|g' root
sed -i 's|/var/backup|/var/backup|g' root
sed -i 's|/mnt/sdb/tmp|/var/backup|g' root

# If the server has external disk
sed -i 's|/var/backup|/mnt/sdb/backup|g' root
```

### Install with script

If the restic package is outdated, you can install it from source.

```bash
wget https://github.com/restic/restic/releases/download/v0.18.0/restic_0.18.0_linux_amd64.bz2
bunzip2 restic_0.18.0_linux_amd64.bz2
sudo mv restic_0.18.0_linux_amd64 /usr/local/bin/restic
sudo chmod +x /usr/local/bin/restic
restic version
```

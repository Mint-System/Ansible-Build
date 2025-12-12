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

  - id: "Backup Jenkins volume"
    upload: false
    type: docker-volume
    container: jenkins01
    exclude: workspace
    tags:
      - moodle
      - jenkins01
    hour: "1"

  - id: "Backup Postgres volume"
    type: docker-volume
    container: postgres01
    volume: postgres_data01
    tags:
    - postgres
    - postgres01
    hour: "1"

  - id: "Backup Bookstack files"
    type: file
    path: /usr/share/bookstack01
    tags:
      - bookstack
      - bookstack01
    hour: "1"
    state: absent

  - id: "Backup Odoo databse"
    type: docker-odoo-backup
    container: odoo02
    database: odoo2
    tags:
      - odoo
      - odoo02
    hour: "2"

  - id: "Backup Postgres database"
    type: postgres-dump
    container: postgres01
    databases: odoo
    tags:
      - postgres
      - postgres01
    hour: "1"
    disabled: true

  - id: "Backup Postgres databases"
    type: postgres-dump
    container: postgres01
    tags:
      - postgres
      - postgres01
    hour: "1"

  - id: "Backup MySQL database"
    type: mysql-dump
    container: mysql01
    databases: wordpress,wordpress2
    tags:
      - mysql
      - mysql01
    hour: "1"
    disabled: true

  - id: "Backup MySQL databases"
    type: mysql-dump
    container: mysql01
    tags:
      - mysql
      - mysql01
    hour: "1"

  - id: "Backup MariaDB database"
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

### Rename cron job

When choosing the job id it is recommended to not add configuraiton details of the backup job to the name. Once the definition has been applied, the job id can not be updated with Ansible.

```bash
job_name="Backup job odoo backup shop"
new_job_name="Backup Odoo database"

# Rename job in crontab
cd /var/spool/cron/crontabs/
sed -i "s|$job_name|$new_job_name|g" root
grep "$new_job_name" root

# Show the grafana job metric
rg "$job_name" /var/tmp/*.prom
```

### Fix cron commands

Fixing cron commands across all servers is a more difficult task, but rather easy with ansible.

In this example the pattern ` restic ` is replaced with ` restic-main ` in all cron jobs. The cron file can be located at `/var/spool/cron/root` or `/var/spool/cron/crontabs/root`.

Run this command to get an overview of all cron jobs that match the pattern:

```bash
task run all -i inventories/setup -b -m shell -a 'if [ -f /var/spool/cron/root ] && grep -q " restic " /var/spool/cron/root; then echo "<<< $(hostname) >>>"; grep " restic " /var/spool/cron/root; fi; if [ -f /var/spool/cron/crontabs/root ] && grep -q " restic " /var/spool/cron/crontabs/root; then echo "<<< $(hostname) >>>"; grep " restic " /var/spool/cron/crontabs/root; fi'
```

If your confident and did a test with a single host, run this command to replace the pattern:

```bash
task run all -i inventories/setup -b -m shell -a 'if [ -f /var/spool/cron/root ] && grep -q " restic " /var/spool/cron/root; then sed -i "s/ restic / restic-main /g" /var/spool/cron/root; fi; if [ -f /var/spool/cron/crontabs/root ] && grep -q " restic " /var/spool/cron/crontabs/root; then sed -i "s/ restic / restic-main /g" /var/spool/cron/crontabs/root; fi'
```
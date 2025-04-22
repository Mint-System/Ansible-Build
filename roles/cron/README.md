<img src="/logos/cron.png" alt="cron logo" width="100" height="100">

# cron role

Setup cron jobs.

## Usage

Configure the role.

```yml
cron_data_dir: /mnt/sdb/share/cron # default: /usr/share/{{ role_name }}
cron_jobs:
  - name: Run cron scheduler
    command: curl https://moodle.example.com/admin/cron.php
    hour: "4" # default: '*'
    minute: "1" # default: '*'
    disabled: true
  - id: "Run job sync folder"
    user: bot
    command: "script"
    minute: "*/10" # Every ten minutes
    script_name: hello-world
    script: |
      #!/bin/bash
      echo "hello world"
```

And include it in your playbook.

```yml
- hosts: cron
  roles:
  - role: cron
```

## Docs

### Change backup path

The backup paths can be changed manually. Ensure that you have set `restic_backup_dir: /mnt/db/backup`.

Navigate into the crontabs folder and replace the backup paths.

```bash
cd /var/spool/cron/crontabs/
sed -i 's|/var/tmp|/var/sdb/backup|g' root
sed -i 's|/var/backup|/var/sdb/backup|g' root
```

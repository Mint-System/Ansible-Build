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
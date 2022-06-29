# cron role

Setup cron jobs.

## Usage

Configure the role.

**vars.yml**

```yml
cron_jobs:
  - name: Run cron scheduler
    command: curl https://moodle.example.com/admin/cron.php
    hour: "4" # default: '*'
    minute: "1" # default: '*'
```

And include it in your playbook.

```yml
- hosts: cron
  roles:
  - role: cron
```
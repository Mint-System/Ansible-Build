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
  - id: "Run job sync folder"
    command: "script"
    minute: "*/10"
    script_name: hello-world
    script: |
      #!/bin/sh
      echo "hello world"
```

And include it in your playbook.

```yml
- hosts: cron
  roles:
  - role: cron
```
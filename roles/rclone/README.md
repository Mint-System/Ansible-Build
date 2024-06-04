# RClone role

Sync files with RClone.

## Usage

Configure the role.

**vars.yml**

```yml
rclone_sync:
- id: "Run job sync folder"
  command: "copy"
  source_provider: filesystem
  source: /mnt/snas1/publication/
  dest_provider: filesystem
  dest: /usr/share/birt01/reports
  minute: "*/10"
- id: "offsite backup"
  name: "remote"
  command: "copy"
  source_provider: filesystem
  source: /var/tmp/odoo.zip
  dest: remote:/home
  dest_provider: sftp
  host: sftp.example.com
  user: backup
  pass: f669HJNLPJTsG61SVuwrqkKCjmvHRG_3jzJ_pGdmO7B9yBAw # password obscured with rclone
  hour: "3"
```

And include it in your playbook.

```yml
- hosts: rclone
  roles:
  - role: rclone
```

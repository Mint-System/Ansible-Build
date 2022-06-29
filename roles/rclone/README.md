# RClone role

Sync files with RClone.

## Usage

Configure the role.

**vars.yml**

```yml
rclone_sync:
- id: "sync folder"
  command: "copy"
  source_provider: filesystem
  source: /mnt/snas1/publication/
  dest_provider: filesystem
  dest: /usr/share/birt01/reports
  minute: "*/10"
```

And include it in your playbook.

```yml
- hosts: rclone
  roles:
  - role: rclone
```

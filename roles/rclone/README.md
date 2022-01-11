# Ansible RClone role

Sync files with RClone.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/rclone/rclone
rclone_image: rclone:6.2.3
rclone_description: Sync for birt01 # default: RClone
rclone_sync:
- id: "Sync folder"
  type: "copy"
  source_provider: filesystem
  source: "/mnt/snas1/IT/Intranet/Publizierung/"
  dest_provider: filesystem
  dest: /usr/share/birt01/reports
  hourly: 
```

And include it in your playbook.

```yml
- hosts: rclone
  roles:
  - role: rclone
```

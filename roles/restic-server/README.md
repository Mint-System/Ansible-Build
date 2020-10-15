# Ansible Restic server role

Deploy Restic server container.

## Usage

Configure the role.

**vars.yml**

```yml
restic_server_image: restic/rest-server:0.9.7
restic_server_user: restic
restic_server_password: "{{ vault_restic_server_password }}"
restic_server_hostname: restic01
restic_server_backup_dir: /path/to/mount
```

And include it in your playbook.

```yml
- hosts: restic-server
  roles:
  - role: restic-server
```

<img src="/logos/restic_server.png" alt="restic_server logo" width="100" height="100">

# Restic server role

Deploy Restic server container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/restic/rest-server
restic_server_image: restic/rest-server:0.12.1
restic_server_description: "restic server" # default: "Restic Server"
restic_server_requires_package: python2-passlib # default: python3-passlib
restic_server_user: restic-user # default: restic
restic_server_password: # default: "{{ vault_restic_server_password }}"
restic_server_hostname: restic01
restic_server_backup_dir: /path/to/mount
```

And include it in your playbook.

```yml
- hosts: restic_server
  roles:
  - role: restic_server
```

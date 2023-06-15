# Restic server role

Deploy Restic server container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/restic/rest-server
restic_server_image: restic/rest-server:0.10.0
restic_server_description: "restic server" # default: "Restic Server"
restic_server_user: restic-user # default: restic
restic_server_password: "{{ vault_restic_server_password }}"
restic_server_hostname: restic01
restic_server_requires_package: python2-passlib # default: python3-passlib
restic_server_backup_dir: /path/to/mount
restic_server_nginx_data_dir: /usr/share/nginx/proxies # default: "{{ nginx_data_dir }}/proxies"
restic_server_proxy_basic_auth_username: exporter # default: restic-server
restic_server_proxy_basic_auth_password: "{{ vault_restic_server_proxy_basic_auth_password }}"
```

And include it in your playbook.

```yml
- hosts: restic_server
  roles:
  - role: restic_server
```

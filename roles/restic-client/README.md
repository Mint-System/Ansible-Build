# Ansible Restic client role

Deploys Restic client backup job

## Requires

The Ansible Restic client role requires the following roles:

* docker
* docker-network

And actual Docker volumes to backup.

## Usage

Configure the role.

**vars.yml**

```yml
restic_client_package: "restic=0.8.3+ds-1"
restic_client_user: restic
restic_client_password: "{{ vault_restic_client_password }}"
restic_client_backup_repo: restic
restic_client_backup_host: restic01:8080
````

And include it in your playbook.

```yml
- hosts: restic-client
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: restic-client
    tags: restic-client
```
# Ansible Docker Volume role

Configures a Docker volume.

## Usage

Configure the role.

**vars.yml**

```yml
docker_volume_name: example_data01
docker_volume_backup_sets: # See restic_backup_sets var in role restic-client
```

And include it in your playbook.

```yml
- hosts: docker-volume
  roles:
  - role: docker-volume
    tags: docker-volume
```

<img src="/logos/docker_volume.png" alt="docker_volume logo" width="100" height="100">

# Docker Volume role

Configures a Docker volume.

## Usage

Configure the role.

```yml
docker_volume_scripts_dir: /home/odoo-prod/bin # default: /usr/local/bin
docker_volume_name: example_data01
docker_volumes:
  - name: service_data02
  - name: service_data03
docker_volume_backup_set: # See restic_backup_set var in role restic
```

And include it in your playbook.

```yml
- hosts: docker_volume
  roles:
  - role: docker_volume
```

The following tags are available:

* docker_volume
* docker_volume_backup

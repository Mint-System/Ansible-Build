# Docker Volume role

Configures a Docker volume.

## Usage

Configure the role.

**vars.yml**

```yml
docker_volume_name: example_data01
docker_volumes:
  - name: service_data02
  - name: service_data03
docker_volume_backup_set: # See restic_backup_set var in role restic_client
```

And include it in your playbook.

```yml
- hosts: docker_volume
  roles:
  - role: docker_volume
```

## Docs

### Install command line tools

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-build/master/roles/docker_volume/files/install | bash` in your terminal.

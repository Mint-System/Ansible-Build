# Ansible Docker Volume role

Configures a Docker volume.

## Usage

Configure the role.

**vars.yml**

```yml
docker_volume_name: example_data01
docker_volumes:
  - name: service_data02
  - name: service_data03
docker_volume_backup_set: # See restic_backup_set var in role restic-client
```

And include it in your playbook.

```yml
- hosts: docker-volume
  roles:
  - role: docker-volume
```

## Docs

### Install without Ansible

The installation script requires that you have sudo access to root.

Run `curl -L https://raw.githubusercontent.com/mint-system/ansible-playbooks/master/roles/docker-volume/files/install | sh` in your terminal.

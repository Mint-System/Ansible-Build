# Ansible Docker Swarm role

Configures a Docker Swarm.

## Usage

Configure the role.

**vars.yml**

```yml
docker_swarm:
```

And include it in your playbook.

```yml
- hosts: docker-swarm
  roles:
  - role: docker-swarm
```

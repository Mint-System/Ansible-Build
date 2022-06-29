# Docker Swarm role

Configures Docker Swarm.

## Usage

Configure the role.

**vars.yml**

```yml
docker_swarm_enable: true # default: false
```

And include it in your playbook.

```yml
- hosts: docker-swarm
  roles:
  - role: docker-swarm
```

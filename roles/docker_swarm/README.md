# Docker Swarm role

Configures Docker Swarm.

## Usage

Configure the role.

```yml
docker_swarm_enabled: true # default: false
```

And include it in your playbook.

```yml
- hosts: docker_swarm
  roles:
  - role: docker_swarm
```

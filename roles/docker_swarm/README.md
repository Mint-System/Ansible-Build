<img src="/logos/docker_swarm.png" alt="docker_swarm logo" width="100" height="100">

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

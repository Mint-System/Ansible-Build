# Docker Network role

Configures a Docker network.

## Usage

Configure the role.

**vars.yml**

```yml
docker_network_name: example.com
docker_network_driver: overlay # defaults: bridge
```

And include it in your playbook.

```yml
- hosts: docker_network
  roles:
  - role: docker_network
```
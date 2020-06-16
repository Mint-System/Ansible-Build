# Ansible Docker Network role

Configures a Docker network.

## Usage

Configure the role.

**vars.yml**

```yml
docker_network_name: example.com
```

And include it in your playbook.

```yml
- hosts: docker-network
  roles:
  - role: docker-network
    tags: docker-network
```
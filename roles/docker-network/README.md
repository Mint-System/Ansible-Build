# Ansible Docker Network role

Configures a Docker network.

## Requires

The Ansible Docker Network role requires the following roles:

* docker

## Usage

Configure the role.

**vars.yml**

```yml
network_name: example-net
````

And include it in your playbook.

```yml
- hosts: docker
  roles:
  - { role: docker, tags: ["docker"] }
  - { role: docker-network, tags: ["docker-network"] }
```
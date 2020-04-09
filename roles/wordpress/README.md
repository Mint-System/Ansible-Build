# Ansible WordPress role

Deploys WordPress container.

## Requires

The Ansible WordPress role requires the following roles:

* docker
* docker-network
* mysql

## Usage

Configure the role.

**vars.yml**

```yml

```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: mysql
    tags: mysql
  - role: wordpress
    tags: wordpress
```

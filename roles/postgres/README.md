# Ansible PostgreSQL role

Deploys PostgreSQL database container

## Requires

The Ansible PostgreSQL role requires the following roles:

* docker
* docker-network

## Usage

Configure the role.

**vars.yml**

```yml
postgres_image: postgres:10-alpine
postgres_hostname: postgres01
postgres_port_exposed: 5432
postgres_data_dir: /usr/share/postgres01
postgres_user: example
postgres_password: "{{ vault_postgres_password }}"
postgres_db: example
````

And include it in your playbook.

```yml
- hosts: postgres
  roles:
  - { role: docker, tags: ["docker"] }
  - { role: docker-network, tags: ["docker-network"] }
  - { role: postgres, tags: ["postgres"] }
```
# Ansible Keycloack role

Deploys Keycloack container.

## Requires

The Ansible Keycloack role requires the following roles:

* docker
* docker-network
* postgres

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/jboss/keycloak
keycloack_image: jboss/keycloak:9.0.2
keycloack_hostname: login01
keycloack_user: admin
keycloack_password: "{{ vault_keycloack_password }}"
keycloack_db_hostname: postgres01
keycloack_db_user: keycloack
keycloack_db_password: "{{ vault_keycloack_db_password }}"
```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: postgres
    tags: postgres
  - role: keycloack
    tags: keycloack
```

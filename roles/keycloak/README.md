# Ansible Keycloak role

Deploys Keycloak container.

## Requires

The Ansible Keycloak role requires the following roles:

* docker
* docker-network
* postgres

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/jboss/keycloak
keycloak_image: jboss/keycloak:9.0.2
keycloak_hostname: login01
keycloak_user: admin
keycloak_password: "{{ vault_keycloak_password }}"
keycloak_db_type: postgres
keycloak_db_hostname: postgres01
keycloak_db_user: keycloak
keycloak_db_password: "{{ vault_keycloak_db_password }}"
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
  - role: keycloak
    tags: keycloak
```

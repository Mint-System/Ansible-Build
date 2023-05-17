# Keycloak role

Deploy Keycloak container.

## Usage

Configure the role.

**vars.yml**

Up to version 17.0 use:

```yml
# https://hub.docker.com/r/jboss/keycloak
keycloak_image: jboss/keycloak:9.0.2
keycloak_description: Login Example Company # default: Keycloak
keycloak_timezone: Europe/Paris # default: Europe/Berlin
keycloak_hostname: login01
keycloak_user: admin
keycloak_password: # default: "{{ vault_keycloak_password }}"
keycloak_db_type: mariadb # default: postgres
keycloak_db_hostname: postgres01
keycloak_db_user: keycloak
keycloak_db_password: # default: "{{ vault_keycloak_db_password }}"
```

From version 17.0 use:

```yml
# https://quay.io/repository/keycloak/keycloak
keycloak_image: quay.io/keycloak/keycloak:21.1
keycloak_description: Login Example Company # default: Keycloak
keycloak_hostname: login02
keycloak_admin: admin
keycloak_admin_password: # default: "{{ vault_keycloak_admin_password }}"
keycloak_db: mariadb # default: postgres
keycloak_db_url_host: postgres01
keycloak_db_url_database: keycloak
keycloak_db_username: keycloak
keycloak_db_password: # default: "{{ vault_keycloak_db_password }}"
keycloak_proxy_hostname: login.example.com
```

And include it in your playbook.

```yml
- hosts: keycloak
  roles:
  - role: keycloak
```

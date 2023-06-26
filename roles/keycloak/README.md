# Keycloak role

Deploy Keycloak container.

## Usage

Configure the role.

**vars.yml**

Up to version 17.0 use:

```yml
# https://hub.docker.com/r/jboss/keycloak
keycloak_image: jboss/keycloak:9.0.2
keycloak_build_image: true # default: false
keycloak_hostname: login01
keycloak_description: Login Example Company # default: Keycloak
keycloak_timezone: Europe/Paris # default: Europe/Berlin
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
keycloak_build_image: true # default: false
keycloak_hostname: login02
keycloak_description: Login Example Company # default: Keycloak
keycloak_data_dir: /usr/share/keycloak # default: "/usr/share/{{ keycloak_hostname }}"
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

## Docs

### Additonal Hash-Providers

The custom image supports the hash providers Argon and Bcrypt. This might be helpful when migrating user credentials from another idp.

To test the providers you can run the following SQL statemens. Replace the `user_id` when doing so.

**Argon**

```sql
UPDATE credential SET credential_data='{"algorithm":"argon"}', secret_data='{"value":"$argon2i$v=19$m=65536,t=16,p=1$bnI2SEl3UXNicmovRTZYdg$MeU+vEnpIQb1q1QiWNiIq70K8hoWWb3gbp1CfqH6jAU"}'
WHERE user_id='dc6eec6c-7aea-456c-bf6d-007f4a5b6b07';
```

**Bcrypt**


```sql
UPDATE credential SET credential_data='{"algorithm":"bcrypt"}', secret_data='{"value":"$2y$12$xtQ/70RpLO8pzGQjYjzsmuJ.eFBAFmizDotdHUBKd9.y755qj/OWu"}'
WHERE user_id='dc6eec6c-7aea-456c-bf6d-007f4a5b6b07';
```

In the both cases the actual password is `sozialinfo`.
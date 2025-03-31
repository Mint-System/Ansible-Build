# Keycloak role

Deploy Keycloak container.

## Usage

Configure the role.

```yml
# https://quay.io/repository/keycloak/keycloak
keycloak_image: quay.io/keycloak/keycloak:22.0
keycloak_build_image: true # default: false
keycloak_build_include: # default: []
  - url: https://github.com/inventage/keycloak-password-hashprovider-extension/releases/download/2.0.0/extension-password-hashprovider-2.0.0-202307200659-6-d59b2187.jar
    dest: /opt/keycloak/providers/hashprovider-extension.jar
  - url: https://repo1.maven.org/maven2/org/springframework/security/spring-security-crypto/6.1.3/spring-security-crypto-6.1.3.jar
    dest: /opt/keycloak/providers/spring-security-crypto.jar
keycloak_hostname: login01
keycloak_description: Login Example Company # default: Keycloak
keycloak_state: stopped # default: started
keycloak_data_dir: /usr/share/keycloak # default: "/usr/share/{{ keycloak_hostname }}"
keycloak_admin: admin
keycloak_admin_password: # default: "{{ vault_keycloak_admin_password }}"
keycloak_db: mariadb # default: postgres
keycloak_db_url_host: postgres01
keycloak_db_url_database: kc # default: keycloak
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

### Use Admin CLI in Container

You can use the `kcadm.sh` cli inside a Docker container to manage the Keycloak instance.

Log into a Kecyloak container.

```bash
docker exec -w /opt/keycloak/bin -it login01 bash
```

Log into the realm with a Keycloak user.

```bash
./kcadm.sh config credentials --server https://login.example.com --realm master --user $USERNAME --password $PASSWORD
```

Run `kcadm.sh` commands.

```bash
./kcadm.sh get clients -r master --fields id,clientId
./kcadm.sh create clear-user-cache -r master -s realm=master
```

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

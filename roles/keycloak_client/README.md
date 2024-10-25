# Keycloak Client role

Configure Keycloak client.

## Usage

Configure the role.

```yml
# https://docs.ansible.com/ansible/latest/collections/community/general/keycloak_client_module.html
keycloak_clients:
  - auth_client_id: admin-cli # default: admin-cli
    auth_keycloak_url: https://login.example.com/auth/
    auth_realm: master # default: master
    auth_username: login@example.com
    auth_password: "{{ vault_keycloakd_client_0_auth_password }}"
    state: present # default: present
    realm: my-realm.com
    client_id: odoo.example.com
    name: Odoo OAuth Client
    description: Default client for Odoo instances
    enabled: False # default: True
    protocol: openid-connect # default: openid-connect
    client_authenticator_type: client-secret # default: client-secret
    standard_flow_enabled: True # default: True
    implicit_flow_enabled: False # default: False
    direct_access_grants_enabled: False # default: False
    root_url: "${authBaseUrl}"
    redirect_uris:
      - https://erp.example.com/*
    base_url: /realms/my-realm.com/account/
    full_scope_allowed: True # default: False
```

And include it in your playbook.

```yml
- hosts: keycloak_client
  roles:
  - role: keycloak_client
```

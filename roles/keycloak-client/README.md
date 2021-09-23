# Ansible Keycloak Client role

Configure Keycloak client.

## Usage

Configure the role.

**vars.yml**

```yml
# https://docs.ansible.com/ansible/latest/collections/community/general/keycloak_client_module.html
keycloak_clients:
  - auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com/auth
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    state: present
    realm: master
    client_id: test
    id: d8b127a3-31f6-44c8-a7e4-4ab9a3e78d95
    name: this_is_a_test
    description: Description of this wonderful client
    root_url: https://www.example.com/
    admin_url: https://www.example.com/admin_url
    base_url: basepath
    enabled: True
    client_authenticator_type: client-secret
    secret: REALLYWELLKEPTSECRET
    redirect_uris:
      - https://www.example.com/*
      - http://localhost:8888/
    web_origins:
      - https://www.example.com/*
    
```

And include it in your playbook.

```yml
- hosts: keycloak-client
  roles:
  - role: keycloak-client
```

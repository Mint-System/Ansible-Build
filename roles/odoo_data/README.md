# Odoo Data role

Generate Odoo data modules.

## Usage

Configure the role.

```yml
odoo_data_dir: /usr/share/odoo # default: "/usr/share/{{ odoo_hostname }}"
odoo_data:
  - id: ir_mail_server_1
    module_name: ir_mail_server_data
    display_name: "Mail Server Example"
    model: ir.mail_server
    fields:
      name: Infomaniak Outgoing
      smtp_host: mail.infomaniak.com
      smtp_port: 587
      smtp_encryption: starttls
      smtp_user: odoo@example.com
      smtp_pass: "{{ vault_odoo_data_smtp_pass }}"
      enabled:
        type: eval
        value: "True"
  - id: provider_mint_system
    module_name: auth_oauth_provider_data
    display_name: "Login Mint System"
    model: auth.oauth.provider
    depends: auth_oauth_keycloak
    fields:
      name: Login Mint System
      body: Login Mint System
      client_id: odoo.mint-system.ch
      enabled:
        type: eval
        value: "True"
      css_class: fa fa-fw fa-sign-in text-primary
      auth_endpoint: https://login.mint-system.ch/realms/mint-system.ch/protocol/openid-connect/auth
      scope: profile
      validation_endpoint: https://login.mint-system.ch/realms/mint-system.ch/protocol/openid-connect/userinfo
```

Include the role in your playbook.

```yml
- hosts: odoo
  roles:
  - role: odoo_data
```
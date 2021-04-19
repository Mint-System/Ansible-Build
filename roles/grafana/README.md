# Ansible Grafana role

Deploy Grafana container.

## Usage

Configure the role.

**vars.yml**

```yml
grafana_image: grafana/grafana:6.7.1
grafana_hostname: graf01
grafana_description: Prometheus dashboard # default: Grafana
grafana_data_dir: /usr/share/graf # default: "/usr/share/{{ grafana_hostname }}"
grafana_volume_name: grafana_data01
grafana_admin_user: admin
grafana_admin_password: "{{ vault_grafana_admin_password }}"
grafana_prometheus_hostname: prom01
grafana_mail_hostname: mail.example.com:587
grafana_mail_from: noreply@example.com
grafana_mail_from_name: Grafana
grafana_mail_username: bot@example.com
grafana_mail_password: "{{ vault_grafana_mail_password }}"
grafana_server_domain: "monitor.example.com"
grafana_server_root_url: "https://monitor.example.com"
grafana_generic_oauth_enabled: "true"
grafana_generic_oauth_name: "Login Example"
grafana_generic_oauth_sign_up: "true"
grafana_generic_oauth_client_id: "monitor.example.com"
grafana_generic_oauth_client_secret: "{{ vault_grafana_generic_oauth_client_secret }}"
grafana_generic_oauth_scopes: email # default: profile
grafana_generic_oauth_auth_url: "https://login.example.com/auth/realms/example.com/protocol/openid-connect/auth"
grafana_generic_oauth_token_url: "https://login.example.com/auth/realms/example.com/protocol/openid-connect/token"
grafana_generic_oauth_api_url: "https://login.example.com/auth/realms/example.com/protocol/openid-connect/userinfo"
```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: grafana
```

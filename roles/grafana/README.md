# Ansible Grafana role

Deploys Grafana container.

## Usage

Configure the role.

**vars.yml**

```yml
grafana_image: grafana/grafana:6.7.1
grafana_hostname: graf01
grafana_data_dir: /usr/share/graf01
grafana_volume_name: grafana_data01
grafana_admin_user: admin
grafana_admin_password: "{{ vault_grafana_admin_password }}"
grafana_prometheus_hostname: prom01
grafana_mail_hostname: mail.example.com:587
grafana_mail_from: noreply@example.com
grafana_mail_from_name: Grafana
grafana_mail_username: bot@example.com
grafana_mail_password: "{{ vault_grafana_mail_password }}"
```

And include it in your playbook.

```yml
- hosts: prometheus
  roles:
  - role: grafana
    tags: grafana
```

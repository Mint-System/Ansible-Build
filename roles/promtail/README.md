# Promtail role

Deploy Promtail container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/grafana/promtail/
promtail_image: grafana/promtail:2.3.0
promtail_hostname: promtail01
promtail_description: forwad logs to loki # default: Promtail
promtail_data_dir: /usr/share/promtail # default: "/usr/share/{{ promtail_hostname }}"
promtail_push_url: loki.example.com/loki/api/v1/push
promtail_loki_basic_auth_username: log # default: loki
promtail_loki_basic_auth_password: "{{ vault_promtail_loki_basic_auth_password }}"
```

And include it in your playbook.

```yml
- hosts: promtail
  roles:
  - role: promtail
```

<img src="/logos/ufw.png" alt="ufw logo" width="100" height="100">

# UFW role

Configures UFW rules.

## Usage

Configure the role.

```yml
ufw_enabled: true # default false
host_ufw_rules_sets:
  custom:
    - rule: allow
      port: "46022"
      proto: tcp
ufw_active_rules:
  - bigbluebutton # default: default
  - custom
```

And include it in your playbook.

```yml
- hosts: ufw
  roles:
  - role: ufw
```

## Docs

### Disable or enable ufw manually

Enable ufw manually.

```bash
ufw enable
```

Disable ufw manually.

```bash
ufw disable
```
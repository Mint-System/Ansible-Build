<img src="/logos/ufw.png" alt="ufw logo" width="100" height="100">

# UFW role

Configures UFW rules.

## Usage

Configure the role.

```yml
ufw_enabled: true # default false
ufw_active_rules:
  - bigbluebutton # default: default
```

And include it in your playbook.

```yml
- hosts: ufw
  roles:
  - role: ufw
```

## Docs

Enable ufw manually.\
`ufw enable`

Disable ufw manually.\
`ufw disable`
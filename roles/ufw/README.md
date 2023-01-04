# UFW role

Configures UFW rules.

## Usage

Configure the role.

**vars.yml**

```yml
ufw_enabled: true # default false
ufw_profiles:
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
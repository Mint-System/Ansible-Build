# Ansible UFW role

Configures UFW rules.

## Usage

Configure the role.

**vars.yml**

```yml
ufw_state: enabled
ufw_profile: bigbluebutton # default: default
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
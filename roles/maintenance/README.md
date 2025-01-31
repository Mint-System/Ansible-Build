# Maintenance role

Maintains operating system and disk space.

## Usage

Configure the role.

```yml
maintenance: true # default: false
maintenance_job: true # default: false
```

And include it in your playbook.

```yml
- hosts: maintenance
  roles:
  - role: maintenance
```

# Maintenance role

Maintains operating system and disk space.

## Usage

Configure the role.

```yml
maintenance: true
maintenance_job: true
```

And include it in your playbook.

```yml
- hosts: maintenance
  roles:
  - role: maintenance
```

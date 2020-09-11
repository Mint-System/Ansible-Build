# Ansible Maintenance role

Maintains operating system and disk space.

## Usage

Configure the role.

**vars.yml**

```yml
maintenance: true
```

And include it in your playbook.

```yml
- hosts: maintenance
  roles:
  - role: maintenance
```

# Ansible WordPress role

Deploys WordPress container.

## Usage

Configure the role.

**vars.yml**

```yml

```

And include it in your playbook.

```yml
- hosts: wordpress
  roles:
  - role: wordpress
    tags: wordpress
```

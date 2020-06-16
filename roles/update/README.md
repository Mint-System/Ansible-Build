# Ansible Update role

Install system and package updates.

## Requires

The Ansible Update role supports os of type:

* ubuntu1604
* ubuntu1804

## Usage

Configure the role.

**vars.yml**

```yml
update: true
```

And include it in your playbook.

```yml
- hosts: update
  roles:
  - role: update
    tags: update
```

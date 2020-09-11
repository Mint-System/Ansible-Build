# Ansible Update role

Install system and package updates.

## Requires

The Ansible Update role supports os of type:

* Ubuntu 
* CentOS
* SLES 

## Usage

Configure the role.

**vars.yml**

```yml
update: true
reboot_allowed: true
```

And include it in your playbook.

```yml
- hosts: update
  roles:
  - role: update
```

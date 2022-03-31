# Ansible Update role

Install system and package updates.

## Requires

The Ansible Update role supports these package managers:

* apt (Debian, Ubuntu) 
* yum (CentOS, RHEL)
* zypper (SLES, OpenSUSE) 

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

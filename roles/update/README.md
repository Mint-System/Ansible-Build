<img src="/logos/update.png" alt="update logo" width="100" height="100">

# Update role

Install system and package updates.

The Ansible Update role supports these package managers:

* apt
* yum
* zypper
* dnf

## Usage

Configure the role.

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

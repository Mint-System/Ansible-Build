<img src="/logos/motd.png" alt="motd logo" width="100" height="100">

# motd role

Set message of the day.

## Usage

Configure the role.

```yml
motd_enabled: false # default: true
all:
  hosts:
    server:
      ansible_host: server.example.com
      function: Odoo
      customer: Your Company
      hosting_provider: On-Premise
```

And include it in your playbook.

```yml
- hosts: motd
  roles:
  - role: motd
```

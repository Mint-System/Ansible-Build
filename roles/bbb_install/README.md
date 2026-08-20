---
kind: application
---

<img src="/logos/bbb_install.png" alt="bbb_install logo" width="100" height="100">

# bbb_install role

Runs the bbb-install script.

## Usage

Configure the role.

```yml
# https://docs.bigbluebutton.org/administration/install/#install
bbb_install_hostname: bbb.example.com
bbb_install_certbot_email: info@example.com
```

And include it in your playbook.

```yml
- hosts: bbb_install
  roles:
  - role: bbb_install
```

---
kind: application
---

<img src="/logos/bigbluebutton.png" alt="bigbluebutton logo" width="100" height="100">

# BigBlueButton role

Runs the bbb-install script.

## Usage

Configure the role.

```yml
# https://docs.bigbluebutton.org/administration/install/#install
bigbluebutton_hostname: bbb.example.com
bigbluebutton_certbot_email: info@example.com
```

And include it in your playbook.

```yml
- hosts: bigbluebutton
  roles:
  - role: bigbluebutton
```

<img src="/logos/simple_mail_forwarder.png" alt="simple_mail_forwarder logo" width="100" height="100">

# Simple Mail Forwarder role

Deploy Simple Mail Forwarder container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/zixia/simple-mail-forwarder
simple_mail_forwarder_image: zixia/simple-mail-forwarder:1.4
simple_mail_forwarder_description: Redirect all incoming mails # default: Simple Mail Forwarder
simple_mail_forwarder_hostname: smf01
simple_mail_forwarder_config: 'test@example.com:test@test.com'
```

And include it in your playbook.

```yml
- hosts: simple_mail_forwarder
  roles:
  - role: simple_mail_forwarder
```

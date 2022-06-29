# Simple Mail Forwarder role

Deploy Simple Mail Forwarder container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/zixia/simple-mail-forwarder
simple_mail_forwarder_image: zixia/simple-mail-forwarder:1.4
simple_mail_forwarder_description: Redirect all incoming mails # default: Simple Mail Forwarder
simple_mail_forwarder_hostname: smf01
simple_mail_forwarder_config: 'test@example.com:test@test.com'
```

And include it in your playbook.

```yml
- hosts: simple-mail-forwarder
  roles:
  - role: simple-mail-forwarder
```

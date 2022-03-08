# Ansible Postfix role

Deploy Postfix relay host.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/boky/postfix
postfix_image: boky/postfix:v3.4.0-alpine
postfix_description: Redirect all incoming mails # default: Postfix
postfix_hostname: postfix01
postfix_ports:
  - 587:587 # default: 127.0.0.1:1587:587
postfix_data_dir: /usr/share/postfix # default: "/usr/share/{{ postfix_hostname }}"
postfix_allowed_sender_domains: 'example.com'
```

And include it in your playbook.

```yml
- hosts: postfix
  roles:
  - role: postfix
```

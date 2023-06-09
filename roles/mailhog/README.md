# MailHog role

Deploy MailHog container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://registry.hub.docker.com/r/mailhog/mailhog/
mailhog_image: mailhog/mailhog:latest
mailhog_description: MailDev # default: MailHog
mailhog_hostname: mailhog01
```

And include it in your playbook.

```yml
- hosts: mailhog
  roles:
  - role: mailhog
```

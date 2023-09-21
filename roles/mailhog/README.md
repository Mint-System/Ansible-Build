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
mailhog_data_dir: /usr/share/mailhog_data01 # default: "/usr/share/{{ mailhog_hostname }}"
mailhoq_web_path: mailhog # default: ""
mailhog_users:
  - username: admin
    password: "{{ vault_mailhog_user_admin_password }}"
```

And include it in your playbook.

```yml
- hosts: mailhog
  roles:
  - role: mailhog
```

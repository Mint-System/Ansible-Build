# Ansible BookStack role

Deploys BookStack Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
bookstack_image: solidnerd/bookstack:0.27.5
bookstack_hostname: book01
bookstack_data_dir: /usr/share/bookstack01
bookstack_app_url: "https://wiki.example.com"
bookstack_db_hostname: mysql01
bookstack_db_user: bookstack
bookstack_db_password: "{{ vault_mysql_password }}"
bookstack_db_name: bookstack
bookstack_mail_driver: smtp
bookstack_mail_hostname: mail.example.com
bookstack_mail_port: "587"
bookstack_mail_from: noreply@mexample.com
bookstack_mail_username: bot@example.com
bookstack_mail_password: "{{ vault_bookstack_mail_password }}"
bookstack_mail_encryption: tls
```

And include it in your playbook.

```yml
- hosts: bookstack
  roles:
  - role: bookstack
    tags: bookstack
```
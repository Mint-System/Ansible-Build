# Ansible WordPress role

Deploys WordPress container.

## Usage

Configure the role.

**vars.yml**

```yml
wordpress_image: wordpress:php7.4-apache
wordpress_hostname: word01
wordpress_volume_name: word_data01
wordpress_db_hostname: mysql01
wordpress_db_user: wordpress
wordpress_db_password: "{{ vault_wordpress_db_password }}"
wordpress_db_name: wordpress
wordpress_smtp_secure: tls
wordpress_smtp_hostname: mail.example.com
wordpress_smtp_port: "587"
wordpress_smtp_from: noreply@example.com
wordpress_smtp_username: bot@example.com
wordpress_smtp_password: "{{ vault_wordpress_smtp_password }}"
```

And include it in your playbook.

```yml
- hosts: wordpress
  roles:
  - role: wordpress
    tags: wordpress
```

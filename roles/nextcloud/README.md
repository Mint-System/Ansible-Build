# Ansible Nextcloud role

Deploys Nextcloud Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/nextcloud/
nextcloud_image: nextcloud:18-apache
nextcloud_hostname: nextcloud01
nextcloud_volume_name: nextcloud_data01
nextcloud_trusted_domains: nextcloud.example.com
nextcloud_admin_user: admin
nextcloud_admin_password: "{{ vault_nextcloud_admin_password }}"
nextcloud_postgres_hostname: postgres01
nextcloud_postgres_user: nextcloud
nextcloud_postgres_password: "{{ vault_postgres_password }}"
nextcloud_postgres_db: nextcloud
nextcloud_mail_hostname: mail.example.com
nextcloud_mail_encryption: tls
nextcloud_mail_port: "587"
nextcloud_mail_from: noreply@example.com
nextcloud_mail_username: bot@example.com
nextcloud_mail_password: "{{ vault_nextcloud_mail_password }}"
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: nextcloud
    tags: nextcloud
```

# Ansible Remark42 role

Deploy Remark42 container

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/umputun/remark42
remark42_image: umputun/remark42:latest
remark42_description: Comments for website  # default: Remark42
remark42_volume_name: remark_data01
remark42_hostname: remark01
remark42_url: comment.example.com
remark42_secret: "{{ vault_remark42_secret }}"
remark42_site: "blog.example.com"
remark42_auth_anonymous: "true" # default: false
remark42_auth_email_enable: "true" # default: false
remark42_auth_email_from: "noreply@example.com"
remark42_auth_github_key: ""
remark42_auth_github_secret: "{{ vault_remark42_github_secret }}"
remark42_smtp_host: mail.example.com
remark42_smtp_port: "587"
remark42_smtp_username: bot@example.com
remark42_smtp_password: "{{ vault_remark42_smtp_password }}"
remark42_volume_backup_sets: # See restic_backup_sets var in role restic-client
```

And include it in your playbook.

```yml
- hosts: remark42
  roles:
  - role: remark42
```

# Ansible Commento role

Deploy Commento container

## Usage

Configure the role.

**vars.yml**

```yml
# https://docs.commento.io/installation/self-hosting/on-your-server/docker.html
commento_image: registry.gitlab.com/commento/commento
commento_description: Comments for website  # default: Commento
commento_hostname: commento01
commento_host: comment.example.com
commento_deny_signups: "true" # default: "false"
commento_db_hostname: postgres01
commento_db_user: commento
commento_db_password: "{{ vault_commento_db_password }}"
commento_smtp_host: mail.example.com
commento_smtp_port: "587"
commento_smtp_from: noreply@example.com
commento_smtp_username: bot@example.com
commento_smtp_password: "{{ vault_commento_smtp_password }}"
commento_github_key: ""
commento_github_secret: "{{ vault_commento_github_secret }}"
```

And include it in your playbook.

```yml
- hosts: commento
  roles:
  - role: commento
```

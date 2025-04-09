<img src="/logos/gitea.png" alt="gitea logo" width="100" height="100">

# Gitea role

Deploy Gitea container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/gitea/gitea/
gitea_image: gitea/gitea:1.22.1
gitea_description: Git Server # default: Gitea
gitea_hostname: git01
odoo_ports:
 - "2222:22" # default: "222:22"
gitea_volume_name: git01_data # default: "{{ gitea_hostname }}"
gitea_user: svn # default: git
gitea_root_url: https://git.example.com
gitea_postgres_hostname: postgres01
gitea_postgres_database: git # default: gitea
gitea_postgres_user: git # default: gitea
gitea_postgres_password: # default: "{{ vault_gitea_postgres_password }}"
gitea_volume_backup_set: # See restic_backup_set var in role restic
gitea_disable_registration: "true" # default: "false"
```

And include it in your playbook.

```yml
- hosts: gitea
  roles:
  - role: gitea
```

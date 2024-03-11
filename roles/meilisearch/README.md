# Mmeilisearch role

Deploy Meilisearch container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/getmeili/meilisearch
meilisearch_image: meilisearch:v1.6.2
meilisearch_build_image: true # default: false
meilisearch_hostname: msrch01
meilisearch_description: Meilisearch # default: meilisearch
meilisearch_state: started
meilisearch_enabled_at_boot: 'true'

meilisearch_user: 'meilisearch'
meilisearch_group: 'meilisearch'

meilisearch_exe_path: '/usr/bin/meilisearch'
meilisearch_db_path: '/var/lib/meilisearch'
meilisearch_listen_ip: 127.0.0.1
meilisearch_listen_port: 7700
meilisearch_master_key: # default: "{{ vault_meilisearch_master_key }}


```

And include it in your playbook.

```yml
- hosts: meilisearch
  roles:
  - role: meilisearch
```

# Meilisearch role

Deploy Meilisearch container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/getmeili/meilisearch
meilisearch_image: getmeili/meilisearch:v1.10.1
meilisearch_hostname: meili01
meilisearch_volume_name: meili01_data # default: "{{ meilisearch_hostname }}"
meilisearch_description: "Meilisearch" # default: "meilisearch"
meilisearch_master_key: # default: "{{ vault_meilisearch_master_key }}
meilisearch_ports:
  - 127.0.0.1:7700:7700 # default: []
```

And include it in your playbook.

```yml
- hosts: meilisearch
  roles:
  - role: meilisearch
```

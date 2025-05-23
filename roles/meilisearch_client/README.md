<img src="/logos/meilisearch_client.png" alt="meilisearch_client logo" width="100" height="100">

# Meilisearch Client role

Configure Meilisearch api keys and indexes.

## Usage

Configure the role.

```yml
meilisearch_url: http://meili01:7700
meilisearch_master_key: # default: "{{ vault_meilisearch_master_key }}
meilisearch_base_path: # default: "{{ inventory_dir}}/host_vars/{{ inventory_hostname }}"
meilisearch_api_keys:
  - path: api_keys/odoo.json
meilisearch_indexes:
  - path: indexes/res_city_state.json
```

And include it in your playbook.

```yml
- hosts: meilisearch_client
  roles:
  - role: meilisearch_client
```

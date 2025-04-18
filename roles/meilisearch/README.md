<img src="/logos/meilisearch.png" alt="meilisearch logo" width="100" height="100">

# Meilisearch role

Deploy Meilisearch container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/getmeili/meilisearch
meilisearch_image: getmeili/meilisearch:v1.10.1
meilisearch_hostname: meili01
meilisearch_volume_name: meili01_data # default: "{{ meilisearch_hostname }}"
meilisearch_description: "Meilisearch" # default: "meilisearch"
meilisearch_master_key: # default: "{{ vault_meilisearch_master_key }}
meilisearch_ports:
  - 127.0.0.1:7700:7700 # default: []
meilisearch_network_mode: host # default: "{{ docker_network_name }}"
meilisearch_etc_hosts: # defaults: {}
  "server.example.com": 10.42.5.2
  "host.docker.internal": host-gateway
meilisearch_task_webhook: http://host.docker.internal:8069/meilisearch/task-webhook # default: ""
```

And include it in your playbook.

```yml
- hosts: meilisearch
  roles:
  - role: meilisearch
```

## Docs

### Test Webhook

Run the curl command to post a succeeded status for task with uid `4`:

```bash
curl \
  -X POST 'http://localhost:8069/meilisearch/task-webhook' \
  -H 'Content-Type: application/json' \
  --data-binary '{"uid":2105,"indexUid":"legal_advice_legal_domain","status":"succeeded","type":"documentAdditionOrUpdate"}'
```
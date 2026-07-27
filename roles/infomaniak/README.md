---
kind: system
---

<img src="/logos/infomaniak.png" alt="infomaniak logo" width="100" height="100">

# Infomaniak role

Manage Infomaniak domain and dns entries.

## Usage

Configure the role.

```yml
infomaniak_token: # default: "{{ vault_infomaniak_token }}"
infomaniak_zones:
  - zone: example.com
    records:
      - { source: '*.exo', type: A, target: 172.30.249.152, state: present }
      - { source: mail, type: MX, target: mxa.eu.mailgun.org, state: present }
```

And include it in your playbook.

```yml
- hosts: infomaniak
  roles:
  - role: infomaniak
```

## Docs

### Set priority

For MX records, `priority` defaults to `10` and is embedded into the `target` sent to the API.

### Update manually

You can also update the DNS records manually with curl. Here is an exapmle to update an MX record:

```bash
INFOMANIAK_TOKEN=*****
ZONE=example.org

# List records of zone
curl -s "https://api.infomaniak.com/2/zones/$ZONE/records" \
  -H "Authorization: Bearer $INFOMANIAK_TOKEN" | python3 -m json.tool

RECORD_ID=31252318

# Update target record
curl -X PUT "https://api.infomaniak.com/2/zones/$ZONE/records/$RECORD_ID" \
  -H 'Authorization: Bearer '"$INFOMANIAK_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"type":"MX","source":"mail","target":"10 mxa.eu.mailgun.org", "ttl":3600}'
```
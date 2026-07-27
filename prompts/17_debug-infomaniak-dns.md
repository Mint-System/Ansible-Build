---
title: "Debug Infomaniak DNS"
state: completed
model: infomaniak/moonshotai/Kimi-K2.6
input_tokens:
---

# Run 17

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

My task `/roles/infomaniak/tasks/infomaniak_dns.yml` fails:

```bash
[main][~/Ansible-Build]$ task play -i inventories/setup plays/localhost.yml -t infomaniak

PLAY [Localhost setup]

TASK [Gathering Facts]

TASK [infomaniak : Include infomaniak dns tasks]
included: /home/janikvonrotz/Ansible-Build/roles/infomaniak/tasks/infomaniak_zone.yml for localhost

TASK [infomaniak : Get existing DNS records for each zone]
TASK [infomaniak : Process DNS records for each zone]

TASK [infomaniak : Set infomaniak DNS present fact for uri-cloud.ch] 

TASK [infomaniak : Show DNS present list for uri-cloud.ch] 

TASK [infomaniak : Update existing DNS records for uri-cloud.ch] **********************************************************************************************************************************************************************************************
ok: [localhost] => (item=mail (TXT))
ok: [localhost] => (item=s1._domainkey.mail (TXT))
failed: [localhost] (item=mail (MX)) => changed=false
  ansible_loop_var: record
  cache_control: no-cache, private
  connection: close
  content: '{"result":"error","error":{"code":"invalid_dns_record","description":"invalid dns record: MX"}}'
  content_length: '95'
  content_type: application/json
  date: Mon, 27 Jul 2026 07:52:14 GMT
  elapsed: 0
  json:
    error:
      code: invalid_dns_record
      description: 'invalid dns record: MX'
    result: error
  msg: 'Status code was 400 and not [200, 201]: HTTP Error 400: Bad Request'
  record:
    source: mail
    state: present
    target: mxa.eu.mailgun.org
    type: MX
  redirected: false
  status: 400
  strict_transport_security: max-age=600; includeSubDomains;
  url: https://api.infomaniak.com/2/zones/uri-cloud.ch/records/31252318
  vary: Origin
  x_overall_time: '0'
  x_query_time: '12.36'
  x_request_id: 4767e644-4453-42e1-9a0a-8588fd7b903a

PLAY RECAP ****************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=11   changed=0    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0
```

Can you help me debug the issue? I captured this curl request in the browser.

```bash
curl 'https://manager.infomaniak.com/v3/api/proxypass_2/1/domain/1793537/dns/record/31252372' \
  -H 'Referer: https://manager.infomaniak.com/v3/317103/ng/domain/1793537/dns/manage-zone/31252372/edit' \
  --data-raw '{"type":"MX","source":"mail","target":"mxa.eu.mailgun.org","priority":10,"ttl":3600}'
```

According to the doc the MX is a valid type: https://developer.infomaniak.com/docs/api/put/2/zones/%7Bzone%7D/records/%7Brecord%7D

My assumption is that `priority` is required and missing.

## Worklog

**Initial investigation** suggested adding a separate `priority` JSON field. However, further testing revealed the v2 API does not accept a separate field and returned a different error once the body format was adjusted:

```bash
failed: [localhost] (item=mail (MX)) => changed=false
  content: '{"result":"error","error":{"code":"cannot_update_object","description":"Cannot update object"}}'
  msg: 'Status code was 500 and not [200, 201]: HTTP Error 500: Internal Server Error'
  record:
    source: mail
    state: present
    target: 10 mxb.eu.mailgun.org
    type: MX
  url: https://api.infomaniak.com/2/zones/uri-cloud.ch/records/31252318
```

**Root cause**:
1. The Infomaniak v2 API (`api.infomaniak.com/2/zones/...`) stores MX record priority **inside the target string** (e.g., `"10 mxa.eu.mailgun.org"`). It does NOT accept a separate `priority` JSON field (the browser-captured curl used the internal Manager API which does).
2. The Ansible logic matched existing records by `source + type` only and always selected `_matched_list[0]`. Because the zone has two `mail MX` records (`mxa` and `mxb`), the role tried to update the `mxa` record ID (`31252318`) with the `mxb` target, causing the API to return HTTP 500 `Cannot update object`.

**Changes**:
- Updated `roles/infomaniak/tasks/infomaniak_dns.yml`:
  - Compute `_record_target` per-item:
    - If `type == 'MX'`, automatically prepend `<priority> ` (default `10`) to the target unless it already starts with that prefix.
    - Otherwise use the target as-is.
  - Create / Update / Delete tasks now send `_record_target` in the request body.
  - Update and Delete matching logic now filters by `source + type + target` (using `_record_target`) so duplicate records are correctly identified.
- Updated `roles/infomaniak/README.md` to show MX record configuration without requiring a manual `priority` field.

**Verification**: YAML syntax validated. Test curls confirmed the v2 API returns `"target": "10 mxa.eu.mailgun.org"` in GET responses, confirming inline priority format.

@Clanker Set frontmatter state to completed and update info about model and token usage.

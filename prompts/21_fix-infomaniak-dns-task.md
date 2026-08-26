---
title: "Fix infomaniak dns task"
state: completed
model: infomaniak/moonshotai/Kimi-K2.6
input_tokens: N/A
---

# Run 21

Note: @Clanker refers to the "ai agent" (you) who is working on this task.

@Clanker when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

@Clanker Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

There is a bug in my task `roles/infomaniak/tasks/infomaniak_zone.yml` / `roles/infomaniak/tasks/infomaniak_dns.yml`

When I run the role with this:

```yaml
infomaniak_zones:
  - zone: ansible.build
    records:
      - { source: '', type: A, target: 179.237.73.43, state: present }
```

I get this:

```
*[main][~/Ansible-Build]$ task play -i inventories/mint_system plays/localhost.yml -t infomaniak
[WARNING]: log file at /var/log/ansible.log is not writeable and we cannot create it, aborting


PLAY [Localhost setup] *******************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************
ok: [localhost]

TASK [infomaniak : Include infomaniak dns tasks] *****************************************************************************************************
included: /home/janikvonrotz/Ansible-Build/roles/infomaniak/tasks/infomaniak_zone.yml for localhost

TASK [infomaniak : Get existing DNS records for each zone] *******************************************************************************************
ok: [localhost] => (item=ansible.build)

TASK [infomaniak : Process DNS records for each zone] ************************************************************************************************
included: /home/janikvonrotz/Ansible-Build/roles/infomaniak/tasks/infomaniak_dns.yml for localhost => (item=ansible.build)

TASK [infomaniak : Set infomaniak DNS present fact for ansible.build] ********************************************************************************
ok: [localhost] => (item={'id': 37201532, 'source': '.', 'type': 'NS', 'ttl': 3600, 'target': 'ns11.infomaniak.ch', 'updated_at': 1787725080})
ok: [localhost] => (item={'id': 37201533, 'source': '.', 'type': 'NS', 'ttl': 3600, 'target': 'ns12.infomaniak.ch', 'updated_at': 1787725080})
ok: [localhost] => (item={'id': 37201534, 'source': '.', 'type': 'TXT', 'ttl': 3600, 'target': '"v=spf1 -all"', 'updated_at': 1787725080})
ok: [localhost] => (item={'id': 37201535, 'source': '_dmarc', 'type': 'TXT', 'ttl': 3600, 'target': '"v=DMARC1; p=reject;"', 'updated_at': 1787725080})

TASK [infomaniak : Show DNS present list for ansible.build] ******************************************************************************************
ok: [localhost] =>
  infomaniak_dns_present:
  - .-NS
  - .-NS
  - .-TXT
  - _dmarc-TXT

TASK [infomaniak : Create new DNS records for ansible.build] *****************************************************************************************
ok: [localhost] => (item=. (A))

PLAY RECAP *******************************************************************************************************************************************
localhost                  : ok=7    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
```

When I run the role with:

```yaml
infomaniak_zones:
  - zone: taskfile.build
    records:
      - { source: 'git', type: CNAME, target: zeus.mint-system.com, state: present }
  - zone: ansible.build
    records:
      - { source: '', type: A, target: 179.237.73.43, state: present }
```

I get this:

```
[main][~/Ansible-Build]$ task play -i inventories/mint_system plays/localhost.yml -t infomaniak
[WARNING]: log file at /var/log/ansible.log is not writeable and we cannot create it, aborting


PLAY [Localhost setup] *******************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************
ok: [localhost]

TASK [infomaniak : Include infomaniak dns tasks] *****************************************************************************************************
included: /home/janikvonrotz/Ansible-Build/roles/infomaniak/tasks/infomaniak_zone.yml for localhost

TASK [infomaniak : Get existing DNS records for each zone] *******************************************************************************************
ok: [localhost] => (item=taskfile.build)
ok: [localhost] => (item=ansible.build)

TASK [infomaniak : Process DNS records for each zone] ************************************************************************************************
included: /home/janikvonrotz/Ansible-Build/roles/infomaniak/tasks/infomaniak_dns.yml for localhost => (item=taskfile.build)
included: /home/janikvonrotz/Ansible-Build/roles/infomaniak/tasks/infomaniak_dns.yml for localhost => (item=ansible.build)

TASK [infomaniak : Set infomaniak DNS present fact for taskfile.build] *******************************************************************************
ok: [localhost] => (item={'id': 28684654, 'source': '.', 'type': 'NS', 'ttl': 3600, 'target': 'ns11.infomaniak.ch', 'updated_at': 1758300600})
ok: [localhost] => (item={'id': 28684656, 'source': '.', 'type': 'NS', 'ttl': 3600, 'target': 'ns12.infomaniak.ch', 'updated_at': 1758300601})
ok: [localhost] => (item={'id': 28684657, 'source': '.', 'type': 'TXT', 'ttl': 3600, 'target': '"v=spf1 -all"', 'updated_at': 1758300602})
ok: [localhost] => (item={'id': 28684658, 'source': '_dmarc', 'type': 'TXT', 'ttl': 3600, 'target': '"v=DMARC1; p=reject;"', 'updated_at': 1758300602})
ok: [localhost] => (item={'id': 28696995, 'source': '.', 'type': 'A', 'ttl': 3600, 'target': '83.228.234.124', 'updated_at': 1776323341})
ok: [localhost] => (item={'id': 28697006, 'source': 'git', 'type': 'CNAME', 'ttl': 3600, 'target': 'zeus.mint-system.com', 'updated_at': 1782116855})

TASK [infomaniak : Show DNS present list for taskfile.build] *****************************************************************************************
ok: [localhost] =>
  infomaniak_dns_present:
  - .-NS
  - .-NS
  - .-TXT
  - _dmarc-TXT
  - .-A
  - git-CNAME

TASK [infomaniak : Show DNS present list for ansible.build] ******************************************************************************************
ok: [localhost] =>
  infomaniak_dns_present:
  - .-NS
  - .-NS
  - .-TXT
  - _dmarc-TXT
  - .-A
  - git-CNAME

PLAY RECAP *******************************************************************************************************************************************
localhost                  : ok=8    changed=0    unreachable=0    failed=0    skipped=7    rescued=0    ignored=0
```

It seems the `infomaniak_dns_present` is not resetted correctly.

## Worklog

@Clanker Add a summary here once the task has been completed.

Fixed bug where `infomaniak_dns_present` was not reset between zones, causing subsequent zones to inherit DNS records from previous zones. Added a task at the beginning of `roles/infomaniak/tasks/infomaniak_dns.yml` to reset `infomaniak_dns_present: []` before processing each zone's records. Also removed the unnecessary `| default([])` filter in the "Set infomaniak DNS present fact" task since the list is now explicitly initialized.

@Clanker Set frontmatter state to completed and update info about model and token usage.
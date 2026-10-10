---
kind: environment
---

<img src="/logos/docker_restic.png" alt="docker_restic logo" width="100" height="100">


# Docker Restic role

Runs Restic in Docker container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/restic/restic
restic_image: restic/restic:0.19.1
restic_owner: admin # default: root
restic_group: wheel # default: backup
restic_repo_type: s3 # default: s3
restic_s3_endpoint: https://s3.swiss-backup02.infomaniak.com
restic_s3_bucket: my-restic-bucket
restic_s3_region: us-east-1 # default: us-east-1
restic_s3_access_key: # default: "{{ vault_restic_s3_access_key }}"
restic_s3_secret_key: # default: "{{ vault_restic_s3_secret_key }}"
restic_backup_set:

restic_backup_rotation:
  daily: 7 # default: 7
  weekly: 4 # default: 4
  monthly: 1 # default: 1
```

And include it in your playbook.

```yml
- hosts: restic
  roles:
  - role: restic
```


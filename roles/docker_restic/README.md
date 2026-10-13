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
  - id: "Backup Nextcloud volume"
    type: docker-restic-backup
    volume: "nextcloud01"
    tags:
      - postgres
      - nextcloud01
    hour: "1"
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

## Docs

### Recover volume from backup

Get the id of the snaphosts that you would like to recover:

```bash
sudo docker-restic snapshots
ID        Time                 Host        Tags                 Paths             Size
--------------------------------------------------------------------------------------------
2ec9d49d  2026-10-13 19:10:54  apollo      postgres,postgres11  /data/postgres11  70.858 MiB
--------------------------------------------------------------------------------------------
Timestamps shown in UTC
1 snapshots
```

Stop the containers that are connected to the volume:

```bash
docker stop nextcloud03 postgres11
```

Restore the volume data:

```bash
sudo docker-restic-restore -v postgres11 -s 2ec9d49d
Restore 2ec9d49d of postgres11 into volume postgres11? [y/N] y
Run restic restore for Docker volume postgres11 into postgres11.
restoring snapshot 2ec9d49d of [/data/postgres11] at 2026-10-13 19:10:54.579863287 +0000 UTC by root@apollo to /
Summary: Restored 147 files/dirs (18.438 MiB) in 0:00, skipped 1902 files/dirs 52.420 MiB
verifying files in /
finished verifying 116 files in / (took 25ms)
```

Start the containers:

```bash
docker start postgres11 nextcloud03
```

<img src="/logos/s3cmd.png" alt="s3cmd logo" width="100" height="100">

# s3cmd role

Install and configure s3cmd.

## Usage

Configure the role.

```yml
s3cmd_host_base: sos-ch-dk-2.exo.io
s3cmd_host_bucket: kronos.sos-ch-dk-2.exo.io
s3cmd_access_key: EXO2677bc43796a0cff80b29b79
s3cmd_secret_key: # default: "{{ vault_s3cmd_secret_key }}"
s3cmd_backup_set:
  - id: "disk2"
    src: /mnt/sdb/
    target: kronos
    hour: "5"
  - id: "disk"
    src: /mnt/sda/
    target: kronos
    hour: "3"
    disabled: true # default: false
    state: absent # default: present
```

And include it in your playbook.

```yml
- hosts: s3cmd
  roles:
  - role: s3cmd
```

## Docs

### Use with s3cmd cli

Become root and list buckets.

```bash
sudo su
s3cmd ls
```

List the files in a bucket.

```bash
s3cmd ls s3://kronos
```
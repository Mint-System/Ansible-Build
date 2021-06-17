# Ansible s3cmd role

Install and configure s3cmd.

## Usage

Configure the role.

**vars.yml**

```yml
s3cmd_host_base: sos-ch-dk-2.exo.io
s3cmd_host_bucket: kronos.sos-ch-dk-2.exo.io
s3cmd_access_key: EXO2677bc43796a0cff80b29b79
s3cmd_secret_key: "{{ vault_s3cmd_secret_key }}"
s3cmd_backup_sets:
  - id: "disk2"
    src: /mnt/kronos-disk2/
    target: kronos
    hour: "5"
  - id: "disk1"
    src: /mnt/kronos-disk1/
    target: kronos
    hour: "3"
    disabled: true # default: false
    status: absent # default: present
```

And include it in your playbook.

```yml
- hosts: s3cmd
  roles:
  - role: s3cmd
```

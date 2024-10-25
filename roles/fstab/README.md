# fstab role

Configure the fstab file.

## Usage

Configure the role.

```yml
fstab_credentials:
  - username: sync
    password: "{{ vault_fstab_credentials_1_password }}"
    domain: domain
fstab_mounts:
  - path: /mnt/sdb
    src: /dev/disk/by-id/scsi-0HC_Volume_10321808
    opts: discard,nofail,defaults
    state: mounted
    fstype: ext4
```

And include it in your playbook.

```yml
- hosts: fstab
  roles:
  - role: fstab
```
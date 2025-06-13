<img src="/logos/etc_hosts.png" alt="etc_hosts logo" width="100" height="100">

# etc Hosts role

Add entries to /etc/hosts files.

## Usage

Configure the role.

```yml
etc_hosts:
  - ip: 172.17.4.15
    name: doc.kmsu.ch
```

And include it in your playbook.

```yml
- hosts: etc_hosts
  roles:
  - role: etc_hosts
```

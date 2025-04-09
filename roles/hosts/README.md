<img src="/logos/hosts.png" alt="hosts logo" width="100" height="100">

# Hosts role

Add entries to hosts files.

## Usage

Configure the role.

```yml
hosts:
  - ip: 172.17.4.15
    name: doc.kmsu.ch
```

And include it in your playbook.

```yml
- hosts: hosts
  roles:
  - role: hosts
```

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

# Ansible Innernet Server role

Setup WireGuard based internal network.

## Usage

Configure the role.

**vars.yml**

```yml
innernet_server_network_name: mintsystem
innernet_server_network_cidr: 10.42.0.0/16
innernet_server_cidrs:
  - name: infra
    cidr: 10.42.5.0/24
    parent: mintsystem
innernet_server_peers:
  - name: leto
    cidr: infra
  - name: pop-os
    cidr: infra
```

And include it in your playbook.

```yml
- hosts: innernet-server
  roles:
  - role: innernet-server
```

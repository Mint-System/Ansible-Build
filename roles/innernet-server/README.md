# Innernet Server role

Setup WireGuard based internal network.

## Usage

Configure the role.

**vars.yml**

```yml
# https://github.com/tonarino/innernet
packages:
  - name: wireguard
  - deb: https://github.com/tonarino/innernet/releases/download/v1.5.3/innernet_1.5.3_amd64.deb
  - deb: https://github.com/tonarino/innernet/releases/download/v1.5.3/innernet-server_1.5.3_amd64.deb

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

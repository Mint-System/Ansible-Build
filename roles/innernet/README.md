<img src="/logos/innernet.png" alt="innernet logo" width="100" height="100">

# Innernet role

Setup WireGuard based internal network.

## Usage

Configure the role.

```yml
apt_repos:
  - name: https://tommie.github.io/innernet-debian/debian
    key: https://tommie.github.io/innernet-debian/repository.asc
```

Configure the server role.

```yml
host_packages:
  - name: wireguard
  - name: innernet-server
innernet_server_network_name: mint-system
innernet_server_network_cidr: 10.42.0.0/16
innernet_server_cidrs:
  - name: infra
    cidr: 10.42.5.0/24
    parent: mint-system
innernet_server_peers:
  - name: server1
    cidr: infra
  - name: client1
    cidr: infra
```

Configure the client role.

```yml
host_packages:
  - name: wireguard
  - name: innernet
innernet_server_network_name: mint-system
innernet_client_peer_name: client1 # default: {{ inventory_hostname }}
```

And include it in your playbook.

```yml
- hosts: innernet
  roles:
  - role: innernet
```

## Docs

### Show server status

Run `sudo systemctl status innernet-server@$NETWORK_NAME`.

### Show client status

Run `sudo innernet` to get the list of available peers.

### Start client service

Check innernet service with `sudo systemctl status innernet@$NETWORK_NAME`.

Start innernet service with `sudo systemctl start innernet@$NETWORK_NAME`.

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
innernet_client_peer_name: client1
innernet_client_invitation_file: |
  [interface]
  network-name = "mint-system"
  address = "10.42.5.1/16"
  private-key = "AJPLsA43duTfZ6bHQtW5VAdcfDq4SoJOBXflM="

  [server]
  public-key = "L5gQCsk3zMkWivS8j2sMWFhTsEXjcDoft75i+zE="
  external-endpoint = "49.12.42.20:51820"
  internal-endpoint = "10.42.0.1:51820"
```

And include it in your playbook.

```yml
- hosts: innernet
  roles:
  - role: innernet
```

The following tags are available:

* innernet_server
* innernet_client

## Docs

### Show client status

Run `sudo innernet status` to get the list of available peers.

### Start client service

Check innernet service with `sudo systemctl status innernet@{{ innernet_client_network_name }}`.

Start innernet service with `sudo systemctl start innernet@{{ innernet_client_network_name }}`.

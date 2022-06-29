# Innernet Client role

Setup WireGuard based internal network.

## Usage

Configure the role.

**vars.yml**

```yml
# https://github.com/tonarino/innernet
packages:
  - name: wireguard
  - deb: https://github.com/tonarino/innernet/releases/download/v1.5.3/innernet_1.5.3_amd64.deb

innernet_client_network_name: mint-system
innernet_client_peer_name: apollo
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
- hosts: innernet-client
  roles:
  - role: innernet-client
```

## Docs

### Show status

Run `sudo innernet status` to get the list of available peers.

### Start Service

Check innernet service with `sudo systemctl status innernet@{{ innernet_client_network_name }}`.

Start innernet service with `sudo systemctl start innernet@{{ innernet_client_network_name }}`.

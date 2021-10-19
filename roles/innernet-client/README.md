# Ansible Innernet Client role

Setup WireGuard based internal network.

## Usage

Configure the role.

**vars.yml**

```yml
innernet_client_network_name: mintsystem
innernet_client_invitation_file: |
  [interface]
  network-name = "mintsystem"
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

<img src="/logos/autossh.png" alt="ssh logo" width="100" height="100">

# Autossh role

Configure Autossh tunnels.

## Usage

Configure the role.

```yml
autossh_enabled: true # default: false
autossh_data_dir: /usr/share/ssh # default: /usr/share/autossh
autossh_tunnels:
  - local_user: server1
    local_key_file:  /home/server1/.ssh/id_ed25519
    local_port: 8080
    remote_port: 80
    remote_user: ubuntu
    remote_server: server2.example.com
    remote_ssh_port: 2222 # default: 22
```

And include it in your playbook.

```yml
- hosts: autossh
  roles:
  - role: autossh
```

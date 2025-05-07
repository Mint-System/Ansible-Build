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
    local_key_file: /home/server1/.ssh/id_ed25519 # default: "/home/{{ item.local_user }}/.ssh/id_ed25519"
    local_interface: 127.0.0.1 # default: 0.0.0.0
    local_port: 8080
    ssh_user: ubuntu
    ssh_server: server2.example.com
    ssh_port: 2222 # default: 22
    remote_server: 172.18.30.1 # default: localhost
    remote_port: 80
```

And include it in your playbook.

```yml
- hosts: autossh
  roles:
  - role: autossh
```

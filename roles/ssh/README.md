<img src="/logos/ssh.png" alt="ssh logo" width="100" height="100">

# SSH role

Configure SSH client and server.

## Usage

Configure the role.

```yml
ssh_port: 2222 # default: 22
ssh_enabled: false # default: true
ssh_disallow_root_access: false # default: true
ssh_allow_password_authentication: true # default: false
```

And include it in your playbook.

```yml
- hosts: ssh
  roles:
  - role: ssh
```

## Docs

### Show OpenSSH version

Show OpenSSH version for alls hosts.

```bash
task run all -i inventories/setup -a "ssh -V"
```
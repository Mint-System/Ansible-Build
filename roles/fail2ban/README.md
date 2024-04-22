# fail2ban role

Install and configure fail2ban.

## Usage

Configure all depending roles.

```yml
fail2ban_packages:
  - name: fail2ban # default: fail2ban
fail2ban_enabled: true # default: false
fail2ban_sshd_enabled: "true" # default: "true"
fail2ban_ignoreip: 84.75.180.227
fail2ban_bantime: 10m # default: 1d
```

Include it in your playbook.

```yml
- hosts: fail2ban
  roles:
  - role: fail2ban
```

## Docs

### Show status

Run `fail2ban-client status sshd` to get the status of the fail2ban service.

Show status for alls hosts.

```bash
ansible all -i inventories/setup -a "sudo fail2ban-client status sshd"
```

### Stop fail2ban service

To stop the fail2ban service run:

```bash
fail2ban-client stop
```
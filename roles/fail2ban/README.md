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
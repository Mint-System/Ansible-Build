# Ansible fail2ban role

Install and configure fail2ban.

## Usage

Configure all depending roles.

```yml
fail2ban_packages:
  - name: fail2ban # Default: fail2ban
fail2ban_enabled: true # Default: false
fail2ban_sshd_enabled: "true" # Default: "true"
fail2ban_ignoreip: 84.75.180.227
fail2ban_bantime: 10m # Default: 1d
```

Include it in your playbook.

```yml
- hosts: fail2ban
  roles:
  - role: fail2ban
```
# Ansible IAM role

Configures users and groups.

## Usage

Configure the role.

**vars.yml**

```yml
iam_options:
  add_wheel_to_sudoers: yes
  disallow_ssh_root_access: yes
iam_groups:
  - wheel
iam_users:
  - username: admin
    ssh_public_key: "ssh-rsa ANzaC1yc2EA...KHgKLVcBaeKQ== admin@example.com"
    groups: wheel,docker
    shell: /bin/zsh
    zshrc: |
      PROMPT="$fg[cyan]%}$USER@%{$fg[blue]%}%m ${PROMPT}"
    hosts:
      - server1
      - server2
  - username: bot
    ssh_public_key: "ssh-ed25519 ANzaC1yc2EA...KHgKLVcBaeKQ== bot@example.com"
    ssh_private_key: "{{ vault_bot_ssh_private_key }}"
    hosts:
      - hermes
```

And include it in your playbook.

```yml
- hosts: iam
  roles:
  - role: iam
```
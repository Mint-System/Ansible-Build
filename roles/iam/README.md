# IAM role

Configures users and groups.

## Usage

Configure the role.

**vars.yml**

```yml
iam_root_password: "{{ vault_iam_root_password }}"
iam_disallow_ssh_root_access: false # default: true
iam_allow_ssh_password_authentication: true # default: false
iam_groups:
  - name: wheel
    add_group_to_sudoers: true
  - name: guests
    add_group_to_sudoers: false
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
      - server1
host_iam_users:
  - username: bobmeyer
    passwort: "{{ vault_iam_users_bobmeyer_password }}"
    hosts:
      - server1
```

And include it in your playbook.

```yml
- hosts: iam
  roles:
  - role: iam
```

## Docs

### Set password manually

Run `sudo passwd $USERNAME` to set the password.

### Add user to group manually

Run `sudo usermod -a -G sshusers janikvonrotz` to add a user to a group.
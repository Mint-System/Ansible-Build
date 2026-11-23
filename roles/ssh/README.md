---
kind: environment
---

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
ssh_deploy_keys: # default: []
  - name: Odoo-Apps-Customer-Name
    ssh_public_key: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFM2dT27qOOiKHZfecvzlh+oAgzxwxC+G9uFp9g9VZxw Odoo-Apps-Customer-Name"
    ssh_private_key: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}/id_ed25519.key"
    users:
      - timmywyss
      - bot
```

And include it in your playbook.

```yml
- hosts: ssh
  roles:
  - role: ssh
```

## Docs

### Generate deploy keys

Generate a named key pair for a private git repo. The name is used as the key filename on the target host, so it must be filesystem safe.

```bash
DEPLOY_KEY_NAME=odoo-apps-customer-name
HOST=nyx
ssh-keygen -t ed25519 -C "$DEPLOY_KEY_NAME" -f "host_vars/$HOST/id_ed25519.key" -N ''
echo "ssh_public_key: $(cat "host_vars/$HOST/id_ed25519.key.pub")"
rm "host_vars/$HOST/id_ed25519.key.pub"
```

Encrypt the private key with ansible-vault.

```bash
ansible-vault encrypt --encrypt-vault-id mint_system "host_vars/$HOST/id_ed25519.key"
```

The key lives next to `vars.yml` in the host folder and only the private key is kept there. The public key goes into `vars.yml` as `ssh_public_key`. Ansible loads every file in a `host_vars/<host>` directory as variables, so the key **must** have a file extension other than `.yml`, `.yaml` or `.json`. A file without a dot in its name is parsed as well, `id_ed25519.key` is safe.

Set the public key as a plain string, it is not a secret. Reference the private key file in `ssh_deploy_keys`. The example below deploys the key to the users `timmywyss` and `bot` on the host.

```yml
ssh_deploy_keys:
  - name: Odoo-Apps-Customer-Name
    ssh_public_key: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFM2dT27qOOiKHZfecvzlh+oAgzxwxC+G9uFp9g9VZxw Odoo-Apps-Customer-Name"
    ssh_private_key: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}/id_ed25519.key"
    users:
      - timmywyss
      - bot
```

The role copies the private key to `~/.ssh/<name>` for every listed user and adds an ssh config entry `Host github.com-<name>` with `IdentitiesOnly yes`. Optional keys are `host` (default `github.com`) and `ssh_config` (default `true`).

Add the public key as a deploy key in the git repo settings, for example <https://github.com/Mint-System/Odoo-Apps-Customer-Name/settings/keys>. Enable write access only if the key must also push.

Clone a repo with the deployed key:

```bash
odoo-repos-clone -p /usr/share/odoo09-dev/addons -r ssh://git@github.com/Mint-System/Odoo-Apps-Customer-Name.git -b 19.0 -t mint-system-customer-name -k ~/.ssh/odoo-apps-customer-name
```

### Show OpenSSH version

Show OpenSSH version for alls hosts.

```bash
task run all -i inventories/mint_system -a "ssh -V"
```

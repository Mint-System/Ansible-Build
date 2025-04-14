<img src="/logos/iam.png" alt="iam logo" width="100" height="100">

<img src="/logos/iam.png" alt="iam logo" width="100" height="100">

# IAM role

Identity and Access Management. Configure user and groups.

## Usage

Configure the role.

```yml
iam_root_password: "{{ vault_iam_root_password }}"
iam_groups:
  - name: wheel
    sudoers_commands: ALL
  - name: guests
  - name: operators
    sudoers_commands: /usr/bin/docker ps, /usr/bin/docker start *,  /usr/bin/docker stop *, /usr/bin/docker restart *
iam_users:
  - username: admin
    state: present
    comment: "Administrator"
    ssh_public_key: "ssh-rsa ANzaC1yc2EA...KHgKLVcBaeKQ== admin@example.com"
    groups: wheel,docker
    shell: /bin/zsh
    zshrc: |
      PROMPT="$fg[cyan]%}$USER@%{$fg[blue]%}%m ${PROMPT}"
    hosts:
      - server1
      - server2
  - username: operator
    state: present
    groups: operators
    hosts: "{{ groups.all }}"
  - username: bot
    state: present
    comment: "Bot Example"
    ssh_public_key: "ssh-ed25519 ANzaC1yc2EA...KHgKLVcBaeKQ== bot@example.com"
    ssh_private_key: "{{ vault_bot_ssh_private_key }}"
    hosts:
      - server1
host_iam_users:
  - username: bobmeyer
    state: present
    comment: "Bob Meyer"
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

### Kubernetes

Configure the manifest.

```yml
k8s_iam_service_account: k8s-deployer
```

And include it in your localhost playbook.

```yml
- hosts: localhost
  roles:
  - role: iam
```

## Docs

### Set password manually

Run `sudo passwd $USERNAME` to set the password.

### Add user to group manually

Run `sudo usermod -a -G sshusers janikvonrotz` to add a user to a group.

### Generate ssh key pair

Generate a ssh key pair for the username.

```bash
SSH_USERNAME=n8ncloud
ssh-keygen -t ed25519 -C "$SSH_USERNAME" -f ./id_ed25519 
echo "vault_${SSH_USERNAME}_ssh_private_key: |"
cat ./id_ed25519 | sed 's/^/    /'
echo "ssh_public_key: $(cat ./id_ed25519.pub)"
```

### Get Kubernetes service account token

The service account token ist stored as secret.

```bash
kubectl get secrets k8s-deployer -o json | jq -r '.data.token' | base64 --decode

```
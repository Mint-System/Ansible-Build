---
kind: service
---

<img src="/logos/taskfile_build.png" alt="taskfile_build logo" width="100" height="100">

# Taskfile Build role

Deploy a container that builds and serves a git repo with <https://taskfile.build/>.

The container clones `taskfile_build_git_url`, runs the Taskfile commands and serves the result with Caddy.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/mintsystem/taskfile.build
taskfile_build_image: mintsystem/taskfile.build:latest # default: mintsystem/taskfile.build:latest
taskfile_build_hostname: taskfile01
taskfile_build_description: Website build # default: Taskfile Build
taskfile_build_git_url: git@github.com:Mint-System/Documentation.git
taskfile_build_task_commands: build # default: build
taskfile_build_command: caddy # default: caddy
taskfile_build_caddy_root: public # default: public
taskfile_build_ssh_public_key: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFM2dT27qOOiKHZfecvzlh+oAgzxwxC+G9uFp9g9VZxw Taskfile-Build-Repo" # default: none
taskfile_build_ssh_private_key: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}/id_ed25519.key" # default: none
taskfile_build_ssh_id_algorithm: id_ed25519 # default: id_ed25519
taskfile_build_ssh_host: github.com # default: github.com
taskfile_build_ssh_config: | # default: none
  Host github.com
    Hostname ssh.github.com
    Port 443
    User git
taskfile_build_sops_age_key: # default: "{{ vault_taskfile_build_sops_age_key }}"
taskfile_build_volume_name: taskfile01 # default: "{{ taskfile_build_hostname }}"
taskfile_build_volumes: # default: [ "{{ taskfile_build_volume_name }}:/app" ]
  - "{{ taskfile_build_volume_name }}:/app"
taskfile_build_ports:
  - 127.0.0.1:8080:80 # default: []
taskfile_build_cron_jobs:
  - name: Rebuild website
    minute: "15"
    command: ./task build
  - name: Nightly build
    hour: "3"
    minute: "0"
    command: ./task build
    disabled: true # default: false
```

And include it in your playbook.

```yml
- hosts: taskfile_build
  roles:
  - role: taskfile_build
```

The following tags are available:

* taskfile_build

## Docs

### Setup deploy keys

Generate a key pair for the build repo and encrypt the private key.

```bash
DEPLOY_KEY_NAME=Taskfile-Build-Repo
HOST=clio
ssh-keygen -t ed25519 -C "$DEPLOY_KEY_NAME" -f "host_vars/$HOST/id_ed25519.key" -N ''
echo "taskfile_build_ssh_public_key: $(cat "host_vars/$HOST/id_ed25519.key.pub")"
rm "host_vars/$HOST/id_ed25519.key.pub"
ansible-vault encrypt --encrypt-vault-id mint_system "host_vars/$HOST/id_ed25519.key"
```

Set the public key in `vars.yml` and reference the private key file. The file must not have a `.yml`, `.yaml` or `.json` extension, see the [ssh role](../ssh/).

```yml
taskfile_build_git_url: git@github.com:Mint-System/Documentation.git
taskfile_build_ssh_public_key: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFM2dT27qOOiKHZfecvzlh+oAgzxwxC+G9uFp9g9VZxw Taskfile-Build-Repo"
taskfile_build_ssh_private_key: "{{ inventory_dir }}/host_vars/{{ inventory_hostname }}/id_ed25519.key"
```

Add the public key as a deploy key with read access in the git repo settings, for example <https://github.com/Mint-System/Documentation/settings/keys>.

Set `taskfile_build_ssh_config` when port `22` is blocked.

```yml
taskfile_build_ssh_config: |
  Host github.com
    Hostname ssh.github.com
    Port 443
    User git
```

<img src="/logos/git.png" alt="git logo" width="100" height="100">

# Git role

Checkout Git repositories.

## Usage

Configure the role.

```yml
git_repositories:
  - repo: https://github.com/Digital-Cluster-Uri/Website
    dest: /usr/share/nginx01/static
    version: main
  - repo: git@github.com:sozialinfo/reference-data.git
    key_file: /home/sozialinfo-git-bot/.ssh/id_ed25519
    dest: /usr/share/postgres43/reference-data
    version: main
```

Include the role in your playbook.

```yml
- hosts: git
  roles:
  - role: git
```

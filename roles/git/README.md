# Git role

Checkout Git repositories.

## Usage

Configure the role.

**vars.yml**

```yml
git_repositories:
  - repo: https://github.com/Digital-Cluster-Uri/Website
    dest: /usr/share/nginx01/static
    version: main
```

Include the role in your playbook.

```yml
- hosts: git
  roles:
  - role: git
```

# Ansible package role

Install and pin packages.

## Usage

Configure the role.

**vars.yml**

```yml
packages:
  - name: vim=2:8.0.1453-1ubuntu1.1
  - name: bacula-console-qt
    state: absent
```

And include it in your playbook.

```yml
- hosts: package
  roles:
  - role: packages
    tags: package
```

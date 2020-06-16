# Ansible Collabora Code role

Deploys Collabora Online Development Edition (CODE) container.

## Usage

Configure the role.

**vars.yml**

```yml
collabora_code_image: collabora/code:4.2.3.1
collabora_code_hostname: colla01
collabora_code_port: 9980
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: collabora-code
    tags: collabora-code
```

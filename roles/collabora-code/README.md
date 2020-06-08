# Ansible Collabora Code role

Deploys Collabora Online Development Edition (CODE) container.

## Requires

The Ansible Collabora Online Development Edition role requires the following roles:

* docker
* docker-network
* nextcloud

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
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: nextcloud
    tags: nextcloud
  - role: collabora-code
    tags: collabora-code
```

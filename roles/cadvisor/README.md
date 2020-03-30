# Ansible cAdvisor role

Deploys cAdvisor container.

## Requires

The Ansible cAdvisor role requires the following roles:

* docker
* docker-network

## Usage

Configure the role.

**vars.yml**

```yml
cadvisor_hostname: cadvisor01
cadvisor_image: gcr.io/google-containers/cadvisor:v0.34.0
```

And include it in your playbook.

```yml
- hosts: cAdvisor
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: cadvisor
    tags: cadvisor
```


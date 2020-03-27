# Ansible Logstash role

Deploys Logstash Docker container.

## Requires

The Ansible Logstash role requires the following roles:

* docker
* docker-network
* elasticsearch

## Usage

Configure the role.

**vars.yml**

```yml

```

And include it in your playbook.

```yml
- hosts: kibana
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: elasticsearch
    tags: elasticsearch
  - role: logstash
    tags: logstash
```

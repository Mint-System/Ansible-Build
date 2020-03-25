# Ansible Kibana role

Deploys Kibana Docker container.

## Requires

The Ansible Kibana role requires the following roles:

* docker
* docker-network
* elasticsearch

## Usage

Configure the role.

**vars.yml**

```yml
kibana_image: docker.elastic.co/kibana/kibana:7.6.1
kibana_hostname: kibana01
kibana_elasticsearch_host: elastic01
kibana_server_name: monitor.example.com
kibana_elasticsearch_username: kibana
kibana_elasticsearch_password: "{{ vault_kibana_elasticsearch_password }}"
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
  - role: kibana
    tags: kibana
```

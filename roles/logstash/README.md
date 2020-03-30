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
logstash_image: docker.elastic.co/logstash/logstash:7.6.1
logstash_hostname: logst01
logstash_data_dir: /usr/share/logst01
logstash_elasticsearch_hostname: elastic01
logstash_elasticsearch_username: elastic
logstash_elasticsearch_password: "{{ vault_logstash_elasticsearch_password }}"
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

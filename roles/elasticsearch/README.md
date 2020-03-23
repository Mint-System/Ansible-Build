# Ansible ElasticSearch role

Deploys ElasticSearch Docker cluster.

## Requires

The Ansible ElasticSearch role requires the following roles:

* docker
* docker-network

## Usage

Configure the role.

**vars.yml**

```yml
elasticsearch_image: docker.elastic.co/elasticsearch/elasticsearch:7.6.1
elasticsearch_cluster_name: elastic-cluster01
elasticsearch_masternodes: "elastic01,elastic02"
elasticsearch_nodes:
  - hostname: elastic01
    data_dir: /usr/share/elastic01
    volume_name: elastic_data01
    seed_hosts: "elastic02"
  - hostname: elastic02
    data_dir: /usr/share/elastic02
    volume_name: elastic_data02
    seed_hosts: "elastic01"
elasticsearch_password: "{{ vault_elasticsearch_password }}"
elasticsearch_users:
  - name: kibana
    password: "{{ vault_elasticsearch_kibana_password }}"
  - name: beats_system
    password: "{{ vault_elasticsearch_beats_system_password }}"
```

And include it in your playbook.

```yml
- hosts: postgres
  roles:
  - role: docker
    tags: docker
  - role: docker-network
    tags: docker-network
  - role: elasticsearch
    tags: elasticsearch
```

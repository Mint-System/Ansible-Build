# Ansible ElasticSearch role

Deploys ElasticSearch Docker cluster.

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
    primary: yes
  - hostname: elastic02
    data_dir: /usr/share/elastic02
    volume_name: elastic_data02
    seed_hosts: "elastic01"
    primary: no
elasticsearch_password: "{{ vault_elasticsearch_password }}"
elasticsearch_users:
  - name: kibana
    password: "{{ vault_elasticsearch_kibana_password }}"
  - name: beats_system
    password: "{{ vault_elasticsearch_beats_system_password }}"
  - name: logstash_system
    password:  "{{ vault_elasticsearch_logstash_password }}"
```

And include it in your playbook.

```yml
- hosts: elasticsearch
  roles:
  - role: elasticsearch
    tags: elasticsearch
```

## Development

### Encrypting communications between nodes in a cluster
edit

Generate key material for node communication.

```bash
# Log into elastic container
docker exec -it elastic01 /bin/bash
# Create ca certificate without password
elasticsearch-certutil ca
# Create node certificate wihtout password
elasticsearch-certutil  cert --ca elastic-stack-ca.p12
# Copy these files into the files folder of the elasticsearch role
# Encrypt files with Ansible vault
ansible-vault encrypt roles/elasticsearch/files/elastic-certificates.p12
ansible-vault encrypt roles/elasticsearch/files/elastic-stack-ca.p12
```

Source: [Elastic - Encrypting communications in Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/configuring-tls.html)
# Elasticsearch role

Deploy Elasticsearch Docker cluster.

## Usage

Configure the role.

**vars.yml**

```yml
# https://www.docker.elastic.co/r/elasticsearch
elasticsearch_image: docker.elastic.co/elasticsearch/elasticsearch:7.15.2
```

Setup a single node.

```yml
elasticsearch_hostname: elastic01
elasticsearch_description: Search index for nextcloud01 # default: Elasticsearch
elasticsearch_data_dir: /usr/share/elastic # default: "{{ elasticsearch_hostname }}"
elasticsearch_volume_name: elastic_data01 # default: "{{ elasticsearch_hostname }}"
elasticsearch_password: "{{ vault_elasticsearch_password }}"
elasticsearch_users:
  - name: nextcloud
    password: "{{ vault_elasticsearch_nextcloud_password }}"
```

Setup a cluster.

```yml
elasticsearch_cluster_name: elastic-cluster01
elasticsearch_masternodes: "elastic01,elastic02"
elasticsearch_nodes:
  - hostname: elastic01
    data_dir: /usr/share/elastic01
    volume_name: elastic_data01
    seed_hosts: "elastic02"
    primary: true
  - hostname: elastic02
    data_dir: /usr/share/elastic02
    volume_name: elastic_data02
    seed_hosts: "elastic01"
    primary: false
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
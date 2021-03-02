# Ansible Logstash role

Deploy Logstash Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
logstash_image: docker.elastic.co/logstash/logstash:7.6.1
logstash_hostname: logst01
logastash_description: log extractor # default: Logstash
logstash_data_dir: /usr/share/logst # default: "/usr/share/{{ logstash_hostname }}"
logstash_elasticsearch_hostname: elastic01
logstash_elasticsearch_username: elastic
logstash_elasticsearch_password: "{{ vault_logstash_elasticsearch_password }}"
```

And include it in your playbook.

```yml
- hosts: logstash
  roles:
  - role: logstash
```

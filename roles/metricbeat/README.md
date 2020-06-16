# Ansible Metricbeat role

Deploys Metricbeat Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
metricbeat_image: docker.elastic.co/beats/metricbeat:7.6.1
metricbeat_hostname: metric01
metricbeat_data_dir: /usr/share/metric01
metricbeat_setup: true
metricbeat_kibana_host: kibana01
metricbeat_kibana_username: kibana
metricbeat_kibana_password: "{{ vault_metricbeat_kibana_password }}"
metricbeat_elasticsearch_hostname: elastic01
metricbeat_elasticsearch_username: elastic
metricbeat_elasticsearch_password: "{{ vault_metricbeat_elasticsearch_password }}"
metricbeat_logstash_hostname: logst01
```

And include it in your playbook.

```yml
- hosts: metricbeat
  roles:
  - role: metricbeat
    tags: metricbeat
```

# Metricbeat role

Deploy Metricbeat Docker container.

## Usage

Configure the role.

```yml
metricbeat_image: docker.elastic.co/beats/metricbeat:7.6.1
metricbeat_hostname: metric01
metricbeat_description: host metrics # default: Metricbeat
metricbeat_data_dir: /usr/share/metric # default: "/usr/share/{{ metricbeat_hostname }}"
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
```

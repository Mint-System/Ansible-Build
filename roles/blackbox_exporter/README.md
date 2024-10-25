# Blackbox exporter role

Deploy Blackbox exporter container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/prom/blackbox-exporter
blackbox_exporter_image: prom/blackbox-exporter:v0.25.0
blackbox_exporter_hostname: blackbox01
blackbox_exporter_description: Probing service for server1 # default: Blackbox exporter
blackbox_exporter_data_dir: /usr/share/blackbox # default: "/usr/share/{{ blackbox_exporter_hostname }}"
```

Setup the Blackbox scrape job for Prometheus.

```yml
prometheus_scrape_configs:
  - job_name: 'blackbox'
    metrics_path: "/probe"
    scrape_interval: 60s
    params:
      module: [http_2xx]
    static_configs:
      - targets: "{{ groups['all'] | map('extract', hostvars) | json_query('[*].nginx_proxies[*].src_hostname') | flatten | map('regex_replace', '^(.*)$', 'https://\\1') }}"
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: blackbox01:9115
```

And include it in your playbook.

```yml
- hosts: blackbox_exporter
  roles:
  - role: blackbox_exporter
```

## Docs

### Debug website probe

On the host run:

```bash
WEBSITE=https://example.com
curl "http://blackbox01:9115/probe?target=$WEBSITE&module=http_2xx&debug=true"
```


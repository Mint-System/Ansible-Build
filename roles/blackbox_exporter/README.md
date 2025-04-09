<img src="/logos/blackbox_exporter.png" alt="blackbox_exporter logo" width="100" height="100">

# Blackbox exporter role

Deploy Blackbox exporter container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/prom/blackbox-exporter
blackbox_exporter_image: prom/blackbox-exporter:v0.26.0
blackbox_exporter_hostname: blackbox01
blackbox_exporter_description: Probing service for prometheus # default: Blackbox exporter
blackbox_exporter_data_dir: /usr/share/blackbox # default: "/usr/share/{{ blackbox_exporter_hostname }}"
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
curl "http://blackbox01:9115/probe?target=$WEBSITE&module=http_redirect&debug=true"
```

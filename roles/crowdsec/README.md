# CrowdSec role

Deploy CrowdSec container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/crowdsecurity/crowdsec
crowdsec_image: crowdsecurity/crowdsec:v1.6.4
crowdsec_hostname: crowdsec01
crowdsec_description: Log Forwarder # default: CrowdSec
crowdsec_volume_name: crowdsec01_data # default: "{{ crowdsec_hostname }}"
crowdsec_data_dir: /usr/share/crowdsec # default: "/usr/share/{{ crowdsec_hostname }}"
crowdsec_enroll_key: # default: "{{ vault_crowdsec_enroll_key }}
crowdsec_whitelist_ip_addresses: |
  - "49.12.42.20" # atlas.mint-system.com
```

And include it in your playbook.

```yml
- hosts: crowdsec
  roles:
  - role: crowdsec
```

## Docs

### Show CrowdSec metric status

The crowdsec service runs in the container.

```bash
docker exec crowdsec01 cscli metrics show
```

### Show CrowdSec bouncers

```bash
docker exec crowdsec01 cscli bouncers list
```

### Test whitelist rules

```bash
LOGS=$(docker logs nginx01 2>&1 | grep "172.19.0.1" | tail -n 1)
docker exec crowdsec01 bash -c "echo $LOGS | cscli explain -f- --type nginx"
```

### Trigger an alert

```bash
pip install wapiti3
```

```bash
wapiti -u http://odoo.local/
```

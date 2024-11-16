# CrowdSec role

Deploy CrowdSec container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/r/crowdsecurity/crowdsec
crowdsec_image: crowdsecurity/crowdsec:v1.6.3
crowdsec_hostname: crowdsec01
crowdsec_description: Log Forwarder # default: CrowdSec
crowdsec_volume_name: crowdsec01_data # default: "{{ crowdsec_hostname }}"
crowdsec_data_dir: /usr/share/crowdsec # default: "/usr/share/{{ crowdsec_hostname }}"
crowdsec_bouncer_enabled: true # default: false
```

And include it in your playbook.

```yml
- hosts: crowdsec
  roles:
  - role: crowdsec
```

## Docs

### Show CrowdSec status

The crowdsec service runs in the container.

```bash
docker exec crowdsec01 cscli metrics show
```

### Show CrowdSec Firewall Bouncer status

The bouncer services runs on the host.

```bash
sudo systemctl status crowdsec-firewall-bouncer
```

Show log files.

```bash
sudo journalctl -u crowdsec-firewall-bouncer
```

Show ip table entry.

```bash
sudo iptables -L CROWDSEC_CHAIN
```
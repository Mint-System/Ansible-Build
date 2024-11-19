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
crowdsec_enroll_key: # default: "{{ vault_crowdsec_enroll_key }}
crowdsec_firewall_bouncer_enabled: true # default: false
crowdsec_firewall_bouncer_key: # default: "{{ vault_crowdsec_firewall_bouncer_key }}
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

### Install bouncer manually

Add apt signing key.

```bash
curl -fsSL https://packagecloud.io/crowdsec/crowdsec/gpgkey | gpg --dearmor > /etc/apt/keyrings/crowdsec_crowdsec-archive-keyring.gpg
```

Show release code name and add apt source.

```bash
CODENAME=$(lsb_release -cs)
vi /etc/apt/sources.list.d/crowdsec_crowdsec.list
```

The content of the list:

```
deb [signed-by=/etc/apt/keyrings/crowdsec_crowdsec-archive-keyring.gpg] https://packagecloud.io/crowdsec/crowdsec/ubuntu $CODENAME main
deb-src [signed-by=/etc/apt/keyrings/crowdsec_crowdsec-archive-keyring.gpg] https://packagecloud.io/crowdsec/crowdsec/ubuntu $CODENAME main
```

Install the firewall bouncer:

```bash
sudo apt update
sudo apt install crowdsec-firewall-bouncer-iptables
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
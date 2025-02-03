# CrowdSec Firewall Bouncer role

Deploy CrowdSec Firewall Bouncer.

## Usage

Configure the role.

```yml
# https://docs.crowdsec.net/u/bouncers/firewall/
crowdsec_firewall_bouncer_enabled: true # default: false
crowdsec_firewall_bouncer_mode: nftables # default: iptables
crowdsec_firewall_bouncer_api_url: https://sec.example.com/ # default: http://{{ crowdsec_hostname }}:8080/
crowdsec_firewall_bouncer_key: # default: "{{ vault_crowdsec_firewall_bouncer_key }}
```

And include it in your playbook.

```yml
- hosts: crowdsec
  roles:
  - role: crowdsec
```

## Docs

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

### Show content of whitelist configuration

Based on `crowdsec_whitelist_ip_addresses` the following file is generated:

```bash
cat /usr/share/crowdsec01/parsers/s02-enrich/01-my-whitelist.yaml
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

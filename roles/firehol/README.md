<img src="/logos/firehol.png" alt="firehol logo" width="100" height="100">

# FireHOL role

Setup FireHOL ip blacklists.

## Usage

Configure the role.

```yml
firehol_enabled: true # default: false
firehol_data_dir: /usr/share/firehol # default: /etc/firehol
```

And include it in your playbook.

```yml
- hosts: firehol
  roles:
  - role: firehol
```

## Docs

### Test ip blocklist

Check if host ip is in applied blacklist.

```bash
sudo iptables -S FIREHOL_BLACKLIST | grep "$(hostname -I | awk '{print $1}')"
sudo iptables -S FIREHOL_BLACKLIST | grep "216.21.8.0"
```

Check if iptable rules work.

```bash
IP="216.21.8.0/22"
sudo iptables -C FIREHOL_BLACKLIST -s $IP -j DROP && echo "Blocked" || echo "Not blocked"
```

### Chain does not exists

If you get the following error:

```
iptables v1.8.4 (nf_tables): Chain 'FIREHOL_BLACKLIST' does not exist
Try `iptables -h' or 'iptables --help' for more information.
```

You have to create the table manually

```bash
sudo iptables -N FIREHOL_BLACKLIST
```
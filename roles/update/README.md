---
kind: environment
---

<img src="/logos/update.png" alt="update logo" width="100" height="100">

# Update role

Install system and package updates.

The Ansible Update role supports these package managers:

* apt
* yum
* zypper
* dnf

## Usage

Configure the role.

```yml
update: true
reboot_allowed: true
```

And include it in your playbook.

```yml
- hosts: update
  roles:
  - role: update
```

## Troubleshooting

### InRelease repo expired

**Problem**

When running the update task it fails with this message:

```
msg: 'Failed to update apt cache: E:Release file for http://security.debian.org/debian-security/dists/bullseye-security/InRelease is expired (invalid since 1d 9h 4min 35s). Updates for this repository will not be applied., E:Release file for http://mirror.hetzner.com/debian/security/dists/bullseye-security/InRelease is expired (invalid since 1d 9h 4min 35s). Updates for this repository will not be applied.'
```

Or this one:

```
'Failed to update apt cache: E:Release file for http://security.debian.org/dists/bullseye-security/InRelease is expired (invalid since 2d 9h 0min 12s). Updates for this repository will not be applied.'
```

**Workaround**

Use the archive repo.

```bash
sudo su
cp /etc/apt/sources.list /etc/apt/sources.list.bak
sed -i 's|deb http://security.debian.org/debian-security|#deb http://security.debian.org/debian-security|' /etc/apt/sources.list
echo "deb http://archive.debian.org/debian-security bullseye-security main contrib non-free" >> /etc/apt/sources.list
echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/10no-check-valid-until
apt update
apt upgrade
apt autoremove
```

**Solution**

Upgrade the distro.
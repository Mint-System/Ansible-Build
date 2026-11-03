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

Optionally move the apt package cache to another directory. This is useful if `/var/cache/apt/archives` is on a small partition.

```yml
update_apt_cache_dir: /mnt/sdb/tmp/apt
```

The role creates the directory and writes the `Dir::Cache::archives` setting to `/etc/apt/apt.conf.d/99cache-dir`. Set the var to `""` (default) to remove this config.

And include it in your playbook.

```yml
- hosts: update
  roles:
  - role: update
```

## Troubleshooting

### Not enough free space in apt cache

**Problem**

When running the update task it fails with this message:

```
msg: '/usr/bin/apt-get upgrade --with-new-pkgs ' failed: E: You don't have enough free space in /var/cache/apt/archives/.
```

**Solution**

Set `update_apt_cache_dir` to a directory on a partition with enough free space.

```yml
update_apt_cache_dir: /mnt/sdb/tmp/apt
```

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
---
commit_ref: ad9e36c5996fe8921157ce366779611dd0625cc6
title: "Support changing apt cache dir"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: completed
date_completed: 2026-11-03
harness: pi
provider: deepseek
model: deepseek-v4-1-flash-1017
input_tokens: 61109
output_tokens: 7166
---

# Support changing apt cache dir

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task

Add a new var to `role/update` that allows changing the apt chache dir. Currently I have this issue:

```bash
fatal: [geras]: FAILED! =>
    changed: false
    msg: |-
        '/usr/bin/apt-get upgrade --with-new-pkgs ' failed: E: You don't have enough free space in /var/cache/apt/archives/.
    rc: 100
    stdout: |-
        Reading package lists...
        Building dependency tree...
        Reading state information...
        Calculating upgrade...
        The following packages were automatically installed and are no longer required:
          libfwupd2 libslirp0 slirp4netns
        Use 'sudo apt autoremove' to remove them.
        The following NEW packages will be installed:
          libfwupd3 libllvm19 linux-firmware-amd-graphics linux-firmware-amd-misc
          linux-firmware-broadcom-wireless linux-firmware-intel-graphics
          linux-firmware-intel-misc linux-firmware-intel-wireless
          linux-firmware-marvell-prestera linux-firmware-marvell-wireless
          linux-firmware-mediatek linux-firmware-mellanox-spectrum linux-firmware-misc
          linux-firmware-netronome linux-firmware-nvidia-graphics
          linux-firmware-qlogic linux-firmware-qualcomm-graphics
          linux-firmware-qualcomm-misc linux-firmware-qualcomm-wireless
          linux-firmware-realtek linux-headers-7.0.0-42-generic
          linux-hwe-7.0-headers-7.0.0-42 linux-hwe-7.0-tools-7.0.0-42
          linux-image-7.0.0-42-generic
          linux-main-modules-v4l2loopback-7.0.0-42-generic
          linux-main-modules-zfs-7.0.0-42-generic linux-modules-7.0.0-42-generic
          linux-tools-7.0.0-42-generic
        The following packages will be upgraded:
          fwupd linux-firmware linux-generic-hwe-24.04 linux-headers-generic-hwe-24.04
          linux-image-generic-hwe-24.04
        5 upgraded, 28 newly installed, 0 to remove and 0 not upgraded.
        Need to get 905 MB of archives.
        After this operation, 511 MB of additional disk space will be used.
    stdout_lines: <omitted>
```

The `/mnt/sdb/tmp` would be suitable target. Also not sure if the ansible apt role supports this.


@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

Added the `update_apt_cache_dir` var to the `update` role. The Ansible `apt` module has no parameter for the archive cache dir, so the role configures it through `/etc/apt/apt.conf.d/99cache-dir` with `Dir::Cache::archives`.

Changes:

- `roles/update/defaults/main.yml`: new var `update_apt_cache_dir: ""`.
- `roles/update/tasks/update_apt.yml`: create the cache dir, write the apt config file and remove the config file again if the var is empty. These tasks run before the cache update and upgrade.
- `roles/update/README.md`: usage example and a troubleshooting entry for the "not enough free space" error.

Verification:

- `./task lint`: no new findings (only pre-existing warnings in the role).
- Playbook run on localhost with `update_apt_cache_dir: /tmp/apt-cache-test`: dir created as `root:root 755`, config rendered as `Dir::Cache::archives "/tmp/apt-cache-test";` with `root:root 644`, second run idempotent (`changed=0`), removal branch deletes the file.
- Not tested against a real Debian/Ubuntu host, because the local machine runs Arch Linux.

Example config for the reported host:

```yml
update: true
update_apt_cache_dir: /mnt/sdb/tmp/apt
```

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count.

---
title: "add frontmatter kind to role readmes."
---

# Run 11

Note: @Agent refers to the AI agent (you) who is working on this task.

@Agent when working on this task, make sure to:

- Read context and task section first
- Prepare a list of todos
- Update the todo list while working on the task

## Context

Read the `AGENTS.md` and `README.md` to get an understanding of the project.

## Task

I want to add a kind attribute to every `roles/*/README.md` file.

Every role can be either a: application, service, environment


Example: `roles/systemd/README.md`

```
---
kind: environment
---

<img src="/logos/systemd.png" alt="systemd logo" width="100" height="100">

# systemd role
...
```

Please add the frontmatter to every README.

## Worklog

**Completed:** Added `kind` frontmatter to all 107 role README.md files with 4 categories.

**Classification breakdown:**

| Category | Count | Description |
|----------|-------|-------------|
| **system** | 18 | OS runtime infrastructure (docker, k3s, networking, firewall, certificates) |
| **environment** | 20 | OS configuration (systemd, packages, timezone, locale, users, etc.) |
| **service** | 38 | Middleware/supporting services (databases, monitoring, proxies, message queues) |
| **application** | 31 | End-user applications (odoo, wordpress, nextcloud, bookstack, etc.) |

**system roles:** acme_sh, autossh, certbot, crowdsec_firewall_bouncer, dind, docker, docker_compose, docker_hosts, docker_network, docker_swarm, docker_volume, firehol, infomaniak, innernet, k3s, resolv, ufw, vercel

**environment roles:** ansible_scripts, cargo, cleanup, cron, etc_hosts, fail2ban, fstab, git, iam, locale, maintenance, motd, packages, rclone, restic, s3cmd, ssh, systemd, timezone, update

**Example:**
```yaml
---
kind: system
---

<img src="/logos/docker.png" alt="docker logo" width="100" height="100">
```
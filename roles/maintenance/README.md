<img src="/logos/maintenance.png" alt="maintenance logo" width="100" height="100">

# Maintenance role

Maintains operating system and disk space.

## Usage

Configure the role.

```yml
maintenance: true # default: false
maintenance_job: true # default: false
```

And include it in your playbook.

```yml
- hosts: maintenance
  roles:
  - role: maintenance
```

## Docs

### Cleanup Docker system

Run this command to remove any unused containers, images, networks and caches.

```bash
docker system prune
```

Then run this command ro remove unattached volumes.

```bash
docker volume prune -a
```
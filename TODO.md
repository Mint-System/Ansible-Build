# TODO

## Bugs

## Container Management

- [ ] Migrate postgres02 `data` folder
- [ ] Manage all stores in volumes? files to volumes and database to host?

## Monitoring

- [ ] Setup fluentd and grep docker logs for errors

## Security

- [ ] Ignore XSS rule for wiki
      https://wiki.mint-system.ch/books/infrastruktur/page/container
      or increase score to 10
      Ignore rule for this host
- [ ] Check audit log and enforce engine
- [ ] Describe backup/recover scenario

## Nginx role

- [ ] Renew certs automatically
- [x] Skip waiting for cert request if not certs are required

## Backup

- [ ] Backup data folders to external system with restic and remote storage

## All roles

## Bookshelf role

- [ ] Connect to ldap

## Nextcloud role

- [ ] Connect to ldap

## Postgres role

# DONE

- [x] SSL check
- [x] Setup waf - docker nginx with modescurity and owasp crs https://hub.docker.com/r/owasp/modsecurity
- [x] Remove server_names variable
- [x] Ensure all assets are persisted
- [x] Update documentation with persisted folder
- [x] Configure email
- [x] Configure email
- [x] Enable multi db deployment https://dev.to/bgord/multiple-postgres-databases-in-a-single-docker-container-417l
- [x] Odoo postgres playbook uses wiki group_vars
- [x] Odoo fails to start if data folder is persisted `odoo docker PermissionError: [Errno 13] Permission denied: '/var/lib/odoo/sessions'` -> use volume
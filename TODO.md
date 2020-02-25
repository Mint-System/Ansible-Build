# TODO

## Bugs

- [ ] Odoo postgres playbook uses wiki group_vars
- [x] Odoo fails to start if data folder is persisted `odoo docker PermissionError: [Errno 13] Permission denied: '/var/lib/odoo/sessions'` -> use volume

## Container Management

- [ ] Migrate postgres02 data folder
- [ ] Manage all stores in volumes? filse to volumes and database to host?

## Monitoring

- [ ] Setup fluentd and grep docker logs for errors

## Security

- [ ] Describe recovery scenario
- [x] SSL check
- [ ] Setup waf - docker nginx with modescurity and owasp crs https://hub.docker.com/r/owasp/modsecurity

## Nginx role

- [x] Remove server_names variable
- [ ] Skip waiting for cert request if not certs are required
- [ ] Renew certs automatically

## Backup

- [ ] Backup data folders to external system

## All roles

- [x] Ensure all assets are persisted
- [x] Update documentation with persisted folder

## Bookshelf role

- [ ] Connect to ldap
- [x] Configure email

## Nextcloud role

- [ ] Connect to ldap
- [x] Configure email

## Postgres role

- [x] Enable multi db deployment https://dev.to/bgord/multiple-postgres-databases-in-a-single-docker-container-417l
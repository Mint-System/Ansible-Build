# TODO

## Bugs

- [ ] Nginx role does not purge unused conf files -> ssl fail -> create list of managed files read files wich are not in list and remove them
- [ ] ansible does not abort if certbot fails
- [ ] Nginx cert works if containers are removed and nginx folder is purged.

## Odoo role

- [ ] Setup erp.mint-system.ch and odoo.mint-system.ch
- [ ] Filter dbs false
- [ ] Auto install base module

## Container Management

- [ ] Migrate data to docker volumes? https://docs.docker.com/storage/ Ansible config must be mounted

## Monitoring

- [ ] Setup fluentd and grep docker logs for errors

## Security

- [ ] Remove vault files?
- [ ] Describe backup/recover scenario

## Nginx role

- [ ] Renew certs automatically

## Backup

- [ ] Backup data folders to external system with restic and remote storage

## Management

- [ ] Lint Ansible roles
- [ ] Reduce config duplicates -> hades and apland are similar -> simple odoo installations

# DONE

- [-] Cannot obtain new LetsEncrypt Certificates
- [x] Odoo and postgres cannot be installed at once
- [x] Postgres database creates new db -> remove multi db script
- [x] Setup new odoo server and migrate data
- [x] Migrate postgres02 `data` folder
- [x] Allow jpg upload https://github.com/Mint-System/Ansible-Playbooks/issues/1
- [x] Fine tune the security rules -> Make sense of inbound and outbound, anomaly and paranoia, etc. https://www.modsecurity.org/CRS/Documentation/anomaly.html
- [-] Document Ansible Deployment
- [x] Document ansible roles
- [-] Connect to ldap
- [-] Connect to ldap
- [x] Skip waiting for cert request if not certs are required
- [x] Ignore XSS rule for wiki
      https://wiki.mint-system.ch/books/infrastruktur/page/container
      or increase score to 10
      Ignore rule for this host
- [x] Check audit log and enforce engine
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
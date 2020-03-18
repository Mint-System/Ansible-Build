# TODO

## Update

- [ ] Update nextcloud to 18.0.2 and document procedure

## Bugs

- [ ] If docker is updated all hosts are stopped -> pin versions
- [ ] Nginx role does not purge unused conf files -> ssl fail -> create list of managed files read files wich are not in list and remove them 

## Odoo role

- [ ] Setup forum for OpenEdu
- [ ] Enable odoo apps installation from zip and tar.gz url -> Install report for apland
- [ ] Auto install base module

## Server

- [ ] Install dotfiles on all server

## Container Management

- [ ] Migrate wiki data to volumes (postgres, mysql, nextcloud, bookstack)!

## Monitoring

- [ ] Setup fluentd and grep docker logs for errors -> Install on hades

## Security

- [ ] Describe backup/recover scenario

## Nginx role

- [ ] Renew certs automatically -> add cron job

## Backup

- [ ] Backup data folders to external system with restic and remote storage https://linuxize.com/post/how-to-setup-automatic-odoo-backup/
- [ ] Setup client and integrate into existing playbook
- [ ] Test recover scenario

## Management

- [ ] Lint and document Ansible roles
- [ ] Only run role if image is configured
- [ ] Rename mint system network to mint-system.com (mint-system.com)

## New Roles

- [ ] Keycloak with user database and oauth integration
- [ ] Monitoring with Elastic, kibana, beats and fluentd

## Maintenance

- [ ] delete www database on odoo01

# DONE

- [x] Transfer all zones to now zeit
- [x] Setup server
- [x] Setup backup server
- [x] Setup www redirect
- [x] Remove vault files? -> not sure
- [-] Migrate data to docker volumes? https://docs.docker.com/storage/ Ansible config must be mounted
- [x] Filter dbs false
- [x] Setup Website, E-Learning and OpenEdu and filter db based on hostname dbfilter = ^%d$
- [-] If odoo is restarted, the db manager password is reseted -> not sure if true
- [x] Harden Nextcloud https://cloud.mint-system.ch/settings/admin/overview#version
- [-] Setup erp and export to odoo.mint
- [x] Nginx cannot start cerbot container when proxy config is not overwritten -> Add tmp container to docker network
- [-] ansible does not abort if certbot fails
- [x] Setup erp.mint-system.ch and odoo.mint-system.ch
- [x] Reduce config duplicates -> hades and apland are similar -> simple odoo installations
- [x] Nginx cert works if containers are removed and nginx folder is purged. RES: Increased time to 60 seconds
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
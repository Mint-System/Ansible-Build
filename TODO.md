# TODO

## Conference

- [ ] BigBlueButton Ansible role
- [ ] Upgrade Jitsi server

## Update

- [ ] Update nextcloud to 18.0.2 and document procedure
- [ ] Update ubuntu packages

## Analytics

- [ ] Integrate fathom snippet into meet.mint-system.ch

## Nextcloud

- [ ] Create Ansible template for config.php

## Bugs

- [ ] openeduca.ch not able to upload pngs
- [ ] Nginx role does not purge unused conf files -> ssl fail -> create list of managed files read files wich are not in list and remove them

## Odoo role

- [ ] Enable odoo apps installation from zip and tar.gz url -> Install report for apland
- [ ] Auto install base module
- [ ] Activate mail for self registrations
- [ ] Checkout mail gateway

## Proxy

- [ ] Add caching options for odoo websites

## Server

- [ ] Enable profile dotfiles: https://github.com/janikvonrotz/dotfiles
- [ ] Install fzf on all server -> ansible download and extract binary

## Monitoring


- [ ] Disable rule sets for elastic -> performance is horrible
- [ ] Monitoring with 
  - [x] Elastic, 
  - [x] kibana, 
  - [ ] beats, 
  - [x] logstash
- [-] Setup fluentd and grep docker logs for errors -> Install on hades
- [ ] Logstash cannot authenticate with the logstash_system user https://www.elastic.co/guide/en/logstash/current/ls-security.html
- [ ] Enalbe monitoring of cluster https://www.elastic.co/guide/en/elasticsearch/reference/7.6/collecting-monitoring-data.html
  - [ ] Output data to two clusters
- [ ] Setup mail watcher for disk space, memory and cpu usage

## Security

- [ ] Setup hashicorp vault for managing server secrets
- [ ] Scan ports
- [ ] Describe backup/recover scenario

## Nginx role

- [ ] Renew certs automatically -> add cron job

## Backup

- [ ] Setup backup for all volumes on all hosts
- [ ] Test recover scenario
- [ ] Check if backup rotation works
- [ ] Create backup type for odoo backups

## Management

- [x] Add github action badge
- [ ] Generate docs with ansible-doc
- [ ] Rename mint system network to mint-system.com (mint-system.com)

## New Roles

- [ ] Keycloak with user database and oauth integration https://hub.docker.com/r/jboss/keycloak/ account.mint-system.ch with OICD

## Maintenance

- [ ] Delete postgres02_delete and mysql01_delete on zeus
- [ ] Remove bookstack_delete folder on zeus
- [ ] Remove nextcloud01 folder on zeus
- [ ] delete openedu database on odoo02
- [ ] delete www database on odoo01

# DONE

- [x] Set alias for servers
- [x] Migrate wiki data to volumes (postgres, mysql, nextcloud, bookstack)! https://stackoverflow.com/questions/49888014/move-docker-bind-mount-to-volume
  - [x] Nextcloud
  - [-] BookStack volume mount not possible
  - [x] mysql
  - [x] postgres
- [x] Lint and document Ansible roles
- [x] Set restart policy always
- [x] integrate openedu.mint-system.ch, https://analytics.google.com
- [-] Deploy roles to localhost. Create host_vars localhost.yml und group_vars dev group. Start with odoo01 and proxy.
- [x] Backup data folders to external system with restic and remote storage https://linuxize.com/post/how-to-setup-automatic-odoo-backup/
- [x] Only run role if image is configured
- [x] Enable proxy mode for odoo https://www.odoo.com/documentation/13.0/setup/deploy.html#https
- [-] Setup forum for OpenEdu
- [x] Remove root login
- [x] Setup dedicated users and groups -> iam
- [x] If docker is updated all hosts are stopped -> pin versions
- [x] fathom analytics on hera
- [x] Restarting odoo docker forgets about it master passwords -> maybe setting admin_passwd helps -> yes work -> set pw -> save config -> get hash -> store pw and hash in inventory
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
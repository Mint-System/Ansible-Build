# TODO

## Business

- [ ] Setup eliasarnold.mint-system.ch on a separate instance

## Conference

- [ ] Change logo for jitsi and bbb

## Update

- [ ] Update nextcloud to 18.0.2 and document procedure
- [ ] Update ubuntu packages
- [ ] Update Odoo and apps

## Quality

- [ ] Start container task must show hostname -> only one task is shown for multiple targets
- [ ] Show container for clean tasks

## Identity

- [ ] Combine keycloack and nextcloud

## Analytics

- [ ] Integrate google dashboard in openeduca

## Bugs

- [ ] eCommerce Plugin installation breaks odoo -> maybe english support -> no -> it worked in local env

## Odoo

- [ ] Install openeduca blog system

## Server

- [ ] User scoped packages
- [ ] Install fzf on all server -> ansible download and extract binary

## Monitoring

- [ ] Configure mail
- [ ] Propertly provision prometheus datasource
- [ ] Configure dashboard
- [ ] Setup alertmanager (with Dashboard?)
- [ ] Notify via Telegram

## Security

- [ ] Enable modsecurity for grafana dashboard
- [ ] Do not expose postgres port by default
- [ ] Ignore ARGS:html for /books request api ,\
        ctl:ruleRemoveTargetById=932100-932999;!ARGS:html
- [ ] Setup user and run container with it for every role? 
- [ ] Protect access to cAdvisor and node-exporter -> docker overlay network
- [ ] Scan ports and block with firewall

## Nginx role

- [ ] Renew certs automatically -> add cron job
- [ ] Do not create cert for redirect adresses
- [ ] Ping cname before adding config

## Backup

- [ ] Extend odoo backup restore script with odoo backup and restore commands
- [ ] Backup type sql dump (for mysql and postgres) -> expose dbs locally?
- [ ] Test recover scenario
- [ ] Check if backup rotation works
- [ ] Document backup and recover scenario

## Maintenance

- [ ] Delete odoo database on apollo 
- [ ] Remove domain analytics.mint-system.ch
- [ ] Delete postgres02_delete and mysql01_delete on zeus
- [ ] Remove bookstack_delete folder on zeus
- [ ] Remove nextcloud01 folder on zeus
- [ ] delete openedu database on odoo02
- [ ] delete www database on odoo01

## Backlog

- [ ] Deploy jitsi with Docker
- [ ] Enable profile dotfiles: https://github.com/janikvonrotz/dotfiles
- [ ] Monitor proxy audit log
- [ ] Setup hashicorp vault for managing server secrets
- [ ] New roleDocker cleanup, prune images
- [ ] Monitor websites with https://github.com/prometheus/blackbox_exporter/blob/master/README.md -> on every node install probe -> use proxy addresses
- [ ] Manage prom exporter in Docker Swarm for enclosed networking -> https://docs.ansible.com/ansible/latest/modules/docker_swarm_module.html -> checkout overlay network https://docs.docker.com/network/overlay/
- [ ] Test roles with molecule
- [ ] CI/CD that installs roles

# DONE

- [-] openeduca.ch not able to upload pngs -> increase file upload size -> set global config
- [x] Deploy cpu und threading conf
- [x] Centralize application profile exclusion rules
- [-] Project inventories to configure everything
- [-] Install jibri and enable recording?
- [x] nextcloud02 hostname is mapped to wrong ip on hades -> restart proxy
- [x] Nextcloud Demo-Umgebung
- [x] Create Ansible template for config.php -> or update lines
- [x] Keycloak with user database and oauth integration https://hub.docker.com/r/jboss/keycloak/ account.mint-system.ch with OICD
- [-] Verify odoo database before backup
- [x] Enable odoo apps installation from zip and tar.gz url -> Install report for apland
- [x] Configure odoo backup for all installations
- [x] Delete all docker networks mint-system.net
- [x] Create backup type for odoo backups
- [-] Upgrade Jitsi server to cx41
- [-] Integrate fathom snippet into meet.mint-system.ch
- [-] Auto install base module
- [-] Activate mail for self registrations
- [-] Checkout mail gateway
- [-] Add caching options for odoo websites
- [-] Generate docs with ansible-doc
- [x] Rename mint system network to mint-system.com (mint-system.com)
- [x] Montor with Prometheus and Docker https://github.com/vegasbrianc/prometheus/
- [x] Setup backup for all volumes on all hosts
- [x] Set jitsi config -> https://community.jitsi.org/t/30-participants-experience/23358/2
- [x] Setup cAdvisor
- [x] Setup node-exporter
- [x] Setup prometheus
- [x] Setup grafana
- [x] BigBlueButton Ansible role
- [x] Nginx role does not purge unused conf files -> ssl fail -> create list of managed files read files wich are not in list and remove them
- [x] Nextcloud file upload size increase
- [-] Disable rule sets for elastic -> performance is horrible
- [-] Monitoring with 
  - [x] Elastic, 
  - [x] kibana, 
  - [-] beats, 
  - [x] logstash
- [-] Setup fluentd and grep docker logs for errors -> Install on hades
- [-] Logstash cannot authenticate with the logstash_system user https://www.elastic.co/guide/en/logstash/current/ls-security.html
- [-] Enalbe monitoring of cluster https://www.elastic.co/guide/en/elasticsearch/reference/7.6/collecting-monitoring-data.html
  - [-] Output data to two clusters
- [-] Setup mail watcher for disk space, memory and cpu usage
- [x] Add github action badge
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
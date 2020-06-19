# TODO

## BigBlueButton

- [ ] TURN Server bereitsellen
- [ ] Install bbb exporter https://github.com/greenstatic/bigbluebutton-exporter
- [ ] Configure nginx role -> map the *.nginx files and include them in the config

## Wordpress

- [ ] Configure sendmail

## Odoo

- [ ] Install etherpad https://github.com/ether/etherpad-lite/blob/develop/doc/docker.md or use pad.odoo.com
- [ ] OAuth access for existing users (not portal users) -> update guides
- [ ] Disable autoinstall 'auto_install': False, (True) -> Fix Ansible task to not reboot -> disable in modules?
- [ ] Update to Odoo 13.2?

## Update

- [ ] Update ubuntu packages -> patch management with Ansible -> check if first reboot also does not work manually -> pin versions ony if version is specified -> update servers -> start with kronos -> boot still hangs -> might be acpi options from grub? -> manuell reboot also does not work -> once reboot has been reseted it works!
  - [ ] hades
  - [ ] zeus -> ensure backup for realm exists!
  - [x] kronos
  - [x] atlas
  - [x] apollo
  - [x] eris
  - [x] hera
- [ ] Package upgrader -> if versions do not match, unpin package
- [ ] Update Odoo and apps -> show db names 1.0.1
- [ ] Update Bookstack to 0.29
- [ ] upgrade nginx images -> basic group -> nginx 1.19

## Identity

- [ ] Allow all kind of redirect uris for odoo.mint-system.ch realm
  - [ ] Remove demo clients from odoo.mint-system.ch client

## Bugs

- [ ] Oauth cookie bypass
- [ ] restic client password leak
- [ ] OAuth not working on mobile browsers -> same for odoo.com, worked on safari on ios pinned page
- [ ] eCommerce Plugin installation breaks odoo -> maybe english support -> no -> it worked in local env -> rebuild?

## Server

- [ ] install fzf
- [ ] Add package uninstall option! -> remove bat -> change config format with name and state

## Nextcloud

- [ ] Configure backup jobs

## Monitoring

- [ ] Test disk full alert
- [ ] Setup blackbox exporter https://github.com/prometheus/blackbox_exporter
- [ ] Setup nextcloud exporter https://github.com/xperimental/nextcloud-exporter

## Security

- [ ] Ignore ARGS:html for /books request api 
        ctl:ruleRemoveTargetById=932100-932999;!ARGS:html
- [ ] Setup user and run container with it for every role? 

## Backup

- [ ] check backups
- [ ] Test recover scenario; restore from zip works! -> check sql files -> nextcloud02
- [ ] Check if backup rotation works
- [ ] Document backup and recover scenario
- [ ] Backup keycloak realms

## Maintenance

- [ ] remove studio odoo apps in erp.mint-system.ch
- [ ] Delete blatthirsch database -> cleanup script for unmanged dbs?

# BACKLOG

- [ ] Prometheus scaper confige -> automate from Ansible group exporter
- [ ] Generate ansible documentation -> ansible-doc?
- [ ] See meta role https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#role-dependencies
- [ ] Unifiy how packages are installed -> include install.yml from central apt role
- [ ] Configure oauth with keycloak for grafana -> https://community.grafana.com/t/grafana-generic-oauth-with-keycloak/9692
- [ ] Log backups state with logger
- [ ] Configure only selected owasp crs range for configs
- [ ] Add odoo app disable option like with the cron jobs
- [ ] Scan ports and block with firewall
- [ ] Monitoring Notify via Telegram
- [ ] Remove obsolete odoo apps -> pruge unapplied module folds
- [ ] Add icons to odoo apps with mint theme
- [ ] Odoo package registry with npm and github registry
- [ ] pgadmin4 docker container serve under /pgadmin -> locations path /pgadmin
- [ ] Enable profile dotfiles: https://github.com/janikvonrotz/dotfiles
- [ ] Monitor proxy audit log
- [ ] Setup hashicorp vault for managing server secrets
- [ ] New role Docker cleanup, prune images
- [ ] Monitor websites with https://github.com/prometheus/blackbox_exporter/blob/master/README.md -> on every node install probe -> use proxy addresses
- [ ] Manage prom exporter in Docker Swarm for enclosed networking -> https://docs.ansible.com/ansible/latest/modules/docker_swarm_module.html -> checkout overlay network https://docs.docker.com/network/overlay/
- [ ] Test roles with molecule
- [ ] CI/CD that installs roles

# DONE

- [x] Docker packages use package role to install its packages -> include role and override packages
- [x] Test PATH update for crontab -> did not work! -> fixed -> all paths were required
- [x] Configure meta/main.yml dependencies for all projects! See cadvisor and update playbooks
  - [x] node-exporter
  - [x] cadvisor
  - [x] restic-server
  - [x] nginx
  - [x] modsecurity
  - [x] iam
  - [x] package
  - [x] restic-client
  - [x] prometheus
  - [x] bigbluebutton
  - [x] odoo
  - [x] postgres
  - [x] moodle
  - [x] mysql
  - [x] bookstack
  - [x] elasticsearch
  - [x] fathom
  - [x] grafana
  - [x] keycloak
  - [x] logstash
  - [x] metricbeat
  - [x] kibana
  - [x] openldap
  - [x] wordpress
  - [x] collabora-code
  - [x] nextcloud
  - [x] docker-network
  - [x] ...
- [x] Setup defaults/main.yml for all `| default()` tags
- [x] Protect access to cAdvisor and node-exporter -> docker overlay network -> setup proxy with basic auth: https://bigbluebutton-exporter.greenstatic.dev/installation/bigbluebutton_exporter/ -> switch to this method!
- [x] Convert all scaper connections to https! Recreate all containers and ensure port is not exposed. Resetup grafana and prometheus. -> eris and hera not done yet -> no proxy config
- [x] User scoped packages, zsh, oh-my-zsh https://github.com/veggiemonk/ansible-ohmyzsh/blob/master/tasks/main.yml -> not possible as apt installs everything system wide -> add an option for default user shell
- [x] Install fzf on all server -> ansible download and extract binary -> debian 9+ and ubuntu 19 supported -> add intall-fzf and install-oh-my-zsh scripts. Then run them in user context with become_user option.
- [x] Install bat and zsh on all servers
- [x] Add license and code of conduct
- [x] Install odoo-scripts on localhost
- [x] Remove /etc/environment call for all cron jobs (shouldn't it be loaded by default?) -> run scripts with >> /var/log/cron.log 2>&1 and * * * * * then append logger
- [x] Extend odoo backup restore script with odoo backup and restore commands
- [-] Deploy jitsi with Docker
- [-] oAuth for openeduca.ch and schule-sisikon.ch -> with existing users
- [-] Greenlight persists recordings -> use bbb-records
- [x] Configure admin user and logo
- [x] Enable SAML for cloud.mint-system.ch and fix SAML for nextcloud demo!? -> https://docs.axway.com/bundle/APIManager_762_APIMgmtGuide_allOS_en_HTML5/page/Content/APIManagementGuideTopics/APIManager_SSO/c_saml_trouble.htm#invalid_requester_in_keycloak_page
- [x] cert renewal cron job not working -> remove the .
- [x] Configure dashboards
- [x] Setup alertmanager (with Dashboard?)
- [x] Password rest -> email verfication feature is broken -> redirect error
- [x] Enable /b redirect
- [-] Change logo and color for jitsi and bbb
- [x] Check mysql and postgres backup jobs
- [x] sql dump backup job does not work -> maybe @weekly changes behavior
- [x] Persist dashboards
- [x] Configure mail with env var
- [x] Propertly provision prometheus datasource -> not working
- [x] New collabora code role
- [x] Do not expose postgres port by default -> redeploy container
- [x] Remove index.php for Nextcloud from url -> redeploy like nextcloud.mint-system.ch; recreate did not help -> updated nextcloud container and it vanished
- [x] Update nextcloud to 18.0.4 and document procedure -> simply bump container and nextcloud will detect that there is an old config and upate accordingly.
- [x] Enable Password reset for realm -> enable option in real settings login
- [x] Odoo OAuth Login Enable for:
  - [x] erp.mint-system.ch
  - [x] erp.apland.ch
  - [x] www.mint-system.ch
  - [x] odoo.mint-system.ch
- [x] Add odoo scripts role with odoo-backup, odoo-restore and docker-odoo-install
- [x] Cleanup records for mint-system.ch -> set all as ALIAS
- [x] Configure incoming email
  - [x] erp.mint-system.ch (mint-system.ch)
  - [x] odoo.mint-system.ch
  - [x] erp.apland.ch
  - [x] Demo?
- [x] Blatthirsch ersetzen mit steinbock -> Referenz, remove db
- [-] Change logo and color erp
- [x] Ping cname before adding config -> or check if dns entry exists
- [x] Do not create cert for redirect adresses
- [x] Change logo and color for wiki and cloud
- [x] Check cert renewal
- [x] Enable modsecurity for grafana dashboard
- [-] max_cron_threads = 2 check -> not working for docker
- [-] Integrate google dashboard in openeduca
- [x] Protect client: https://stackoverflow.com/questions/54305880/how-can-i-restrict-client-access-to-only-one-group-of-users-in-keycloak -> enable -Dkeycloak.profile.feature.scripts=enabled
- [x] Create login account for mint system user admint
- [x] Rebuilt SAML and OAuth config
- [x] Rename keycloak db
- [x] Keycloak db dump is empty -> not saving anything
- [x] Prepare monday
- [-] Create docker-mysql-backup job
- [-] Odoo long polling does not work
- [-] Backup cannot target odoo04
- [x] Backup type sql dump (for mysql and postgres); multiple databases yes; backup non odoo dbs
- [-] Install openeduca blog system
- [x] Do not delete odoo dabase -> odoo has problems -> update env?
- [x] Cannot install odoo.mint-system.ch
- [x] Could not delete odoo on odoo02 database
- [x] odoo02 has wrong long polling port
- [x] Combine keycloak and nextcloud
- [x] Setup mail provider for Keycloak self portal
- [x] Delete odoo database on apollo and filestore
- [x] delete openedu database on odoo02 and filestore
- [x] delete www database on odoo01 and filestore
- [x] Renew certs automatically -> add cron job
- [x] Start container task must show hostname -> only one task is shown for multiple targets
- [x] Show container for clean tasks
- [x] SAML Keycloak login
- [x] Remove bookstack_delete folder on zeus
- [x] Remove nextcloud01 folder on zeus
- [x] Delete postgres02_delete and mysql01_delete on zeus
- [x] Remove domain analytics.mint-system.ch
- [x] Delete mysql01 and mysql01_delete folder
- [x] Setup eliasarnold.mint-system.ch on a separate instance
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
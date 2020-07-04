# TODO

## BigBlueButton

- [ ] TURN Server bereitsellen
- [ ] Configure nginx role -> map the *.nginx files and include them in the config

## Odoo

- [ ] OAuth access for existing users (not portal users) -> update guides
- [ ] Update to Odoo 13.2?
- [ ] Check odoo apps dependencies before copying

## Update

- [ ] Check if package latest update method works for Ubuntu
- [ ] Package upgrader -> if versions do not match, unpin package
- [ ] Update Bookstack to 0.29
- [ ] upgrade nginx images -> basic group -> nginx 1.19 -> all others

## Bugs

- [ ] Cannot issue multiple certificates
- [ ] Configure CentOS package pinning and system updates
- [ ] Oauth cookie bypass
- [ ] restic client password leak
- [ ] OAuth not working on mobile browsers -> same for odoo.com, worked on safari on ios pinned page

## Server

- [ ] install fzf
- [ ] Add package uninstall option! -> remove bat -> change config format with name and state

## Monitoring

- [ ] Test disk full alert -> alert triggered once

## Security

- [ ] Ignore ARGS:html for /books request api 
        ctl:ruleRemoveTargetById=932100-932999;!ARGS:html

## Backup

- [ ] Test recover scenario; restore from zip works! -> check sql files -> nextcloud02
- [ ] Check if backup rotation works
- [ ] Document backup and recover scenario
- [ ] Automatically enable backup -> when creating docker volume -> autoregister a backup job for volumes. -> new module docker-volume and include the a task from restic-client.

## Maintenance

- [ ] remove studio odoo apps in erp.mint-system.ch
- [ ] Delete blatthirsch database -> cleanup script for unmanged dbs?

# BACKLOG

- [ ] Setup user and run container with it for every role?
- [ ] Install etherpad https://github.com/ether/etherpad-lite/blob/develop/doc/docker.md or use pad.odoo.com
- [ ] Mail dev für Mail-Tests Odoo
- [ ] Prometheus scaper config -> automate from Ansible group exporter
- [ ] Generate ansible documentation -> ansible-doc?
- [ ] Configure oauth with keycloak for grafana -> https://community.grafana.com/t/grafana-generic-oauth-with-keycloak/9692
- [ ] Configure only selected owasp crs range for configs
- [ ] Add odoo app disable option likwise with the cron jobs
- [ ] Scan ports and block with firewall
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
- [ ] Install bbb exporter https://github.com/greenstatic/bigbluebutton-exporter
- [ ] Setup blackbox exporter https://github.com/prometheus/blackbox_exporter
- [ ] Setup nextcloud exporter https://github.com/xperimental/nextcloud-exporter

# DONE

- [x] Create app bundles for odoo
- [x] Disable autoinstall 'auto_install': False, (True) -> Fix Ansible task to not reboot -> disable in modules?
  - [x] web_enterprise-13.0.1.0.zip
  - [x] web_mobile-13.0.1.0
  - [x] mail_enterprise-13.0.0.0
  - [x] web_grid-13.0.0.1
  - [x] timesheet_grid-13.0.1.0
  - [x] web_gantt-13.0.2.0
  - [x] mrp_maintenance-13.0.1.0
  - [x] quality_mrp-13.0.1.0.zip
  - [x] quality_mrp_workorder-13.0.1.0.zip
- [x] python3-passlib is only available for centos8! -> workaround added
- [x] Configure CentOS package pinning and system updates
- [x] See meta role https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#role-dependencies
- [x] Unifiy how packages are installed -> include install.yml from central apt role
- [x] Log backups state with logger
- [-] Monitoring Notify via Telegram
- [-] Backup keycloak realms -> db backup is fine
- [x] eCommerce Plugin installation breaks odoo -> maybe english support -> no -> it worked in local env -> rebuild? -> works
- [x] Allow all kind of redirect uris for odoo.mint-system.ch realm
  - [x] Remove demo clients from odoo.mint-system.ch client
- [x] Update ubuntu packages -> patch management with Ansible -> check if first reboot also does not work manually -> pin versions ony if version is specified -> update servers -> start with kronos -> boot still hangs -> might be acpi options from grub? -> manuell reboot also does not work -> once reboot has been reseted it works!
  - [x] hades
  - [x] zeus -> ensure backup for realm exists!
  - [x] hermes
  - [x] kronos
  - [x] atlas
  - [x] apollo
  - [x] eris
  - [x] hera
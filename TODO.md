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
- [ ] If odoo server is restarted it might change ip and therefore won't be reachable by nginx

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


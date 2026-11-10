---
commit_ref:
title: "Nextcloud wait on upgrade"
author: "Janik von Rotz <login@janikvonrotz.ch>"
action: implement
state: draft
date_completed: YYYY-MM-DD
harness:
provider:
model:
input_tokens:
output_tokens:
---

# Nextcloud wait on upgrade

Note: @Clanker refers to the "ai agent" (you) who is working on this prompt file.

@Clanker when working on this prompt file, make sure to:

- Read the `AGENTS.md` and `README.md` to get an understanding of the project
- Read entire task section and prepare a list of todos
- Update the todo list while working on task

## Task

To update Nextcloud I update the `nextcloud_image` in the inventory and run this command:

```bash
task play -i inventories/mint_system plays/nextcloud.yml -t nextcloud --limit apollo_nextcloud
```

When I get to `Info about upgrade` I abort the deployment.

```bash
TASK [nextcloud : Info about upgrades] ********************************************************************************
ok: [apollo_nextcloud] =>
    msg: When Nextlcoud upgrade is running, abort the task. The upgrade process will most
        likely take more time than 30 seconds.
Pausing for 30 seconds
(ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)

```

Then I watch the Nextcloud upograde scripts on the server until its finished:

```
[apollo ~]$ docker logs nextcloud03 -f
=> Configuring PHP session handler...
==> Using Redis as PHP session handler...
Initializing nextcloud 33.0.10.1 ...
Upgrading nextcloud from 32.0.15.1 ...
=> Searching for hook scripts (*.sh) to run, located in the folder "/docker-entrypoint-hooks.d/pre-upgrade"
==> Skipped: the "pre-upgrade" folder is empty (or does not exist)
Setting log level to debug
Turned on maintenance mode
Updating database schema
Updated database
Disabled incompatible app: gpxpod
Disabled incompatible app: richdocuments
Updating <federation> ...
Updated <federation> to 1.23.0
Updating <lookup_server_connector> ...
Updated <lookup_server_connector> to 1.21.0
Updating <oauth2> ...
Updated <oauth2> to 1.21.0
Updating <password_policy> ...
Updated <password_policy> to 5.0.0
Updating <photos> ...
Updated <photos> to 6.0.0
Updating <activity> ...
Updated <activity> to 6.0.0
Updating <circles> ...
Updated <circles> to 33.0.0
Updating <cloud_federation_api> ...
Updated <cloud_federation_api> to 1.17.0
Updating <dav> ...
Fix broken values of calendar objects

 Starting ...

Clean up old calendar subscriptions from deleted users that were not cleaned-up

    0/0 [>---------------------------]   0% Starting ...

Updated <dav> to 1.36.1
Updating <files> ...
Updated <files> to 2.5.0
Updating <files_sharing> ...
Updated <files_sharing> to 1.25.2
Updated <files_trashbin> to 1.23.0
Updating <files_versions> ...
Updated <files_versions> to 1.26.0
Updating <sharebymail> ...
Updated <sharebymail> to 1.23.0
Updating <webhook_listeners> ...
Updated <webhook_listeners> to 1.5.0
Updating <workflowengine> ...
Updated <workflowengine> to 2.15.0
Updating <comments> ...
Updated <comments> to 1.23.0
Updating <logreader> ...
Updated <logreader> to 6.0.0
Updating <nextcloud_announcements> ...
Updated <nextcloud_announcements> to 5.0.0
Updating <notifications> ...
Updated <notifications> to 6.0.0
Updating <systemtags> ...
Updated <systemtags> to 1.23.0
Updating <theming> ...
Updated <theming> to 2.8.0
Updating <app_api> ...
Updated <app_api> to 33.0.0
Updating <bruteforcesettings> ...
Updated <bruteforcesettings> to 6.0.0
Updating <contactsinteraction> ...
Updated <contactsinteraction> to 1.14.1
Updating <dashboard> ...
Updated <dashboard> to 7.13.0
Updating <federatedfilesharing> ...
Updated <federatedfilesharing> to 1.23.0
Updating <files_downloadlimit> ...
Updated <files_downloadlimit> to 5.1.0
Updating <files_pdfviewer> ...
Updated <files_pdfviewer> to 6.0.0
Updating <files_reminders> ...
Updated <files_reminders> to 1.6.0
Updating <firstrunwizard> ...
Updated <firstrunwizard> to 6.0.0
Updating <privacy> ...
Updated <privacy> to 5.0.0
Updating <profile> ...
Updated <profile> to 1.2.0
...
Updated <text> to 7.0.1
Updating <twofactor_backupcodes> ...
Updated <twofactor_backupcodes> to 1.22.0
Updating <updatenotification> ...
Updated <updatenotification> to 1.23.0
Updating <user_status> ...
Updated <user_status> to 1.13.0
Updating <viewer> ...
Updated <viewer> to 6.0.0
Updating <weather_status> ...
Updated <weather_status> to 1.13.0
Update app calendar from App Store
Update app contacts from App Store
Update app forms from App Store
Update app news from App Store
Update app gpxpod from App Store
Update app richdocuments from App Store
Starting code integrity check...
Finished code integrity check
Update successful
Turned off maintenance mode
Resetting log level
=> Searching for hook scripts (*.sh) to run, located in the folder "/docker-entrypoint-hooks.d/post-upgrade"
==> Skipped: the "post-upgrade" folder is empty (or does not exist)
Initializing finished
Warning: /var/www/html/config/apps.config.php differs from the latest version of this image at /usr/src/nextcloud/config/apps.config.php
Warning: /var/www/html/config/redis.config.php differs from the latest version of this image at /usr/src/nextcloud/config/redis.config.php
Warning: /var/www/html/config/reverse-proxy.config.php differs from the latest version of this image at /usr/src/nextcloud/config/reverse-proxy.config.php
Warning: /var/www/html/config/s3.config.php differs from the latest version of this image at /usr/src/nextcloud/config/s3.config.php
Warning: /var/www/html/config/smtp.config.php differs from the latest version of this image at /usr/src/nextcloud/config/smtp.config.php
Warning: /var/www/html/config/upgrade-disable-web.config.php differs from the latest version of this image at /usr/src/nextcloud/config/upgrade-disable-web.config.php
=> Searching for hook scripts (*.sh) to run, located in the folder "/docker-entrypoint-hooks.d/before-starting"
==> Skipped: the "before-starting" folder is empty (or does not exist)
    0/0 [->--------------------------]   0%AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.18.0.6. Set the 'ServerName' directive globally to suppress this message
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 172.18.0.6. Set the 'ServerName' directive globally to suppress this message
[Tue Nov 10 17:02:40.190659 2026] [mpm_prefork:notice] [pid 1:tid 1] AH00163: Apache/2.4.69 (Debian) PHP/8.4.27 configured -- resuming normal operations
[Tue Nov 10 17:02:40.190758 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'apache2 -D FOREGROUND'
```

This takes more than 30 seconds.

Once the script finishes I rerun the Ansible deployment to apply the default config.

Instead of aborting I would like the deployment to wait for the upgrade to finish. I think it should check for the maintenance mode and wait until the container turns maintenance mode off.

Can you update the role `roles/nextcloud/tasks/nextcloud.yml` to do this?

### Testing

I will test it myself by running the nextcloud update for `hades_nextcloud`.

@Clanker When task is completed set frontmatter state to review. Prompt the author to verify the results.

## Worklog

@Clanker Add a summary here once the task has been completed.

@Clanker If author confirms results set frontmatter state to completed, otherwise to aborted. Update date, harness, provider and model. If you have access to session info also add token count. Finally, update the changelog with the most important changes.

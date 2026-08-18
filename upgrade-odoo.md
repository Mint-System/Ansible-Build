# Upgrade Odoo

The Odoo Build project assists you in running upgrades for any Odoo project. This document provides a highly opinionated way to connect Odoo Build with an existing Odoo enviroment and execute the upgrade.

### Requirements

Running the upgrade requires scripts on the servers. Ensure that the following scripts are installed on the server:

- <https://ansible.build/scripts.html#docker> provides generic Docker container commands
- <https://ansible.build/scripts.html#odoo> helps managing the Odoo container
- <https://ansible.build/scripts.html#postgres> supports managing the Postgres container

## Setup

Odoo Build provies task file commands that take `env` as an argument. The `env` is reference to the name of a dotenv file (`inventories/dotenv/.env.$NAME`). These files are managed with `*-dotenv` commands.

Setting up a Odoo upgrade project requires the creation of a dotenv file. This guide assumes that we have the following case:

- Our customer is `Acme Corporation`
- The production server is `host1.example.com` and the upgrade server is `host2.example.com`
- Odoo 16.0 production instance is running at `https://odoo.example.com`
- Odoo 18.0 upgrade environment is running at `https://upgrade.odoo.example.com`
- The Odoo setup is docker based. The Postgres containers have a different version
- Name of Odoo databases depends on the subdomain of the url

Get started by creating the `inventories/dotenv/` folder.

```bash
task init-dotenv-dir
```

Then create a dotenv file for the upgrade project.

```bash
task create-env acme upgrade
```

This will create the file with the upgrade template. Edit the file.

```bash
task edit-env acme
```

Update the configs with the definition of your enviroment.

First we have the source environment:

- `HOST`: Hostname of the Odoo pruction instance
- `SERVER`: SSH url to access the pruction server
- `PORT`: SSH port of server
- `JUMP_HOST`: SSH jump host
- `ODOO_CONTAINER`: Name of production Odoo Docker container
- `ODOO_VERSION`: Version of Odoo production
- `POSTGRES_CONTAINER`: Name of production Postgres Docker container
- `DATABASE`: Name of production database

Then we have the target enviroment:

- `TARGET_HOST`: Hostname of the Odoo upgrade instance.
- `TARGET_SERVER`: SSH url to access the upgrade server
- `TARGET_PORT`: SSH port of server
- `TARGET_JUMP_HOST`: SSH jump host
- `TARGET_ODOO_CONTAINER`: Name of upgrade Odoo Docker container
- `TARGET_ODOO_VERSION`: Version of Odoo upgrade
- `TARGET_POSTGRES_CONTAINER`: Name of upgrade Postgres Docker container
- `TARGET_DATABASE`: Name of upgrade database

In our case the definition is:

```bash
HOST='odoo.example.com'
SERVER='host1.example.com'
PORT=22
ODOO_CONTAINER='odoo01'
ODOO_VERSION='16.0'
POSTGRES_CONTAINER='postgres01'
DATABASE='odoo'

TARGET_HOST='upgrade.odoo.example.com'
TARGET_SERVER='host2.example.com'
TARGET_PORT=22
TARGET_ODOO_CONTAINER='odoo02'
TARGET_ODOO_VERSION='18.0'
TARGET_POSTGRES_CONTAINER='postgres02'
TARGET_DATABASE='upgrade'
```

Note that the `HOST` and `TARGET_HOST` is a reference to another dotenv file.

You can show the upgrade information with `task upgrade-odoo amce info`.

## Test Run

Before going live with an upgraded Odoo database, the new enviroments needs to be tested thoroughly . An upgrade run copies the production database and runs the Odoo Enterprise Upgrade or the Odoo OpenUpgrade scripts in test mode. On sucess a neutralized and upgraded database will be ready for testing.

### Execute

List the steps with `task upgrade-odoo list`. Here are the details for each step:

**dump-database**

Dump and restore the production database on the Postgres container.

```bash
task upgrade-odoo acme dump-database
```

**dump-filestore**

Export and import the Odoo filestore.

```bash
task upgrade-odoo acme dump-filestore
```

**drop-database**

Drop the existing upgrade database.

```bash
task upgrade-odoo acme drop-database
```

**upgrade-test**

Run the Odoo Enterprise Upgrade scripts in test mode. This will neutralize the database after an upgrade.

```bash
task upgrade-odoo acme upgrade-test
```

**openupgrade-test**

Run the Odoo OpenUpgrade scripts. This will neutralize the database after an upgrade.

```bash
task upgrade-odoo acme openupgrade-test
```

**clear-assets**

Clear Odoo assets.

```bash
task upgrade-odoo acme clear-assets
```

**init**

Init modules on the upgraded database.

This step requires an env var: `ODOO_ADDONS_INIT=web_environment_ribbon`

```bash
task upgrade-odoo acme init
```

**uninstall**

Uninstall modules on the upgraded database.

This step requires an env var: `ODOO_ADDONS_UNINSTALL=board_user_acl,l10n_din5008_expense`

```bash
task upgrade-odoo acme uninstall
```

**auto-update**

Calls the `upgrade_changed_checksum` method.

```bash
task upgrade-odoo acme auto-update
```

**update**

Update all modules and clear assets.

```bash
task upgrade-odoo acme update
```

**configure-test**

Run custom Python code in Odoo shell.

This step requires an env var: `ODOO_CONFIGURE_TEST="env.ref('mail.ir_cron_module_update_notification').write({'active': False})"`

```bash
task upgrade-odoo acme configure-test
```

**restart**

Restart target Odoo and Postgres container.

```bash
task upgrade-odoo acme restart
```

### Troubleshooting

At any point the upgrade process can fail and requires investigating. There are additional commands that help troubleshooting the issues:

**list-databases**

List databases in source and target Postgres container.

```bash
task upgrade-odoo acme list-databases
```

**logs**

Show log of target Odoo container.

```bash
task upgrade-odoo acme logs
```

**shell**

Start Odoo shell in target container.

```bash
task upgrade-odoo acme shell
```

**psql**

Start psql shell in target Postgres container.

```bash
task upgrade-odoo acme psql
```

**env**

Show env vars of the target Odoo container.

```bash
task upgrade-odoo acme env
```

**conf**

Show odoo.conf of the target Odoo container.

```bash
task upgrade-odoo acme conf
```

### Configure

With every Odoo release Odoo introduces new features and enhancements, but also deprecates features and ways of doing. If you have a heavily customized Odoo database and many features enabled, more things are bound to break in the upgrade process.

In the configuration of the upgrade process you are fixing Odoo features that cannot be automated with code. Create a list of steps to make configurations in Odoo.

### Testing

The testing of an upgraded Odoo database is done in collaboration of the Odoo partner and the customer. The partner defines test cases that verify the customer's workflows. Feedback is collected and feedback loop for testing, documenting, bugfixing and restarting the upgrade process is established.

Repeat the feedback loop until you are confident that the upgraded works well. Do not aim for 100% test coverage. Minor issues can be resolved in the post-production-upgrade-phase.

## Production Run

Once the testing phase of the upgrade project has finished and a date for the go-live has been chosen, you are reay for the production upgrade. This basically mans to execute the upgrade in production mode on the date of the go-live.

The goals is that production url `https://odoo.example.com` points to the container with upgraded Odoo database.

### Execute

**upgrade-production**

Run the Odoo Enterprise Upgrade scripts in production mode. This will **not** neutralize the database after an upgrade.

```bash
task upgrade-odoo acme upgrade-production
```

**openupgrade-production**

Run the Odoo OpenUpgrade scripts. This will **not** neutralize the database after an upgrade.

```bash
task upgrade-odoo acme openupgrade-test
```

**configure-production**

Run custom Python code in Odoo shell.

This step requires an env var: `ODOO_CONFIGURE_PRODUCTION="env.ref('mail.ir_cron_module_update_notification').write({'active': True})"`

```bash
task upgrade-odoo acme configure-production
```

### Configure

Once the production enviroment is ready, execute the the manual configuration steps as you did for the test enviroment.

### Testing

Run simple smoke tests. Ensure that the upgrade wenn well. There is no need to execute the test cases.

### Rename

Until here it is still possible to abort the go-live. To go-live means to rename the target database to the original database name and ensure that `https://odoo.example.com` points to the target environment. Use this command to rename:

**rename-database**

Rename target database to source name.

```bash
task upgrade-odoo acme rename-database
```

As the final step, update DNS records and/or proxy configuration so that `https://odoo.example.com` points to `host2.example.com`.

### Restore

Insead of renaming the target database, you can also restore the database and filestore into the source enviroment. This makes sense if you want to deploy the upgraded database to `host1.example.com`. And instead of updating the DNS records and/or proxy configuration, you replace the Odoo production instance with the definitions of the uprade instance.

**restore-database**

Restore source database from target databases.

```bash
task upgrade-odoo acme restore-database
```

The existing source database will be renamed to `${DATABASE}-old`.

**restore-filestore**

Restore source filestore from target filestore.

```bash
task upgrade-odoo acme restore-filestore
```

The existing source filestore will be renamed to `${DATABASE}-old`.

### Recovery

If something goes wrong after the go-live, fallback to the old environment. Simply revert the DNS update and/or the proxy configuration.

### Cleanup

After a week of working successfully with the upgraded database, it is safe to sunset the original server and/or Odoo enviroment.

In our example this means shutting down the `odoo01` container and the `host1.example.com` server.

Ensure that `https://upgrade.odoo.example.com` no longer resolves.

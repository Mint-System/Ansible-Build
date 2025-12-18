<img src="/logos/nextcloud.png" alt="nextcloud logo" width="100" height="100">

# Nextcloud role

Deploy Nextcloud Docker container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/_/nextcloud/
nextcloud_image: nextcloud:32-apache
nextcloud_build_image: true # default: false
nextcloud_hostname: nextcloud01
nextcloud_data_dir: /usr/share/nextcloud # default: "/usr/share/{{ nextcloud_hostname }}"
nextcloud_volume_name: nextcloud_data01 # default: "{{ nextcloud_hostname}}"
nextcloud_volume_backup_set: # See restic_backup_set var in role restic
nextcloud_domain: nextcloud.example.com
nextcloud_trusted_domains: nextcloud.example.com # default: "{{ nextcloud_domain }}"
nextcloud_admin_user: admin
nextcloud_admin_password: # default: "{{ vault_nextcloud_admin_password }}"
nextcloud_postgres_hostname: postgres01
nextcloud_postgres_user: nextcloud # default: "{{ postgres_user }}"
nextcloud_postgres_password: # default: "{{ vault_postgres_password }}"
nextcloud_postgres_db: nextcloud
nextcloud_mail_hostname: mail.example.com
nextcloud_mail_encryption: tls # default: ""
nextcloud_mail_port: "587"
nextcloud_mail_from: noreply@example.com # default: ""
nextcloud_mail_username: bot@example.com # default: ""
nextcloud_mail_password: "{{ vault_nextcloud_mail_password }}"
nextcloud_redis_hostname: redis01
nextcloud_redis_password: "{{ vault_nextcloud_redis_password }}"
nextcloud_etc_hosts: # defaults: {}
  "doc.example.com": 10.42.5.2
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: nextcloud
```

## Docs

### Nginx config

Setup this Nginx configuration for the `nextcloud01` host:

```yaml
  - src_hostname: cloud.example.com
    dest_hostname: nextcloud01
    dest_port: 80
    tls: true
    monitor: /login
    options: |
      include /etc/nginx/conf.d/proxy-params.conf;
      location /.well-known/carddav {
        return 301 $scheme://$host:$server_port/remote.php/dav;
      }
      location /.well-known/caldav {
        return 301 $scheme://$host:$server_port/remote.php/dav;
      }
      add_header Strict-Transport-Security "max-age=15552000; includeSubDomains" always;
      client_max_body_size 512M;
```

### Use MySQL/MariaDB database

Configure these vars to make a connection to a MySQL/MariaDB database:

```yaml
nextcloud_mysql_hostname: mysql01
nextcloud_mysql_user: nextcloud # default: "{{ mysql_user }}"
nextcloud_mysql_password: # default: "{{ vault_mysql_password }}"
nextcloud_mysql_db: nextcloud
```

### Add Redis config manually

In case the Redis container is deployed after Nextcloud has been initated, the config below must be added to the `config.php` to enable Redis caching.

```php
'memcache.distributed' => '\OC\Memcache\Redis',
'memcache.locking' => '\OC\Memcache\Redis',
'redis' => [
     'host' => 'nextcloud_redis_hostname',
     'password' => 'nextcloud_redis_password',
     'port' => 6379,
],
```

### Build manually

Copy the build files with Ansible.

Build with Docker.

```bash
cd /srv/build/nextcloud01
docker build . -t nextcloud:nextcloud01
```

### Debug an internal server error

When Nextcloud is throwing an *Internal Server Error* without details in the log, run the occ cli to get details on the issue.

```bash
docker exec --user www-data nextcloud01 php occ
```

### Exit maintenance mode

Disable the maintenance mode with the occ cli.

```bash
ansible host.example.com -m shell -a 'docker exec --user www-data {{ nextcloud_hostname }} php occ maintenance:mode --off' -i inventories/nextcloud
```

### Cleanup trashbin

Cleanup the deleted files and folders for all users.

```bash
ansible host.example.com -m shell -a 'docker exec --user www-data {{ nextcloud_hostname }} php occ trashbin:cleanup --off' -i inventories/nextcloud
```

### Migrate mimetypes

```bash
ansible host.example.com -m shell -a 'docker exec --user www-data {{ nextcloud_hostname }} php occ maintenance:repair --include-expensive' -i inventories/nextcloud
```

### Get session settings

Retrieve the session settings with these commands:

```bash
docker exec --user www-data nextcloud01 php occ config:system:get session_keepalive
docker exec --user www-data nextcloud01 php occ config:system:get session_lifetime
docker exec --user www-data nextcloud01 php occ config:system:get remember_login_cookie_lifetime
```

### Enable/disable user account

Use the `occ` cli to disable/enable accounts.

```bash
docker exec --user www-data nextcloud01 php occ user:disable admint
docker exec --user www-data nextcloud01 php occ user:enable admint
```
# Nextcloud role

Deploy Nextcloud Docker container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/nextcloud/
nextcloud_image: nextcloud:27-apache
nextcloud_build_image: true # default: false
nextcloud_hostname: nextcloud01
nextcloud_volume_name: nextcloud_data01 # default: "{{ nextcloud_hostname}}"
nextcloud_volume_backup_set: # See restic_backup_set var in role restic_client
nextcloud_domain: nextcloud.example.com
nextcloud_trusted_domains: nextcloud.example.com # default: "{{ nextcloud_domain }}"
nextcloud_admin_user: admin
nextcloud_admin_password: "{{ vault_nextcloud_admin_password }}"
nextcloud_postgres_hostname: postgres01
nextcloud_postgres_user: nextcloud
nextcloud_postgres_password: "{{ vault_nextcloud_postgres_password }}"
nextcloud_postgres_db: nextcloud
nextcloud_mail_hostname: mail.example.com
nextcloud_mail_encryption: tls
nextcloud_mail_port: "587"
nextcloud_mail_from: noreply@example.com
nextcloud_mail_username: bot@example.com
nextcloud_mail_password: "{{ vault_nextcloud_mail_password }}"
nextcloud_redis_hostname: redis01
nextcloud_redis_password: "{{ vault_nextcloud_redis_password }}"
nextcloud_integrity_check: true # default: false
```

And include it in your playbook.

```yml
- hosts: nextcloud
  roles:
  - role: nextcloud
```

## Docs

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
docker build . -t nextcloud:custom
```
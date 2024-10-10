# PHP-FPM role

Deploy PHP-FPM container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/php
php_fpm_image: php:8.3.1-fpm
php_fpm_build_image: true # default: false
php_fpm_hostname: php01
php_fpm_description: Moodle # default: PHP-FPM
php_fpm_volume_name: php_data01 # default: "{{ php_fpm_hostname }}"
php_fpm_volumes:
  - moodle01:/var/www/moodledata # default: - "{{ php_fpm_volume_name }}:/var/www/html"
  - /usr/share/php01/moodle:/var/www/html
php_fpm_env: # default: {}
  MOODLE_USERNAME: moodle
```

And include it in your playbook.

```yml
- hosts: php_fpm
  roles:
  - role: php_fpm
```

## Docs

### Nginx config

Setup this PHP-FPM configuration for the `php01` host:

```yaml
nginx_http_options: |
  map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
  }
nginx_proxies:
  - src_hostname: moodle.example.com
    dest_hostname: php01
    dest_port: 8069
    options: |
      include /etc/nginx/conf.d/proxy-params.conf;          
```
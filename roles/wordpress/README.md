# WordPress role

Deploy WordPress container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/_/wordpress
wordpress_image: wordpress:php7.4-apache
wordpress_hostname: word01
wordpress_description: WP # default: WordPress
wordpress_volume_name: word_data01 # default: "{{ wordpress_hostname }}"
wordpress_db_hostname: mysql01
wordpress_db_user: wordpress
wordpress_db_password: "{{ vault_wordpress_db_password }}"
wordpress_db_name: wordpress
```

And include it in your playbook.

```yml
- hosts: wordpress
  roles:
  - role: wordpress
```

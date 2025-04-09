<img src="/logos/redis.png" alt="redis logo" width="100" height="100">

# Redis role

Deploy Redis container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/_/redis
redis_image: redis:6.2.3
redis_description: cache for nextcloud # default: Redis
redis_hostname: redis01
redis_volume_name: redis_data01 # default: "{{ redis_hostname }}"
redis_password: # default: "{{ vault_redis_password }}"
```

And include it in your playbook.

```yml
- hosts: redis
  roles:
  - role: redis
```

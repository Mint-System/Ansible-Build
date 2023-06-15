# Docker Compose role

Deploy Docker Compose project.

## Usage

Configure the role.

**vars.yml**

```yml
docker_compose_project_name: project01
docker_compose_data_dir: /usr/share/compose01 # default: "/usr/share/{{ docker_compose_project_name }}"
docker_compose_volumes:
  - name: postgresql-vol
docker_compose_backup_set: # See restic_backup_set var in role restic_client
docker_compose_dotenv: |
  FRAPPE_VERSION: v13
  LETSENCRYPT_EMAIL: email@example.com
  POSTGRES_HOST=postgresql
  POSTGRES_PASSWORD=frappe
  SITE_NAME=mysite.localhost
  SITES=mysite.localhost
  POSTGRES_USER=postgres
  ADMIN_PASSWORD=frappe
docker_compose_definition: |
  version: '3'
  # https://github.com/frappe/frappe_docker/blob/develop/installation/frappe-postgresql/docker-compose.yml
  services:

    frappe-nginx:
      container_name: frappe-nginx
      image: frappe/frappe-nginx:${FRAPPE_VERSION}
      restart: on-failure
      environment:
        FRAPPE_PY: frappe-python
        FRAPPE_PY_PORT: 8000
        FRAPPE_SOCKETIO: frappe-socketio
        SOCKETIO_PORT: 9000
        LETSENCRYPT_HOST: ${SITES}
        VIRTUAL_HOST: ${SITES}
        LETSENCRYPT_EMAIL: ${LETSENCRYPT_EMAIL}
      ports:
        - "127.0.0.1:8080:80"
        - "127.0.0.1:8443:443"
      volumes:
        - sites-vol/:/var/www/html/sites:rw
        - assets-vol:/assets:rw

    frappe-python:
      container_name: frappe-python
      image: frappe/frappe-worker:${FRAPPE_VERSION}
      restart: on-failure
      environment:
        POSTGRES_HOST: ${POSTGRES_HOST}
        DB_PORT: 5432
        REDIS_CACHE: redis-cache:6379
        REDIS_QUEUE: redis-queue:6379
        REDIS_SOCKETIO: redis-socketio:6379
        SOCKETIO_PORT: 9000
        AUTO_MIGRATE: 1
      volumes:
        - sites-vol:/home/frappe/frappe-bench/sites:rw
        - logs-vol:/home/frappe/frappe-bench/logs:rw
        - assets-vol:/home/frappe/frappe-bench/sites/assets:rw

    frappe-socketio:
      container_name: frappe-socketio
      image: frappe/frappe-socketio:${FRAPPE_VERSION}
      restart: on-failure
      depends_on:
        - redis-socketio
      volumes:
        - sites-vol:/home/frappe/frappe-bench/sites:rw
        - logs-vol:/home/frappe/frappe-bench/logs:rw

    frappe-worker-default:
      container_name: frappe-worker-default
      image: frappe/frappe-worker:${FRAPPE_VERSION}
      restart: on-failure
      command: worker
      depends_on:
        - redis-queue
        - redis-cache
      volumes:
        - sites-vol:/home/frappe/frappe-bench/sites:rw
        - logs-vol:/home/frappe/frappe-bench/logs:rw

    frappe-worker-short:
      container_name: frappe-worker-short
      image: frappe/frappe-worker:${FRAPPE_VERSION}
      restart: on-failure
      command: worker
      environment:
        WORKER_TYPE: short
      depends_on:
        - redis-queue
        - redis-cache
      volumes:
        - sites-vol:/home/frappe/frappe-bench/sites:rw
        - logs-vol:/home/frappe/frappe-bench/logs:rw

    frappe-worker-long:
      container_name: frappe-worker-long
      image: frappe/frappe-worker:${FRAPPE_VERSION}
      restart: on-failure
      command: worker
      environment:
        WORKER_TYPE: long
      depends_on:
        - redis-queue
        - redis-cache
      volumes:
        - sites-vol:/home/frappe/frappe-bench/sites:rw
        - logs-vol:/home/frappe/frappe-bench/logs:rw

    frappe-schedule:
      container_name: frappe-schedule
      image: frappe/frappe-worker:${FRAPPE_VERSION}
      restart: on-failure
      command: schedule
      depends_on:
        - redis-queue
        - redis-cache
      volumes:
        - sites-vol:/home/frappe/frappe-bench/sites:rw
        - logs-vol:/home/frappe/frappe-bench/logs:rw

    redis-cache:
      container_name: redis-cache
      image: redis:latest
      restart: on-failure
      ports:
        - "127.0.0.1:6379:6379"
      volumes:
        - redis-cache-vol:/data

    redis-queue:
      container_name: redis-queue
      image: redis:latest
      restart: on-failure
      ports:
        - "127.0.0.1:6380:6379"
      volumes:
        - redis-queue-vol:/data

    redis-socketio:
      container_name: redis-socketio
      image: redis:latest
      restart: on-failure
      ports:
        - "127.0.0.1:6381:6379"
      volumes:
        - redis-socketio-vol:/data    

    postgresql:
      container_name: postgresql
      image: postgres:11.8
      restart: on-failure
      ports:
        - "127.0.0.1:5432:5432"
      environment:
        POSTGRES_USER: ${POSTGRES_USER}
        POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      volumes:
        - postgresql-vol:/var/lib/postgresql/data
          
    site-creator:
      container_name: site-creator
      image: frappe/frappe-worker:${FRAPPE_VERSION}
      restart: "no"
      command: new
      depends_on:
        - frappe-python
      environment:
        POSTGRES_HOST: ${POSTGRES_HOST}
        SITE_NAME: ${SITE_NAME}
        DB_ROOT_USER: ${POSTGRES_USER}
        POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
        ADMIN_PASSWORD: ${ADMIN_PASSWORD}
        INSTALL_APPS: ${INSTALL_APPS}
      volumes:
        - sites-vol:/home/frappe/frappe-bench/sites:rw

  volumes:
    logs-vol:
    sites-vol:
    assets-vol:
    redis-cache-vol:
    redis-queue-vol:
    redis-socketio-vol:
```

And include it in your playbook.

```yml
- hosts: docker_compose
  roles:
  - role: docker_compose
```

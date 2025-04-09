<img src="/logos/docker_compose.png" alt="docker_compose logo" width="100" height="100">

# Docker Compose role

Deploy Docker Compose project.

## Usage

Configure the role.

```yml
docker_compose_project_name: project01
docker_compose_data_dir: /srv/compose/compose01 # default: "/srv/compose/{{ docker_compose_project_name }}"
docker_compose_volumes:
  - name: postgresql-vol
docker_compose_backup_set: # See restic_backup_set var in role restic
docker_compose_dotenv: |
  POSTGRES_PASSWORD=postgres
docker_compose_definition:
  services:
    db:
      image: postgres
      volumes:
        - ./data/db:/var/lib/postgresql/data
      environment:
        - POSTGRES_DB=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=postgres
    web:
      image: django
      command: python -m http.server
      ports:
        - "8000:8000"
      environment:
        - POSTGRES_NAME=postgres
        - POSTGRES_USER=postgres
        - POSTGRES_PASSWORD=$POSTGRES_PASSWORD
      depends_on:
        - db
```

And include it in your playbook.

```yml
- hosts: docker_compose
  roles:
  - role: docker_compose
```

The following tags are available:

* docker_compose
* docker_compose_backup

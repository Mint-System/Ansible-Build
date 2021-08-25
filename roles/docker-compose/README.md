# Ansible Docker Compose role

Deploy Docker Compose project.

## Usage

Configure the role.

**vars.yml**

```yml
docker_compose_project_name: project01
docker_compose_data_dir: /usr/share/compose01 # default: "/usr/share/{{ docker_compose_project_name }}"
docker_compose_dotenv: |
  FRAPPE_VERSION: v13
  ETSENCRYPT_EMAIL: email@example.com
  POSTGRES_HOST=postgresql
  POSTGRES_PASSWORD=frappe
  SITE_NAME=mysite.localhost
  SITES=mysite.localhost
  DB_ROOT_USER=postgres
  ADMIN_PASSWORD=frappe
docker_compose_definition: |

```

And include it in your playbook.

```yml
- hosts: docker-compose
  roles:
  - role: docker-compose
```

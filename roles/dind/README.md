# dind role

Deploy Docker in Docker container.

## Usage

Configure the role.

```yml
# https://hub.docker.com/_/docker
dind_image: docker:24.0.5-dind
dind_description: Build Environment # default: Docker in Docker
dind_hostname: dind01
dind_env: # default: []
  DOCKER_TLS_CERTDIR: ""
dind_volumes: # default: []
  jenkins01:/var/jenkins_home
```

And include it in your playbook.

```yml
- hosts: dind
  roles:
  - role: dind
```

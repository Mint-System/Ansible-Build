# Jenkins role

Deploy Jenkins container.

## Usage

Configure the role.

**vars.yml**

```yml
# https://hub.docker.com/r/jenkins/jenkins
jenkins_image: jenkins/jenkins:2.416-jdk11
jenkins_build_image: true # default: false
jenkins_description: Continuous Integration and Delivery server # default: Jenkins
jenkins_hostname: jenkins01
jenkins_volume_name: jenkins_data01 # default: "{{ jenkins_hostname}}"
jenkins_user: admin
jenkins_password: # default: "{{ vault_jenkins_password }}"
jenkins_url: https://cd.example.com
jenkins_plugins: |
  oic-auth:latest
jenkins_docker_host: tcp://dind01:2375 # default: "unix:///var/run/docker.sock"
jenkins_casc: | # default: see defaults/main.yml
  securityRealm:
    local:
      allowsSignup: false
      users:
      - id: ${JENKINS_USER}
        password: ${JENKINS_PASSWORD}
  authorizationStrategy:
    globalMatrix:
      entries:
      - group:
          name: "authenticated"
          permissions:
          - "Overall/Read"
      - user:
          name: "${JENKINS_USER}"
          permissions:
          - "Overall/Administer"
  unclassified:
    location:
      url: ${JENKINS_URL}
```

And include it in your playbook.

```yml
- hosts: jenkins
  roles:
  - role: jenkins
```

## Docs

### Get app list from existing Jenkins server

Here is an example to get the list of plugins from an existing server:

```
JENKINS_HOST=username:password@myhost.com:port
curl -sSL "http://$JENKINS_HOST/pluginManager/api/xml?depth=1&xpath=/*/*/shortName|/*/*/version&wrapper=plugins" | perl -pe 's/.*?<shortName>([\w-]+).*?<version>([^<]+)()(<\/\w+>)+/\1 \2\n/g'|sed 's/ /:/'
```

Source: <https://github.com/jenkinsci/docker#usage-1>
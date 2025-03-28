FROM {{ jenkins_build_image }}

USER root

RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive \
apt-get install --no-install-recommends --assume-yes \
docker.io \
gettext \
jq \
rsync
  
USER jenkins

ENV JAVA_OPTS -Xmx512M -Djenkins.install.runSetupWizard=false

COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt

ENV CASC_JENKINS_CONFIG /usr/share/jenkins/ref/jenkins.yml

FROM {{ jenkins_build_image }}

USER root
RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive \
apt-get install --no-install-recommends --assume-yes \
docker.io
USER jenkins

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt

COPY casc.yml /var/jenkins_home/casc.yml
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yml
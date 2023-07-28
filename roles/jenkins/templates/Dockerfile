FROM {{ jenkins_build_image }}
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt

COPY casc.yml /var/jenkins_home/casc.yml
ENV CASC_JENKINS_CONFIG /var/jenkins_home/casc.yml
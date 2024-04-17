FROM {{ meilisync_image }}

USER root

RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive \
apt-get install --no-install-recommends --assume-yes \
docker.io gettext jq rsync

RUN curl -L \  
  "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" \  
  -o /usr/local/bin/docker-compose \  
  && chmod +x /usr/local/bin/docker-compose  

USER meilisync

ENV JAVA_OPTS -Xmx512M -Dmeilisync.install.runSetupWizard=false

COPY --chown=meilisync:meilisync plugins.txt /usr/share/meilisync/ref/plugins.txt
RUN meilisync-plugin-cli -f /usr/share/meilisync/ref/plugins.txt

ENV CASC_MEILISYNC_CONFIG /usr/share/meilisync/ref/meilisync.yml

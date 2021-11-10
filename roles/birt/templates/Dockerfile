FROM phusion/baseimage:0.9.18

ENV TERM=xterm LANG=en_US LC_CTYPE=en_US LC_TIME=de_CH LC_NUMERIC=de_CH LC_MONETARY=de_CH LC_MEASUREMENT=de_CH
COPY . /tmp/
RUN /tmp/setup

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8080
EXPOSE 8443
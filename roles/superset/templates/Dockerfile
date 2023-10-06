FROM {{ superset_build_image }}
USER root
RUN pip install psycopg2

COPY ./superset-init /superset-init
COPY superset_config.py /app/
ENV SUPERSET_CONFIG_PATH /app/superset_config.py

USER superset
ENTRYPOINT [ "/superset-init" ]
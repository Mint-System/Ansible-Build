FROM {{ postgres_build_image }}

{% if postgres_build_image == 'postgres:12' -%}
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-server-dev-all \
       postgresql-12-mysql-fdw \
    && rm -rf /var/lib/apt/lists/*
{% endif %}
{% if postgres_build_image == 'postgres:14' -%}
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-server-dev-all \
       postgresql-14-wal2json \
       postgresql-14-mysql-fdw \
    && rm -rf /var/lib/apt/lists/*
{% endif %}

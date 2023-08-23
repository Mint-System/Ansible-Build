FROM {{ keycloak_build_image }}

{% for item in keycloak_build_include %}
COPY .{{ item.dest }} {{ item.dest }}
{% endfor %}
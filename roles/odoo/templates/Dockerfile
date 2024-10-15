FROM {{ odoo_build_image }}

USER root

{% if odoo_build_pip_install %}
RUN python -m pip install {{ odoo_build_pip_install }}
{% endif %}

{% if odoo_build_apt_install %}
RUN apt-get update && apt-get install -y {{ odoo_build_apt_install }}
{% endif %}

USER odoo
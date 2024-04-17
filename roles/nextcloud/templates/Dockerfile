FROM {{ nextcloud_build_image }}
RUN apt update
RUN apt install -y smbclient libsmbclient-dev
RUN pecl install smbclient
RUN docker-php-ext-enable smbclient
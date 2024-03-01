FROM {{ php_fpm_build_image }}

# unfortunatly the official docker-php-ext-install command ran into problems installing eg. zip
# one solution was to use this unoffical docker-php-extension-installer script, which works!
ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/
# RUN docker-php-extension-install mysqli pdo pdo_mysql gd soap exif 

RUN chmod +x /usr/local/bin/install-php-extensions && \
    install-php-extensions mysqli pdo pdo_mysql gd soap exif intl zip opcache

COPY "./php.ini" "$PHP_INI_DIR/php.ini"

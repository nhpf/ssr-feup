FROM handsonsecurity/seed-server:apache-php
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y openssh-server  \
    && apt-get clean

COPY index.php /var/www/html/
COPY server_name.conf /etc/apache2/sites-available/
RUN rm /var/www/html/index.html && a2ensite server_name.conf

CMD service apache2 start && tail -f /dev/null

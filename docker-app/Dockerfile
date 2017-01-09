FROM ubuntu:14.04

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./conf/sources.list /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y python2.7 \
    && apt-get install -y uwsgi \
    && apt-get install -y python-pip \
    && apt-get install -y uwsgi-plugin-python \
    && apt-get install -y supervisor \
    && apt-get autoremove

# RUN mkdir -p /data/www
# COPY ./app/* /data/www/
# COPY ./conf/app.ini /etc/uwsgi/apps-enabled/app.ini
# COPY ./conf/app.conf /etc/supervisor/conf.d/app.conf

# CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/app.conf"]
CMD ["/bin/bash"]

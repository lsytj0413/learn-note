
FROM uwsgi:v1

RUN pip install flask

COPY ./app/* /data/www/
COPY ./conf/app.ini /etc/uwsgi/apps-enabled/app.ini
COPY ./conf/app.conf /etc/supervisor/conf.d/app.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/app.conf"]

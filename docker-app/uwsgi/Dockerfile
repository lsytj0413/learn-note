# 构建一个安装有uwsgi 和 supervisor 的镜像

FROM python:v2.7.12

RUN apt-get update \
    && apt-get install -y --no-install-recommends uwsgi \
               uwsgi-plugin-python \
               supervisor \
    && rm -rf /var/lib/apt/lists* \
    && mkdir -p /data/www


CMD ["/bin/bash"]

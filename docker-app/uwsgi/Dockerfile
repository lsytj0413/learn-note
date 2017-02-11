# 构建一个安装有uwsgi 和 supervisor 的镜像

# 基础镜像
FROM python:v2.7.12

# 安装uwsgi 和 supervisor
RUN apt-get update \
    && apt-get install -y --no-install-recommends uwsgi \
               uwsgi-plugin-python \
               supervisor \
    && rm -rf /var/lib/apt/lists* \
    && mkdir -p /data/www

# 启动命令
CMD ["/bin/bash"]

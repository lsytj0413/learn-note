# 构建一个flask app 示例镜像

# 基础镜像
FROM uwsgi:v1.0.0

# 拷贝源代码
COPY ./app/* /data/www/
COPY ./conf/app.ini /etc/uwsgi/apps-enabled/app.ini
COPY ./conf/app.conf /etc/supervisor/conf.d/app.conf

# 安装依赖包
WORKDIR /data/www
RUN pip install -r requirements.txt

WORKDIR /

# 启动命令
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/app.conf"]

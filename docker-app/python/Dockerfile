# 构建一个安装了Python以及pip的ubuntu14.04镜像

FROM ubuntu:14.04

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./conf/sources.list /etc/apt/sources.list

RUN mkdir /root/.pip
COPY ./conf/pip.conf /root/.pip/pip.conf

RUN apt-get update \
    && apt-get install -y python2.7 \
    && apt-get install -y python-pip \
    && apt-get autoremove \
    && apt-get autoclean

CMD ["/bin/bash"]

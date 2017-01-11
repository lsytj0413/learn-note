# 构建一个安装了Python以及pip的ubuntu16.04镜像

FROM ubuntu:16.04

RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./conf/sources.list /etc/apt/sources.list

RUN mkdir /root/.pip
COPY ./conf/pip.conf /root/.pip/pip.conf

RUN apt-get update \
    && apt-get install -y --no-install-recommends python2.7 \
               python-pip \
    # && apt-get remove --purge -y $(apt-mark showauto) \
    && pip install --upgrade pip \
    && pip install setuptools \
    && rm -rf /var/lib/apt/lists/*
    # && apt-get autoremove \
    # && apt-get autoclean \

CMD ["/bin/bash"]

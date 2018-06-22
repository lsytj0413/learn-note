# 构建一个安装了Python以及pip的ubuntu16.04镜像

# 基础镜像
FROM ubuntu:16.04

# 使用阿里云的UBUNTU源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./conf/sources.list /etc/apt/sources.list

# 使用阿里云pip源
RUN mkdir /root/.pip
COPY ./conf/pip.conf /root/.pip/pip.conf

# 安装python2.7.12以及pip
RUN apt-get update \
    && apt-get install -y --no-install-recommends python2.7 \
               python-pip \
    # && apt-get remove --purge -y $(apt-mark showauto) \
    && pip install --upgrade pip \
    && pip install -i https://mirrors.aliyun.com/pypi/simple setuptools \
    && rm -rf /var/lib/apt/lists/*
    # && apt-get autoremove \
    # && apt-get autoclean \

# 启动命令行
CMD ["/bin/bash"]

# 构建python2.7 镜像, 基础镜像系统为Ubuntu16.04
# 构建命令: docker build -t python:v2.7 .

# 基础镜像
FROM registry.cn-hangzhou.aliyuncs.com/soren/base:v16.04

# 作者
MAINTAINER sorenyang@foxmail.com

# 使用阿里云pip源
RUN mkdir /root/.pip
COPY ./pip.conf /root/.pip/pip.conf

# 安装python2.7.12以及pip
RUN apt-get update \
    && apt-get install -y --no-install-recommends python2.7 \
               python-pip \
    # && apt-get remove --purge -y $(apt-mark showauto) \
    && pip install --upgrade pip \
    && pip install setuptools \
    && rm -rf /var/lib/apt/lists/*
    # && apt-get autoremove \
    # && apt-get autoclean \

# 启动命令行
CMD ["/bin/bash"]
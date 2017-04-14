# 构建基镜像, 基础镜像版本为 ubuntu16.04
# 构建命令: docker build -t base:v16.04 .

# 基础镜像
FROM ubuntu:16.04

# 作者
MAINTAINER sorenyang@foxmail.com

# 使用阿里云的UBUNTU源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./sources.list /etc/apt/sources.list

# 更新包
RUN apt-get update \
    && apt-get -y --no-install-recommends upgrade \
    && rm -rf /var/lib/apt/lists/*

# 启动命令行
CMD ["/bin/bash"]
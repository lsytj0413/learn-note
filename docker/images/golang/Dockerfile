# 构建golang1.8 镜像, 基础镜像为 Ubuntu16.04

# 基础镜像
FROM ubuntu:16.04

# 作者
MAINTAINER soren

# 使用阿里云的UBUNTU源
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
COPY ./sources.list /etc/apt/sources.list

# 首先添加ppa源
# 然后安装golang1.8
RUN apt update \
    && apt install -y --no-install-recommends python-software-properties \
    && add-apt-repository -y ppa:longsleep/golang-backports \
    && apt-get update \
    && apt-get install -y --no-install-recommends golang-go \
    && rm -rf /var/lib/lists/* \
    && mkdir /go

# 设置环境变量
ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH

# 修改目录属性
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

# 设置工作目录
WORKDIR $GOPATH

# 启动命令行
CMD ["/bin/bash"]
# 构建golang1.8 镜像, 基础镜像系统为Ubuntu16.04
# 构建命令: docker build -t golang:v1.8 .

# 基础镜像
FROM registry.cn-hangzhou.aliyuncs.com/soren/base:v16.04

# 作者
MAINTAINER sorenyang@foxmail.com

# 首先添加ppa源
# 然后安装golang1.8
RUN apt-get update \
    && apt-get install -y --no-install-recommends software-properties-common \
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
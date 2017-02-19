# docker-app

docker-app是一个使用docker构建简单的python flask应用的实例.

例子包含三个部分, 包括构建一个python运行环境, 一个uwsgi运行环境, 再加上一个app运行镜像.

# 如何使用docker

docker是一个开源的应用容器引擎, 让开发者可以打包他们的应用以及依赖包到一个可移植的容器中, 然后发布到任何支持docker的机器上, 也可以实现虚拟化. 容器是完全使用沙箱机制, 相互之间不会有任何接口.

docker常用的命令介绍如下:

## 拉取镜像 ##

使用 **docker pull** 命令可以拉取镜像. 所有的docker容器都是以镜像的方式发布, 当镜像被运行起来之后就称为容器.

`
docker pull ubuntu:16.04
`


# 如何使用

## python

### 构建python镜像

cd python
docker build -t python:v2.7.12 .

### 查看镜像

docker images

### 执行镜像

docker run -it --rm python:v2.7.12 /bin/bash

### 停止容器

docker ps -a
docker stop <container id>

### 删除容器

docker rm <container id>

### 删除镜像

docker rmi <image id>

## uwsgi

### 构建uwsgi 镜像

cd uwsgi
docker build -t uwsgi:v1 .

## app

### 构建app镜像

cd app
docker build -t app:v1 .

### 运行app

docker run -p :8084:8084 app:v1

### 测试

wget http://localhost:8084
wget http://localhost:8084/hello

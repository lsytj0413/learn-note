# docker-app

docker-app是一个使用docker构建简单的python flask应用的实例.

例子包含三个部分, 包括构建一个python运行环境, 一个uwsgi运行环境, 再加上一个app运行镜像.

# 如何使用docker



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

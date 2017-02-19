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

## 查看镜像 ##

使用 **docker images** 命令可以查看本机上已经存在的镜像列表.

`
docker images
`

## 删除镜像 ##

使用 **docker rmi** 命令可以删除本机上已经存在的镜像.

删除单个镜像:

```
docker rmi <image ID>
```

或者删除所有名为 xxx 的镜像:

```
sudo docker rmi $(sudo docker image -q xxx)
```

## 启动容器 ##

使用 **docker run** 命令启动容器.

```
docker run ubuntu:16.04
```

使用 **-p** 参数进行端口映射, 使用 **-e** 端口设置环境变量, 使用 **-it** 参数通过命令行交互, 使用 **--rm** 参数在容器退出时自动删除.

## 查看运行中的容器 ##

使用 **docker ps** 命令查看运行中的容器.

```
docker ps -a
```

## 进入运行中的容器 ##

使用 **docker exec** 命令进入运行中的容器.

```
docker exec -it <container id> /bin/bash
```

## 停止容器 ##

使用 **docker kill** 命令停止运行中的容器.

```
docker kill <container id>
```

## 删除容器 ##

使用 **docker rm** 命令删除已经停止的容器.

删除单个容器:

```
docker rm <container ID>
```

或者删除所有的已停止容器:

```
sudo docker rm $(sudo docker ps -aq)
```

## 构建镜像 ##

使用 **docker build** 命令从 **Dockerfile** 构建镜像.

进入 **Dockerfile** 所在目录, 执行以下命令:

```
docker build -t ubuntu:16.04 .
docker tag <image ID> new:16.04
docker push new:16.04
```

例如通过以下命令使用阿里云docker仓库:

```
sudo docker tag b9f399c9b482 registry.cn-hangzhou.aliyuncs.com/rapself/fortest:v1.0.0
sudo docker login --username=tangying2729959 registry.cn-hangzhou.aliyuncs.com 
sudo docker push registry.cn-hangzhou.aliyuncs.com/rapself/fortest:v1.0.0
```

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

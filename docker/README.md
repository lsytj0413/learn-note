# Docker(moby) #

##  安装 ##

### 默认安装 ###

在 ubuntu16.04 TLS 环境下, 直接使用如下命令即可安装 Docker:

```
apt install docker.io
```

### 新版本安装 ###

采用默认安装的 Docker 可能不是最新的版本, 可以使用如下命令安装新版本的 Docker:

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
sudo apt update
# 安装 latest 版本的 docker-ce
sudo proxychains4 apt install docker-ce
# 获取 docker-ce 版本
sudo apt-cache madison docker-ce
# 安装特定版本的 docker-ce
apt install docker-ce=<version>
```

### 避免使用 sudo ###

docker 提供了一个 docker组, 只需要将用户加入 docker组, 然后再执行与 docker 相关的命令就不再需要使用 sudo.

```
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
```

## 代理 ##

举个例子, 假如需要通过 docker pull 获取一个 image, 但是此时需要使用代理, 那么需要进行如下操作:

```
sudo service docker stop
sudo HTTP_PROXY="127.0.0.1:8118" HTTPS_PROXY="127.0.0.1:8118" dockerd
```

即首先需要停止 docker deamon, 然后使用代理配置重新启动它.

## 如何使用docker ##

docker是一个开源的应用容器引擎, 让开发者可以打包他们的应用以及依赖包到一个可移植的容器中, 然后发布到任何支持docker的机器上, 也可以实现虚拟化. 容器是完全使用沙箱机制, 相互之间不会有任何接口.

docker常用的命令介绍如下:

### 拉取镜像 ###

使用 **docker pull** 命令可以拉取镜像. 所有的docker容器都是以镜像的方式发布, 当镜像被运行起来之后就称为容器.

`
docker pull ubuntu:16.04
`

### 查看镜像 ###

使用 **docker images** 命令可以查看本机上已经存在的镜像列表.

`
docker images
`

### 删除镜像 ###

使用 **docker rmi** 命令可以删除本机上已经存在的镜像.

删除单个镜像:

```
docker rmi <image ID>
```

或者删除所有名为 xxx 的镜像:

```
sudo docker rmi $(sudo docker images -q xxx)
```

或者删除所有为 <none> 的镜像:

```
docker rmi $(docker images -f "dangling=true" -q)
```

### 启动容器 ###

使用 **docker run** 命令启动容器.

```
docker run ubuntu:16.04
```

使用 **-p** 参数进行端口映射, 使用 **-e** 端口设置环境变量, 使用 **-it** 参数通过命令行交互, 使用 **--rm** 参数在容器退出时自动删除, 使用 **--name** 指定容器名称, 使用 **-d** 参数指定以 deamon 的方式启动容器, 使用 **--cpuset-cpus** 指定 CPU 限制.

### 查看运行中的容器 ###

使用 **docker ps** 命令查看运行中的容器.

```
docker ps -a
```

### 进入运行中的容器 ###

使用 **docker exec** 命令进入运行中的容器.

```
docker exec -it <container id> /bin/bash
```

### 停止容器 ###

使用 **docker kill** 命令停止运行中的容器.

```
docker kill <container id>
```

### 删除容器 ###

使用 **docker rm** 命令删除已经停止的容器.

删除单个容器:

```
docker rm <container ID>
```

或者删除所有的已停止容器:

```
sudo docker rm $(sudo docker ps -aq)
```

### 构建镜像 ###

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

# 参考资料 #

- [Docker简介与应用](./Docker简介与应用.pptx)
- [有关容器的三大路线之争](./有关容器的三大路线之争.pdf)

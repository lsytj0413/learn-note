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

## 避免使用 sudo ##

docker 提供了一个 docker组, 只需要将用户加入 docker组, 然后再执行与 docker 相关的命令就不再需要使用 sudo.

```
sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
```

# 内容分类

| 目录 | 描述 |
|:--|:--|
| python | 构建一个基于Ubuntu16.04 的python2.7.12 运行环境镜像 |
| uwsgi | 构建一个安装有 uwsgi 和 supervisor 的运行环境镜像 |
| app | 构建一个示例 flask app 运行镜像 |

# 其他内容 #

## uwsgi使用介绍 ##

1. 启动uwsgi

```
uwsgi xxx.ini
```

2. 停止uwsig

```
uwsgi --stop xxx.pid
```

## supervisor使用介绍 ##

1. 生成默认配置

```
echo_supervisord_config > app.conf
```

2. 增加应用的配置

```
[program:app]
command = /usr/bin/uwsgi --ini /etc/uwsgi/apps-enabled/app.ini
stopsignal=QUIT
autostart=true
autorestart=true
# stdout_logfile=/var/log/uwsgi/supervisor_app.log
# stderr_logfile=/dev/stdout

stdout_logfile=/dev/stdout
redirect_stderr=true
stdout_logfile_maxbytes=0
```

3. 其他

如果需要结合uwsgi使用, 则需要注释掉 uwsgi.conf 中的 daemonize.

如果需要结合docker使用, 则需要修改supervisor的以下配置项:

```
nodaemon=true                ; (start in foreground if true;default false)
```

## 使用python获取本机ip ##

```
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15])
    )[20:24])

print get_ip_address('eth1')
```

## etcd简介 ##

etcd是一个类似于 **zookeeper** 的分布式下的一致的键值存储服务. 可以用于分布式环境下的配置管理, 服务发现等.

## confd 使用示例 ##

confd是一个自动配置管理工具, 可用于微服务架构下的配置自动更新.

```
sudo ./confd -onetime -node=http://127.0.0.1:4001 -config-file=
/etc/confd/conf.d/nginx.toml -log-level debug
sudo ./confd -interval 10 -node http://127.0.0.1:4001 -config-file /etc/confd/conf.d/nginx.toml
curl -L "http://127.0.0.1:4001/v2/keys/app/app3" -XPUT -d value="127.0.0.1:4004"
curl -L "http://127.0.0.1:4001/v2/keys/app" -XPUT -d dir=true
curl -L "http://127.0.0.1:4001/v2/keys/app?recursive=true" -XDELETE
```

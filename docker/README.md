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

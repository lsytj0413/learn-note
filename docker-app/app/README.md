# 简介 #

构建一个基于 uwsgi:v1.0.0 的flask app 镜像, 使用 supervisor 管理进程, 由uwsgi代理flask app.

# 如何使用 #

1. 构建镜像

```
docker build -t app:v1.0.0
```

2. 运行容器

```
docker run -it --rm -p :80:80 app:v1.0.0
```

3. 测试

```
wget http://localhost/
wget http://localhost/hello
```

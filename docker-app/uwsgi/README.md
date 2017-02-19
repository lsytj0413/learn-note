# 简介

包含一个构建基于 python:v2.7.12 的 uwsgi 以及 supervisor 的运行环境镜像.

# 如何使用 #

1. 构建镜像

```
docker build -t uwsgi:v1.0.0
```

2. 运行容器

```
docker run -it --rm uwsgi:v1.0.0
```

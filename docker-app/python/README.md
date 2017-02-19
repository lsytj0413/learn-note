# 简介

包含一个构建基于 Ubuntu:16.04 的 python2.7.12 运行环境镜像.

# 如何使用 #

1. 构建镜像

```
docker build -t python:v2.7.12
```

2. 运行容器

```
docker run -it --rm python:v2.7.12
```

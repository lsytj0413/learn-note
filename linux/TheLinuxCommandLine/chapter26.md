# 第二十六章: 自顶向下设计 #

对于任意一个大项目, 一般都会把繁重而复杂的任务分割为细小且简单的任务.

先确定上层步骤, 然后再逐步细化这些步骤的过程被称为自顶向下设计, 这种技巧允许我们把庞大而复杂的任务分割为许多小而简单的任务.
自顶向下设计是一种常见的程序设计方法, 尤其适合shell编程.

## 26.1 shell函数 ##

目前我们的脚本执行以下步骤来产生这个HTML文档:

1. 打开网页
2. 打开网页标头
3. 设置网页标题
4. 关闭网页标头
5. 打开网页主体部分
6. 输出网页标头
7. 输出时间戳
8. 关闭网页主体
9. 关闭网页

我们将在步骤7和步骤8之间添加一些额外的任务:

- 系统正常运行时间和负载: 这是自上次关机或重启系统的运行时间, 以及在几个时间间隔内当前运行在处理中的平均任务量
- 磁盘空间: 系统中存储设备的总使用量
- 家目录空间: 每个用户所使用的存储空间使用量

对于每一个任务, 都有相应的命令, 通过命令替换就可以很容易的把它们添加到我们的脚本中:

```
#!/bin/bash
# Program to output a system information page
TITLE="System Information Report For $HOSTNAME"
CURRENT_TIME=$(date +"%x %r %Z")
TIME_STAMP="Generated $CURRENT_TIME, by $USER"
cat << _EOF_
<HTML>
    <HEAD>
        <TITLE>$TITLE</TITLE>
    </HEAD>
    <BODY>
        <H1>$TITLE</H1>
        <P>$TIME_STAMP</P>
        $(report_uptime)
        $(report_disk_space)
        $(report_home_space)
    </BODY>
</HTML>
_EOF_
```

## 26.2 局部变量 ##

## 26.3 保持脚本的运行 ##

## 26.4 本章结尾语 ##

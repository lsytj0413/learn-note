# 第二十九章: 流控制: WHILE和UNTIL循环 #

## 29.1 循环 ##

循环是一系列重复的步骤, 循环中的动作会一直重复, 直到条件为真.

## 29.2 while ##

while命令的语法结构如下:

```
while commands; do commands; done
```

例如按顺序显示1～5的脚本如下:

```
#!/bin/bash

# while-count: display a series of numbers

count=1

while [ $count -le 5 ]; do
    echo $count
    count=$(( count + 1 ))
done
echo "Finished."
```

while循环会判断一系列指令的退出状态, 如果退出状态为0则执行循环内的命令.

## 29.3 跳出循环 ##

## 29.4 until ##

## 29.5 使用循环读取文件 ##

## 29.6 本章结尾语 ##

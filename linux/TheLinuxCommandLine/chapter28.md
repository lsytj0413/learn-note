# 第二十八章: 读取键盘输入 #

## 28.1 read-从标准输入读取输入值 ##

内嵌命令read的作用是读取一行标准输入, 可用于读取键盘输入值或应用重定向读取文件中的一行, 语法结构如下:

```
read [-options] [variable...]
```

其中variable是一个或多个用于存放输入值的变量, 若没有提供任何变量则由shell变量REPLY来存储数据行.

options为一个或多个可用的选项, 常用的选项如下表:

| 选项 | 描述 |
|:--|:--|
| -a array | 将输入值从索引为0的位置开始赋值给array |
| -d delimiter | 用字符串delimiter的第一个字符标志输入的结束, 而不是新的一行的开始 |
| -e | 使用Readline处理输入, 此命令使用户能使用命令行模式的相同方式编辑输入 |
| -n num | 从输入中读取num个字符, 而不是一整行 |
| -p prompt | 使用prompt字符串提示用户进行输入 |
| -r | 原始模式, 不能将反斜杠字符翻译为转义码 |
| -s | 保密模式, 不在屏幕中显示输入的字符 |
| -t seconds | 超时, 若输入超时则返回一个非0的退出状态 |
| -u fd | 从文件说明符fd读取输入, 而不是从标准输入中读取 |

使用read命令改写整数验证脚本如下:

```
#!/bin/bash

# read-integer: evaluate the value of an integer.

echo -n "Please enter an integer -> "
read int

if [ -z "$int" ]; then
    echo "int is empty." >&2
    exit 1
fi

if [[ "$int" =~ ^-?[0-9]+$ ]]; then
    if [ $int -eq 0 ]; then
        echo "int is zero."
    else
        if [ $int -lt 0 ]; then
            echo "int is negative."
        else
            echo "int is positive."
        fi
        if [ $((int % 2)) -eq 0 ]; then
            echo "int is even."
        else
            echo "int is odd."
        fi
    fi
else
    echo "int is not an integer." >&2
    exit 1
fi
```

或者读取输入值到多个变量:

```
echo -n "Enter one or more values > "
read var1 var2 var3 var4 var5
```

若read命令读取的值少于预期的数目, 则多余的变量值为空, 而输入值多余预期的数目时, 最后的变量则包含了所有的多余值.

### 28.1.1 选项 ###

可以使用 -p 选项来显示提示符:

```
read -p "Enter one or more values > " var1 var2
```

也可以使用 -t 选项加上 -s 选项来提示用户输入密码, 并限制等待时间:

```
read -t 10 -sp "ENter secret passphrase > " secret_pass
```

### 28.1.2 使用IFS间隔输入字段 ###

## 28.2 验证输入 ##

## 28.3 菜单 ##

## 28.4 本章结尾语 ##

## 28.5 附加项 ##

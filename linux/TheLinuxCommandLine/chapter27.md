# 第二十七章: 流控制: IF分支语句 #

## 27.1 使用if ##

在shell中一个简单的分支语句如下:

```
x=5
if [ $x = 5 ]; then
    echo "x equals 5."
else
    echo "x does not euqal 5."
fi
```

或者直接在命令行中如下输入:

```
x=5
if [ $x = 5 ]; then echo "equals 5."; else echo "does not equal 5"; fi
```

if语句的语法格式如下:

```
if commands; then
    commands
[elif commands; then
    commands...]
[else
    commands]
fi
```

## 27.2 退出状态 ##

## 27.3 使用test命令 ##

### 27.3.1 文件表达式 ###

### 27.3.2 字符串表达式 ###

### 27.3.3 整数表达式 ###

## 27.4 更现代的test命令版本 ##

## 27.5 (())-为整数设计 ##

## 27.6 组合表达式 ##

## 27.7 控制运算符: 另一种方式的分支 ##

## 27.8 本章结尾语 ##

# 第三十一章: 流控制: case分支 #

## 31.1 case ##

shell的多项选择复合命令称为case, 语法如下:

```
case word in
    [pattern [| pattern]...) commands ;;]...
esac
```

使用case命令简化read-menu程序如下:

```
#!/bin/bash

# read-menu: a menu driven system information program

clear
echo "
Please Select:

1. Display System Information
2. Display Disk Space
3. Display Home Space Utilization
0. Quit
"

read -p "Enter selection [0-3] > "

case $REPLY in
    0)         echo "Program terminated."
               exit
               ;;
    1)         echo "Hostname: $HOSTNAME"
               uptime
               ;;
    2)         df -h
               ;;
    3)         if [[ $(id -u) -eq 0 ]]; then
                   echo "Home Space Utilization (All Users)"
                   du -sh /home/*
               else
                   echo "Home Space Utilization ($USER)"
                   du -sh $HOME
               fi
               ;;
    *)         echo "Invalid entry." >&2
               exit 1
               ;;
esac
```

case命令将关键字的值与特定的模式相比较, 若发现吻合的模式则执行与此模式相联系的命令, 并不再对比剩余的模式.

### 31.1.1 模式 ###

### 31.1.2 多个模式的组合 ###

## 31.2 本章结尾语 ##

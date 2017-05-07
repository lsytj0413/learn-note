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

使用while循环改写 read-menu程序如下:

```
#!/bin/bash

# read-menu: a menu driven system information program

DELAY=3 # Number of seconds to display results

while [[ $REPLY != 0 ]]; do

    clear
    cat <<- EOF
Please Select:

1. Display System Information
2. Display Disk Space
3. Display Home Space Utilization
0. Quit
EOF

    read -p "Enter selection [0-3] > "
    if [[ $REPLY =~ ^[0-3]$ ]]; then
        if [[ $REPLY == 1 ]]; then
            echo "Hostname: $HOSTNAME"
            uptime
            sleep $DELAY
        fi
        if [[ $REPLY == 2 ]]; then
            df -h
            sleep $DELAY
        fi
        if [[ $REPLY == 3 ]]; then
            if [[ $(id -u) -eq 0 ]]; then
                echo "Home Space Utilization (All Users)"
                du -sh /home/*
            else
                echo "Home Space Utilization ($USER)"
                du -sh $HOME
            fi
            sleep $DELAY
        fi
    else
        echo "Invalid entry." >&2
        exit 1
    fi
done

echo "Program terminated."
```

## 29.3 跳出循环 ##

## 29.4 until ##

## 29.5 使用循环读取文件 ##

## 29.6 本章结尾语 ##

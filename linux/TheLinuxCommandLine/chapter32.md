# 第三十二章: 位置参数 #

## 32.1 访问命令行 ##

shell提供了一组称为位置参数的变量, 用于存储命令行中的关键字, 这些变量分别命名为0-9, 使用方法如下:

```
#!/bin/bash
# posit-param: script to view command line parameters
echo "
\$0 = $0
\$1 = $1
\$2 = $2
\$3 = $3
\$4 = $4
\$5 = $5
\$6 = $6
\$7 = $7
\$8 = $8
\$9 = $9
"
```

即便没有提供任何实参, 变量 $0 总是会存储命令行显示的第一行数据, 也就是所执行程序的路径名.

使用参数扩展技术, 可以获取多余9个的参数, 为标明一个大于9的数字, 将数字用大括号括起来即可, 例如 ${211} .

### 32.1.1 确定实参的数目 ###

shell还提供了变量 $# 以给出命令行参数的数目. 例如:

```
#!/bin/bash
# posit-param: script to view command line parameters
echo "
Number of arguments: $#
\$0 = $0
\$1 = $1
\$2 = $2
\$3 = $3
\$4 = $4
\$5 = $5
\$6 = $6
\$7 = $7
\$8 = $8
\$9 = $9
"
```

### 32.1.2 shift-处理大量的实参 ###

为了处理大量的实参, shell提供了shift命令, 每次执行shift命令之后所有的参数均下移一位, 这样就可以只处理一个参数($0) 而完成全部的任务.

```
#!/bin/bash
# posit-param2: script to display all arguments
count=1
while [[ $# -gt 0 ]]; do
    echo "Argument $count = $1"
    count=$((count + 1))
    shift
done
```

### 32.1.3 简单的应用程序 ###

一个简单的使用位置参数的程序如下:

```
#!/bin/bash
# file_info: simple file information program
PROGNAME=$(basename $0)
if [[ -e $1 ]]; then
    echo -e "\nFile Type:"
    file $1
    echo -e "\nFile Status:"
    stat $1
else
    echo "$PROGNAME: usage: $PROGNAME file" >&2
    exit 1
fi
```

这个程序输出了单个特定文件的文件类型和文件状态, 并且使用basename命令移除路径名的起始部分, 只留下基本的文件名.

### 32.1.4 在shell函数中使用位置参数 ###

位置参数也可用于shell函数实参的传递, 例子如下:

```
file_info () {
  # file_info: function to display file information
  if [[ -e $1 ]]; then
      echo -e "\nFile Type:"
      file $1
      echo -e "\nFile Status:"
      stat $1
  else
      echo "$FUNCNAME: usage: $FUNCNAME file" >&2
      return 1
  fi
}
```

shell会自动更新FUNCNAME变量以追踪当前执行的shell函数, 但是变量$0包含的总是命令行第一项的路径全名.

## 32.2 处理多个位置参数 ##

## 32.3 更完整的应用程序 ##

## 32.4 本章结尾语 ##

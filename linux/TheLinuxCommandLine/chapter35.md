# 第三十五章: 数组 #

本章介绍一种包含多个值的数据结构--数组.

## 35.1 什么是数组 ##

数组是可以一次存放多个值的变量, 组织形式如同表格. 数组中的单元叫做元素, 并且每个元素含有数据, 使用一种叫做索引或是下标的地址就可以访问一个独立的数组元素.

bash的数组是一维的, bash的第二个版本开始提供对数组的支持, 而最初的UNIX shell程序sh是不支持数组的.

## 35.2 创建一个数组 ##

命名数组变量同命名其他shell变量一样, 当访问数组变量时可以自动创建它们. 例如:

```
a[1]=foo
echo ${a[1]}
```

在输出变量时使用花括号是为了阻止shell在数组元素名里试图扩展路径名. 也可以使用 declare 命令创建数组, 如下:

```
declare -a a
```

## 35.3 数组赋值 ##

使用下面的语法可以对数组的单一元素赋值:

```
name[subscript]=value
```

这里name是数组名, subscript是大于等于0的整数, value是赋值给数组元素的字符串或整数.

使用下面的语法可以对整个数组赋值:

```
name=(value1 value2...)
```

这里name是数组名, 并且将value1, value2...等值依次赋予从索引0开始的数组元素. 也可以通过为每个值指定下标来对特定的元素赋值:

```
days=(Sun Mon Tue Wed Thu Fri Sat)
# 等价于
days=([0]=Sun [1]=Mon [2]=Tue [3]=Wed [4]=Thu [5]=Fri [6]=Sat)
```

## 35.4 访问数组元素 ##

创建一个脚本, 用于输出特定目录中文件的修改次数, 示例输出如下:

```
[me@linuxbox ~]$ hours .
Hour Files Hour Files
---- ----- ---- ----
00   0     12   11
01   1     13   7
02   0     14   1
03   0     15   7
04   1     16   6
04   1     17   5
06   6     18   4
07   3     19   4
08   1     20   1
09   14    21   0
10   2     22   0
11   5     23   0
Total files = 80
```

hours程序输出在指定目录中, 一天中的每个小时有多少文件经过最后一次修改. 该脚本代码如下:

```
#!/bin/bash
# hours : script to count files by modification time
usage () {
    echo "usage: $(basename $0) directory" >&2
}
# Check that argument is a directory
if [[ ! -d $1 ]]; then
    usage
    exit 1
fi
# Initialize array
for i in {0..23}; do hours[i]=0; done
# Collect data
for i in $(stat -c %y "$1"/* | cut -c 12-13); do
    j=${i/#0}
    ((++hours[j]))
    ((++count))
done
# Display data
echo -e "Hour\tFiles\tHour\tFiles"
echo -e "----\t-----\t----\t-----"
for i in {0..11}; do
    j=$((i + 12))
    printf "%02d\t%d\t%02d\t%d\n" $i ${hours[i]} $j ${hours[j]}
done
printf "\nTotal files = %d\n" $count
```

在第三部分代码中, 我们使用stat程序遍历目录中的每个文件来采集数据, 使用cut选项中结果中提取两位小时数, 并且清除hour域中的前导0.

## 35.5 数组操作 ##

### 35.5.1 输出数组的所有内容 ###

### 35.5.2 确定数组元素的数目 ###

### 35.5.3 查找数组中使用的下标 ###

### 35.5.4 在数组的结尾增加元素 ###

### 35.5.5 数组排序操作 ###

### 35.5.6 数组的删除 ###

## 35.6 本章结尾语 ##

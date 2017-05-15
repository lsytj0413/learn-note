# 第三十六章: 其他命令 #

## 36.1 组命令和子shell ##

bash允许将命令组合到一起使用, 有两种方式, 分别是组命令和子shell:

```
# 组命令
{ command1; command2; [command3; ...] }
# 子shell
(command1; command2; [command3; ...])
```

需要注意的是, 在实现组命令时必须使用一个空格将花括号与命令分开, 并且在闭花括号前使用分号或是换行来结束最后的命令.

### 36.1.1 执行重定向 ###

可以使用组命令和子shell来管理重定向:

```
ls -l > output.txt
echo "Listing of foo.txt" >> output.txt
cat foo.txt >> output.txt

# 等价于
{ ls -l; echo "Listing of foo.txt"; cat foo.txt; } > output.txt
# 或是
(ls -l; echo "Listing of foo.txt"; cat foo.txt) > output.txt
```

当创建命令管道时, 通常将多条命令的结果输出到一条流中, 这比较有用:

```
{ ls -l; echo "Listing of foo.txt"; cat foo.txt; } | lpr
```

### 36.1.2 进程替换 ###

组命令和子shell有一个主要的不同: 子shell在当前shell的子拷贝中执行命令, 而组命令在当前shell里面执行命令. 通常情况下组命令更合适, 除非脚本真的需要子shell.

在之前的章节中, 我们接触到了一个子shell环境导致的问题实例:

```
echo "foo" | read
```

以上的命令并不能对REPLY变量进行赋值, 因为read命令是在子shell中执行的. 由于总是在子shell中执行管道中的命令, 所以任何变量赋值都会遇到这个问题. shell提供了一种称为进程替换的外部扩展方式来解决这个问题:

实现进程替换的方式有两种, 一种是产生标准输出的进程:

```
<(list)
```

另一种是吸纳标准输入的进程:

```
>(list)
```

这里的list是一系列命令. 为了解决上述read命令的问题, 可以像如下方式那样来使用进程替换:

```
read < <(echo "foo")
```

进程替换允许把子shell的输出当作一个普通的文件, 目的是为了重定向. 事实上这是一种扩展形式, 我们可以查看它的真实值:

```
[me@linuxbox ~]$ echo <(echo "foo")
/dev/fd/63
```

进程替换通常结合带有read的循环使用, 例如如下代码:

```
#!/bin/bash
# pro-sub : demo of process substitution
while read attr links owner group size date time filename; do
    cat <<- EOF
        Filename:     $filename
        Size:         $size
        Owner:        $owner
        Group:        $group
        Modified:     $date $time
        Links:        $links
        Attributes:   $attr
    EOF
done < <(ls -l | tail -n +2)
```

产生的输出如下:

```
[me@linuxbox ~]$ pro_sub | head -n 20
Filename: addresses.ldif
Size: 14540
Owner: me
Group: me
Modified: 2009-04-02 11:12
Links:
1
Attributes: -rw-r--r--
Filename: bin
Size: 4096
Owner: me
Group: me
Modified: 2009-07-10 07:31
Links: 2
Attributes: drwxr-xr-x
Filename: bookmarks.html
Size: 394213
Owner: me
Group: me
```

## 36.2 trap ##

## 36.3 异步执行 ##

## 36.4 命名管道 ##

### 36.4.1 设置命名管道 ###

### 36.4.2 使用命名管道 ###

## 36.5 本章结尾语 ##

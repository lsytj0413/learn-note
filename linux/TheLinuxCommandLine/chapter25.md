# 第二十五章: 启动一个项目 #

从本章开始, 以编写一个报告生成器程序为示例, 该程序会显示系统的各种统计数据和它的状态, 并将产生HTML格式的报告.

## 25.1 第一阶段: 最小的文档 ##

首先编写一个直接输出HTML文件的程序, 编辑 ~/bin/sys\_info\_page 文件内容如下:

```
#!/bin/bash
# Program to output a system information page
echo "<HTML>
    <HEAD>
        <TITLE>Page Title</TITLE>
    </HEAD>
    <BODY>
        Page Body.
    </BODY>
</HTML> "
```

然后使用以下命令生成结果文件:

```
sys_info_page > sys_info_page.html
```

## 25.2 第二阶段: 加入一点数据 ##

修改脚本, 增加一个网页标题和报告正文部分:

```
#!/bin/bash
# Program to output a system information page
echo "<HTML>
    <HEAD>
        <TITLE>System Information Report</TITLE>
    </HEAD>
    <BODY>
        <H1>System Information Report</H1>
    </BODY>
</HTML> "
```

## 25.3 变量和常量 ##

### 25.3.1 创建变量和常量 ###

我们可以创建一个名为title的变量, 并把 *System Information Report* 字符串赋值给它, 以简化脚本的编写和维护工作:

```
#!/bin/bash
# Program to output a system information page
title="System Information Report"
echo "<HTML>
    <HEAD>
        <TITLE>$title</TITLE>
    </HEAD>
    <BODY>
        <H1>$title</H1>
    </BODY>
</HTML> "
```

当shell碰到一个变量的时候, 它会自动创建该变量. 变量的命名规则如下:

1. 变量名可以由字母数字字符和下划线组成
2. 变量名的第一个字符必须是一个字母或一个下划线
3. 变量名中不允许出现空格和标点符号

在shell中不能辨别变量和常量, 一个惯例是指定大写字母来表示常量, 小写字母表示变量:

```
#!/bin/bash
# Program to output a system information page
TITLE="System Information Report For $HOSTNAME"
echo "<HTML>
    <HEAD>
        <TITLE>$TITLE</TITLE>
    </HEAD>
    <BODY>
        <H1>$TITLE</H1>
    </BODY>
</HTML> "
```

我们在标题中添加了HOSTNAME, 使标题与机器的网络名称相关联起来.

shell提供了一种方法, 通过使用带有 -r 选项的内部命令 declare来强制常量的不变性.

```
declare -r TITLE="System Information Report For $HOSTNAME"
```

但是这个功能极少被使用, 但为了很早之前的脚本, 它仍然存在.

### 25.3.2 为变量和常量赋值 ###

## 25.4 here文档 ##

## 25.5 本章结尾语 ##

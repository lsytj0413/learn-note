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

### 25.3.2 为变量和常量赋值 ###

## 25.4 here文档 ##

## 25.5 本章结尾语 ##

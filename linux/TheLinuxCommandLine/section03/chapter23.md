# 第二十三章: 编译程序 #

本章介绍的命令如下:

- make: 维护程序的工具

## 23.1 什么是编译 ##

编译是把源码翻译成计算机处理器的语言的过程.

用高级语言编写的程序, 经过另一个称为编译器的程序的处理, 会转换成机器语言. 一些编译器把高级语言翻译成汇编语言, 然后使用一个汇编器完成翻译成机器语言的最后阶段.

## 23.2 是不是所有的程序都需要编译 ##

不是所有的程序都需要编译, 例如脚本语言由解释器执行, 就不需要编译.

## 23.3 编译一个C程序 ##

在编译之前, 需要一些工具, 例如编译器, 链接器以及make. 在Linux环境中, 普遍使用的C编译器叫做gcc.

### 23.3.1 获取源代码 ###

首先创建一个名为src的目录来存放源码, 然后使用ftp协议把源码下载下来:

```
mkdir src
cd src
ftp ftp.gnu.org
cd gnu/diction
get diction-1.11.tar.gz
bye
```

然后解压代码:

```
tar xzf diction-1.11.tar.gz
```

### 23.3.2 检查源代码树 ###

### 23.3.3 生成程序 ###

大多数程序都可以通过以下的简单的命令编译:

```
./configure
make
```

configure程序是一个shell脚本, 由源码树提供, 它的工作是分析程序建立环境.

configure命令会创建几个新文件, 其中最重要的是 Makefile. Makefile是一个配置文件, 指示make程序如何构建程序.

### 23.3.4 安装程序 ###

打包良好的源码经常包括一个特别的make目标文件, 叫做install, 使用以下命令可以执行安装操作:

```
# 通常安装到 /usr/local/bin
sudo make install
```

## 23.4 本章结尾语 ##

在本章中, 介绍了通过以下命令编译并安装程序:

```
./configure
make
make install
```
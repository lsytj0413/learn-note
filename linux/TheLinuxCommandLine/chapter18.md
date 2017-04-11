# 第十八章: 归档和备份 #

本章介绍的命令如下:

- gzip: 压缩和解压缩文件工具
- bzip2: 块排序文件压缩工具
- tar: 磁带归档工具
- zip: 打包和压缩文件
- rsync: 远程文件和目录的同步

## 18.1 文件压缩 ##

压缩算法一般分为两大类: 无损压缩和有损压缩. 在下面的讨论中仅仅设计无损压缩.

### 18.1.1 gzip-文件压缩与解压缩 ###

gzip命令用于压缩一个或多个文件, 执行命令后原文件会被压缩文件取代, 执行gunzip命令则可以将压缩文件还原为原文件.

```
ls -l /etc > foo.txt
# 压缩, 生成foo.txt.gz文件, foo.txt被删除
gzip foo.txt
# 解压缩foo.txt.gz文件
gunzip foo.txt
```

gzip常用的选项如下表:

| 选项 | 功能描述 |
|:--|:--|
| -c | 将输出内容写道标准输出并且保持原文件, 同 --stdout或 --to-stdout选项 |
| -d | 解压缩, 加上此命令后则等同 gunzip命令, 同 --decompress或 --uncompress 选项 |
| -f | 强制压缩, 即使压缩版本已经存在, 同 --force 选项 |
| -h | 显示帮助信息, 同 --help 选项 |
| -l | 列出所有压缩文件的压缩统计, 同 --list 选项 |
| -r | 如果操作参数有一个或多个目录, 则递归压缩包含在目录中的文件, 同 --recursive 选项 |
| -t | 检验压缩文件的完整性, 同 --test 选项 |
| -v | 在压缩时显示详细信息, 同 --verbose 选项 |
| -number | 设定压缩级别, number为 1(速度最快, 压缩比最小) 到9(速度最慢, 压缩比最大), 其中1等于 --fast, 9等于 --best, 默认级别为6 |

```
gzip foo.txt
gzip -tv foo.txt.gz
gzip -d foo.txt.gz

ls -l /etc | gzip > foo.txt.gz
# gunzip默认解压缩后最为 .gz 的文件
gunzip foo.txt
# 只查看压缩文本文件的内容
gunzip -c foo.txt | less
```

可以利用zcat命令联合gzip, 效果等同于带有 -c 选项的gunzip. zcat 的功能与cat命令相同, 只是它的操作对象是压缩文件.

```
zcat foo.txt.gz | less
```

同样也有zless命令, 与less管道功能相同.

### 18.1.2 bzip2-牺牲速度以换取高质量的数据压缩 ###

bzip2与gzip命令功能相仿, 但使用不同的压缩算法, 该算法具有高质量的数据压缩能力, 但却降低了压缩速度. 多数情况下用法与gzip相似, 只是用bzip2压缩后的文件以 .bz2 为后缀.

```
ls -l /etc > foo.txt
ls -l foo.txt
bzip2 foo.txt
ls -l foo.txt.bz2
bunzip2 foo.txt.bz2
```
前面讨论的gzip的所有选项(除 -r选项), bzip2都支持. 两者的压缩级别选项有些许不同, 同时解压缩文件的专用工具是 bunzip2 额 bzcat 命令.

bzip2还有 bzip2recover 命令, 用于恢复损坏的 .bz2 文件.

## 18.2 文件归档 ##

### 18.2.1 tar-磁带归档工具 ###

### 18.2.2 zip-打包压缩工具 ###

## 18.3 同步文件和目录 ##

### 18.3.1 rsync-远程文件, 目录的同步 ###

### 18.3.2 在网络上使用rsync命令 ###

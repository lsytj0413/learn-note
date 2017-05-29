# ditaa #

[官网](http://ditaa.sourceforge.net/)

## 简介 ##

ditaa 是一个使用java语言编写的命令行工具, 可以将ascii字符组成的图形转换为图片.

## 安装及使用 ##

在 Ubuntu16.04 中, 可以使用 *apt install ditaa* 安装ditaa工具, 使用的命令行如下:

```
ditaa example.dit [example.png]
```

例如使用以下内容, [ditaa01](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa01.dit):

```
+--------+   +-------+    +-------+
|        | --+ ditaa +--> |       |
|  Text  |   +-------+    |diagram|
|Document|   |!magic!|    |       |
|     {d}|   |       |    |       |
+---|----+   +-------+    +-------+
    :                         ^
    |       Lots of work      |
    +-------------------------+
```

生成的效果图如下:

![ditaa01.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa01.png)

## 语法 ##

### 矩形 ###

可以使用 / 以及 \ 来连接转角, ditaa会将这两个字符绘制为圆角, 例如 [ditaa02](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa02.dit):

```
/--+
|  |
+--/
```

生成的效果图如下:

![ditaa02.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa02.png)

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

### 颜色 ###

可以在图形中定义颜色, 对于颜色代码的语法如下:

```
cXXX
```

其中 XXX 是一个16进制的数字, 一个示例如下 [ditaa03](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa03.dit):

```
/----\  /----\
|c33F|  |cC02|
|    |  |    |
\----/  \----/

/----\  /----\
|c1FF|  |c1AB|
|    |  |    |
\----/  \----/
```

生成的效果图如下:

![ditaa03.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa03.png)

也可以使用一些可读的字符串来定义颜色, 一个示例如下 [ditaa04](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa04.dit):

```
Color codes
/-------------|-------------\
|cRED RED     |cBLU BLU     |
+-------------|-------------+
|cGRE GRE     |cPNK PNK     |
+-------------|-------------+
|cBLK BLK     |cYEL YEL     |
\-------------|-------------/
```

生成的效果图如下:

![ditaa04.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa04.png)

如果定义了颜色的形状中包含文字, 文字的颜色会根据形状的颜色而自动变化. 颜色代码只在闭合的形状中生效, 在其他地方是不生效的.

### 形状 ###

ditaa 支持一些其他的形状, 形状的代码在 {} 中定义, 常见的形状如下表:

| 形状 | 代码 | 图形 |
|:--|:--|:--|
| Document | {d} | ![ditaa05.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa05.png) |
| Storage | {s} | ![ditaa06.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa06.png) |
| Input/Output | {io} | ![ditaa07.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa07.png) |

#### Document ####

定义内容如下 [ditaa05](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa05.dit):

```
+-----+
|{d}  |
|     |
|     |
+-----+
```

生成的效果图如下:

![ditaa05.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa05.png)

#### Storage ####

定义内容如下 [ditaa06](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa06.dit):

```
+-----+
|{s}  |
|     |
|     |
+-----+
```

生成的效果图如下:

![ditaa06.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa06.png)

#### Input/Output ####

定义内容如下 [ditaa07](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa07.dit):

```
+-----+
|{io} |
|     |
|     |
+-----+
```

生成的效果图如下:

![ditaa07.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa07.png)

### 线条 ###

所有的包含一个 =(横线) 或者 :(竖线) 的线条会被绘制为虚线, 一个示例如下 [ditaa08](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa08.dit):

```
----+  /----\  +----+
    :  |    |  :    |
    |  |    |  |{s} |
    v  \-=--+  +---=+
```

生成的效果图如下:

![ditaa08.png](https://github.com/lsytj0413/learn-note/blob/master/draw/ditaa/ditaa08.png)

# graphviz #

[官网](http://www.graphviz.org/)

## 简介 ##

graphviz是贝尔实验室开发的一个开源的工具包, 它使用一个特定的DSL(领域特定语言): dot作为脚本语言, 然后使用布局引擎来解析此脚本并完成自动布局.
graphviz提供丰富的导出格式, 如常用的图片格式, SVG, PDF格式等.

graphviz包含了众多的布局器:

- dot: 默认布局方式, 主要用于有向图
- neato: 基于spring-model(又称force-based)算法
- twopi: 径向布局
- circo: 圆环布局
- fdp: 用于无向图

首先, 在dot脚本中定义图的顶点和边, 顶点和边都具有各自的属性, 比如形状, 颜色, 填充模式, 字体和样式等, 然后使用合适的布局算法进行布局. 布局算法除了绘制各个顶点和边之外, 需要尽可能的将顶点均匀的分布在画布上, 并且尽可能的减少边的交叉.

使用graphviz绘图的一般流程为:

1. 定义一个图, 并向图中添加需要的顶点和边
2. 为顶点和边添加样式
3. 使用布局引擎进行绘制

对于开发人员而言, 经常会用到的图形绘制可能包括: 函数调用关系, 一个复杂的数据结构, 系统的模块组成, 抽象语法树等.

## 基础知识 ##

graphviz包含3种元素, 即图, 顶点和边. 每个元素都可以具有各自的属性, 用来定义字体, 样式, 颜色和形状等.

### 第一个graphviz图 ###

绘制一个简单的有向图, 包含a, b, c, d四个节点. 其中a指向b, b和c指向d.
将以下内容保存为 [graph01.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph01.dot):

```
digraph graph01 {
  a;
  b;
  c;
  d;

  a -> b;
  b -> d;
  c -> d;
}
```

使用dot布局方式, 绘制出来的效果如下图:

![graph01](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph01.png)

默认的顶点中的文字为定义顶点变量的名称, 形状为椭圆. 边的默认样式为黑色实线箭头.

### 定义顶点和边的样式 ###

在digraph的花括号内, 添加顶点和边的新定义, 保存为 [graph02.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph02.dot):

```
  node [shape="record"];
  edge [style="dashed"];
```

绘制的效果如下图:

![graph02](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph02.png)

### 修改顶点和边样式 ###

进一步, 我们将顶点a的颜色修改为淡绿色, 并将c到d的边修改为红色, 将以下内容保存为 [graph03](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph03.dot):

```
digraph graph03{
  node [shape="record"];
  edge [style="dashed"];

  a [style="filled", color="black", fillcolor="chartreuse"];
  b;
  c;
  d;

  a -> b;
  b -> d;
  c -> d [color="red"];
}
```

绘制的效果如下图:

![graph03](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph03.png)

### 以图片为节点 ###

# graphviz #

[官网](http://www.graphviz.org/)

[User Guide](https://github.com/lsytj0413/learn-note/blob/master/draw/dotguide.pdf)

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

## dot语法 ##

### 注释 ###

dot语言使用类 C 语言形式的注释, 如下:

```
// this is comment
/* comment
   next line
   */
```

### 有向图 ###

1. 使用 digraph 定义有向图
2. 使用 -> 表述节点之间的关系

例如:

```
digraph g {
  a -> b;
  b -> c;
  c -> a;
}
```

### 无向图 ###

1. 使用 graph 定义无向图
2. 使用 -- 表述节点之间的关系

### 节点之间的关系 ###

- 在有向图中使用 a -> b 形式, 表示节点 a 指向节点 b ;
- 在无向图中使用 a -- b 形式, 表示节点 a 和节点 b 连通;

### 定义节点属性 ###

定义属性的格式为:

```
node [attr1=value1, attr2=value2];
```

例如定义 a 节点为长方形, 显示文本为 Hello world, 样式为填充, 填充颜色为 #ABACBA

```
a [shape=box, label="Hello world", style=filled, fillcolor="#ABACBA"];
```

### 定义关系属性 ###

格式与定义节点属性相似:

```
a -> b [attr1=value1, attr2=value2];
```

## 基础图形 ##

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

节点也可以使用图片, 不过需要注意的是, 在使用图片作为节点的时候需要将本来的形状设置为none, 并且将label置为空字符串, 以避免文字对图片的干扰.

将以下内容保存为 [graph04.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph04.dot):

```
digraph graph04{
  node [shape="record"];
  edge [style="dashed"];


  a [style="filled", color="black", fillcolor="chartreuse"];
  b;
  c [shape="none", image="../img/chrome.png", label=""];
  d;

  a -> b;
  b -> d;
  c -> d [color="red"];
}
```

效果图如下:

![graph04](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph04.png)

### 子图的绘制 ###

graphviz支持子图, 即图中的部分节点和边相对对立. 将以下内容保存为 [graph05.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph05.dot):

```
digraph graph05{
  node [shape="record"];
  edge [style="dashed"];

  a [style="filled", color="black", fillcolor="chartreuse"];
  b;

  subgraph cluster_cd{
    label="c and d";
    bgcolor="mintcream";
    c;
    d;
  }

  a -> b;
  b -> d;
  c -> d [color="red"];
}
```

效果图如下:

![graph05](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph05.png)

需要注意的是, 子图的名称必须以 cluster开头, 否则graphviz无法识别.

## 结构的可视化 ##

在实际的开发中, 经常要用到的是对复杂结构的描述, graphviz提供完善的机制来绘制此类图形.

### hash表 ###

假设一个具有如下结构的hash表:

```
struct st_hash_type {
    int (*compare) ();
    int (*hash) ();
};

struct st_table_entry {
    unsigned int hash;
    char *key;
    char *record;
    st_table_entry *next;
};

struct st_table {
    struct st_hash_type *type;
    int num_bins;
    int num_entries;
    struct st_table_entry **bins;
};
```

可以通过graphviz绘制结构之间的引用关系, 将以下内容保存为 [graph06.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph06.dot):

```
digraph graph06 {
  fontname = "Verdana";
  fontsize = 10;
  rankdir = TB;

  node [fontname="Verdana", fontsize=10, color="skyblue", shape="record"];
  edge [fontname="Verdana", fontsize=10, color="crimson", style="solid"];

  st_hash_type [label="{<head>st_hash_type|(*compare)|(*hash)}"];
  st_table_entry [label="{<head>st_table_entry|hash|key|record|<next>next}"];
  st_table [label="{st_table|<type>type|num_bins|num_entries|<bins>bins}"];

  st_table:bins -> st_table_entry:head;
  st_table:type -> st_hash_type:head;
  st_table_entry:next -> st_table_entry:head [style="dashed", color="forestgreen"];
}
```

效果图如下:

![graph06](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph06.png)

在顶点的形状为record的时候, lable属性的语法比较奇怪, 但是使用起来非常灵活. 比如用竖线隔开的串会在绘制出来的节点中展现为一条分隔符, 用尖括号括起来的串称为锚点, 当一个节点具有多个锚点的时候这个特性会非常有用.
例如节点 st\_table 的type属性指向 st\_hash\_type, 第4个属性指向 st\_table\_entry等, 都是通过锚点来实现的.

也可以使用 circo算法来重新布局, 在 [graph07.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph07.dot) 中添加以下内容:

```
  layout = "circo";
```

效果图如下:

![graph07](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph07.png)

### 另一个hash表 ###

将以下内容保存为 [graph08.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph08.dot):

```
digraph graph08 {
  fontname = "Verdana";
  fontsize = 10;
  rankdir = LR;
  rotate = 180;

  node [shape="record", width=.1, height=.1];
  node [fontname="Verdana", fontsize=10, color="skyblue", shape="record"];

  edge [fontname="Verdana", fontsize=10, color="crimson", style="solid"];
  node [shape="plaintext"];

  st_table [label=<
            <table border="0" cellborder="1" cellspacing="0" align="left">
            <tr>
            <td>st_table</td>
            </tr>
            <tr>
            <td>num_bins=5</td>
            </tr>
            <tr>
            <td>num_entries=3</td>
            </tr>
            <tr>
            <td port="bins">bins</td>
            </tr>
            </table>
  >];

  node [shape="record"];
  num_bins [label=" <b1> | <b2> | <b3> | <b4> | <b5> ", height=2];
  node [width=2];

  entry_1 [label="{<e>st_table_entry|<next>next}"];
  entry_2 [label="{<e>st_table_entry|<next>null}"];
  entry_3 [label="{<e>st_table_entry|<next>null}"];

  st_table:bins -> num_bins:b1;
  num_bins:b1 -> entry_1:e;
  entry_1:next -> entry_2:e;
  num_bins:b3 -> entry_3:e;
}
```

效果图如下:

![graph08](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph08.png)

从上例中可以看到, 节点的label属性支持类似于HTML语言中的TABLE形式的定义, 通过行列的数目来定义节点的形状, 从而使节点的组成更加灵活.

### 软件模块组成图 ###

可以使用graphviz绘制软件的模块图, 这些模块之间可以有复杂的关系, 并且部分关系密切的模块应归为一个子系统中.
将以下内容保存为 [graph09.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph09.dot):

```
digraph graph09{
  rankdir = TB;
  fontname = "Verdana";
  fontsize = 12;

  node [fontname="Verdana", fontsize=12, shape="record"];
  edge [fontname="Verdana", fontsize=12];

  subgraph cluster_sl{
    label="IDP支持层";
    bgcolor="mintcream";
    node [shape="Mrecord", color="skyblue", style="filled"];
    network_mgr [label=<<table><tr><td>网络管理器</td></tr></table>>];
    log_mgr [label=<<table><tr><td>日志管理器</td></tr></table>>];
    module_mgr [label=<<table><tr><td>模块管理器</td></tr></table>>];
    conf_mgr [label=<<table><tr><td>配置管理器</td></tr></table>>];
    db_mgr [label=<<table><tr><td>数据库管理器</td></tr></table>>];
    };

  subgraph cluster_md{
    label="可插拔模块集";
    bgcolor="lightcyan";
    node [color="chartreuse2", style="filled"];

    mod_dev [label=<<table><tr><td>开发支持模块</td></tr></table>>];
    mod_dm [label=<<table><tr><td>数据建模模块</td></tr></table>>];
    mod_dp [label=<<table><tr><td>部署发布模块</td></tr></table>>];
    };

 mod_dp -> mod_dev [label="依赖..."];
 mod_dp -> mod_dm [label="依赖..."];
 mod_dp -> module_mgr [label="安装...", color="yellowgreen", arrowhead="none"];
 mod_dev -> mod_dm [label="依赖..."];
 mod_dev -> module_mgr [label="安装...", color="yellowgreen", arrowhead="none"];
 mod_dm -> module_mgr [label="安装...", color="yellowgreen", arrowhead="none"];
}
```

效果图如下:

![graph09](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph09.png)

在上例中我们在有些地方使用HTML形式的label语法, 因为使用字符串形式的语法不能正确显示中文, 具体原因待查.

### 状态机 ###

作一个简易有限自动机图, 接受a以及以a结尾的任意长度的字符串.
将以下内容保存为 [graph10.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph10.dot):

```
digraph graph10{
  size = "8.5, 11";
  fontname = "Verdana";
  fontsize = 10;

  node [shape=circle, fontname="Verdana", fontsize=10];
  edge [fontname="Verdana", fontsize=10];

  0 [style=filled, color=lightgrey];
  2 [shape=doublecircle];

  0 -> 2 [label="a "];
  0 -> 1 [label="other "];
  1 -> 2 [label="a "];
  1 -> 1 [label="other "];
  2 -> 2 [label="a "];
  2 -> 1 [label="other "];

  "Machine: a" [shape=plaintext];
}
```

效果图如下:

![graph10](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph10.png)

形状值为plaintext的表示不绘制边框, 用于展示纯文本内容, 在绘制指示性的文本时很有用.

### 模块生命周期图 ###

作一个简易生命周期图, 包括安装, 卸载, 正在启动等状态.
将以下内容保存为 [graph11.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph11.dot):

```
digraph graph11{
  rankdir = TB;
  fontname = "Verdana";
  fontsize = 12;

  node [fontname="Verdana", fontsize=12, shape="Mrecord", color="skyblue", style="filled"];
  edge [fontname="Verdana", fontsize=12, color="darkgreen"];

  installed [label=<<table><tr><td>已安装</td></tr></table>>];
  resolved [label=<<table><tr><td>已就绪</td></tr></table>>];
  uninstalled [label=<<table><tr><td>已卸载</td></tr></table>>];
  starting [label=<<table><tr><td>正在启动</td></tr></table>>];
  active [label=<<table><tr><td>正在运行</td></tr></table>>];
  stoping [label=<<table><tr><td>正在停止</td></tr></table>>];
  start [label="", shape="circle", width=0.5, fixedsize=true, style=filled, color="black"];

  start -> installed [label="安装"];
  installed -> uninstalled [label="卸载"];
  installed -> resolved [label="准备"];
  installed -> installed [label="更新"];
  resolved -> installed [label="更新"];
  resolved -> uninstalled [label="卸载"];
  resolved -> starting [label="启动"];
  starting -> active [label=""];
  active -> stoping [label="停止"];
  stoping -> resolved [label=""];
}
```

效果图如下:

![graph11](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph11.png)

## 其他实例 ##

### 抽象语法树 ###

使用graphviz绘图的表达式 (3+4)*5 的抽象语法树, 将以下内容保存为 [graph12.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph12.dot):

```
digraph graph12{
  fontname = "Verdana";
  fontsize = 10;

  node [sbape=circle, fontname="Verdana", fontsize=10];
  edge [fontname="Verdana", fontsize=10];
  node [shape="plaintext"];

  mul [label="mul(*)"];
  add [label="add(+)"];

  add -> 3;
  add -> 4;
  mul -> add;
  mul -> 5;
}
```

效果图如下:

![graph12](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph12.png)

### UML类图 ###

使用graphviz绘图的简单的UML类图, 将以下内容保存为 [graph13.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph13.dot):

```
digraph graph13{
  fontname = "Courier New";
  fontsize = 10;

  node [fontname="Courier New", fontsize=10, shape=record];
  edge [fontname="Courier New", fontsize=10];

  Animal [label="{Animal |+ name : String\l+ age : int \l|+ die() : void\l}"];
  subgraph clusterAnimalImpl{
    bgcolor="yellow";
    Dog [label="{Dog||+ bark() : void\l}"];
    Cat [label="{Cat||+ meow() : void\l}"];
  };

  edge [arrowhead="empty"];

  Dog -> Animal;
  Cat -> Animal;
  Dog -> Cat [arrowhead="none", label="0..*"];
}
```

效果图如下:

![graph13](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph13.png)

### 状态图 ###


将以下内容保存为 [graph14.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph14.dot):

```
digraph graph14 {
  rankdir = LR;
  size = "8,5"

  node [shape = doublecircle];

  LR_0 LR_3 LR_4 LR_8;

  node [shape = circle];

  LR_0 -> LR_2 [ label = "SS(B)" ];
  LR_0 -> LR_1 [ label = "SS(S)" ];
  LR_1 -> LR_3 [ label = "S($end)" ];
  LR_2 -> LR_6 [ label = "SS(b)" ];
  LR_2 -> LR_5 [ label = "SS(a)" ];
  LR_2 -> LR_4 [ label = "S(A)" ];
  LR_5 -> LR_7 [ label = "S(b)" ];
  LR_5 -> LR_5 [ label = "S(a)" ];
  LR_6 -> LR_6 [ label = "S(b)" ];
  LR_6 -> LR_5 [ label = "S(a)" ];
  LR_7 -> LR_8 [ label = "S(b)" ];
  LR_7 -> LR_5 [ label = "S(a)" ];
  LR_8 -> LR_6 [ label = "S(b)" ];
  LR_8 -> LR_5 [ label = "S(a)" ];
}
```

效果图如下:

![graph14](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph14.png)

### 时序图 ###

使用graphviz绘图的简单的时序图, 将以下内容保存为 [graph15.dot](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph15.dot):

```
digraph graph15 {
  rankdir="LR";
  node[shape="point", width=0, height=0];
  edge[arrowhead="none", style="dashed"]

  {
    rank="same";
    edge[style="solided"];
    LC[shape="plaintext"];
    LC -> step00 -> step01 -> step02 -> step03 -> step04 -> step05;
  }

  {
    rank="same";
    edge[style="solided"];
    Agency[shape="plaintext"];
    Agency -> step10 -> step11 -> step12 -> step13 -> step14 -> step15;
  }

  {
    rank="same";
    edge[style="solided"];
    Agent[shape="plaintext"];
    Agent -> step20 -> step21 -> step22 -> step23 -> step24 -> step25;
  }

  step00 -> step10 [label="sends email new custumer", arrowhead="normal"];
  step11 -> step01 [label="declines", arrowhead="normal"];
  step12 -> step02 [label="accepts", arrowhead="normal"];
  step13 -> step23 [label="forward to", arrowhead="normal"];
  step24 -> step14;
  step14 -> step04 [arrowhead="normal"];
}
```

效果图如下:

![graph15](https://github.com/lsytj0413/learn-note/blob/master/draw/graphviz/graph15.png)

可以看到, 在代码中有用 {} 括起来的部分, 每一个 rank=same 的block中的所有节点都会在同一条线上.

## 附录 ##

dot脚本很容易被其他语言生成, 而且如果你希望快速的将自己的想法画出来, 那么graphviz是一个不错的选择.

但是graphviz也有一定的局限, 比如绘制时序图就很难实现. 而且graphviz中的节点出现在画布上的位置是不确定的, 依赖于所使用的布局算法, 而不是在脚本中出现的位置.

graphviz的强项在于自动布局, 如果仅用于显示模块间的关系, 子模块与子模块通信的方式, 模块间的逻辑位置等, 那么graphviz完全可以胜任. 但是如果图中节点的位置必须是精确的, 例如节点A必须位于左上角等, 使用graphviz则很难做到.

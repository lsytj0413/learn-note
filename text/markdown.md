# markdown #

[markdown-guide](https://github.com/lsytj0413/learn-note/blob/master/text/markdown-guide.pdf)

[在线学习网站](http://www.markdowntutorial.com/)

## 引用 ##

只需要在被引用的内容段落开头加上右尖括号 '>' 即可, 可以只在段落第一行加一个, 也可以在每行加一个.

```
> 这一整段的内容都会作为一个HTML的引用元素。
引用元素是会自动优化排版的（reflowable，可回流）。
你可以任意地将引用的内容包含进来，然后所有这些都会
被解析成为单独一个引用元素。
```

上述的内容会转换成以下 HTML 内容:

```
<blockquote><p>这一整段的内容都会作为一个HTML的引用元素。引用元素是会自动优化排版的（reflowable，可回流）。
你可以任意地将引用的内容包含进来，然后所有这些都会被解析成为单独一个引用元素。</p></blockquote>
```

引用可以嵌套, 如果需要在一个引用里面插入另一个引用, 可以用 >> 开头.

```
> 这是一个引用。这是第一行
这是第二行。
>> 这是一个嵌套的引用。这是第一行。
这是第二行
> 
> 外层引用的第三行。前面需要一个视觉上的空行表示内层嵌套的结束，空行前面的('>')可以有可以没有。
```

## 代码 ##

### 代码块 ###

如果将每一行都缩进一个TAB或者4个空格, 那么这些行就会被作为代码块插入文档. 在代码块中的 &符号 以及尖括号在输出为 HTML 时会被转换为相对应的 HTML 实体符号.

```
If you want to mark something as code, indent it by 4 spaces.
    <p>This has been indented 4 spaces.</p>
```

也可以将代码块用 '符号包含, 其中在开始行之前使用3个 '符号, 在结尾行之后使用3个 '符号.

### 代码行 ###

如果需要在某一行中插入一点代码, 那么将代码文本放入反引号之内包含即可.

```
Markdown is a `<em>text-to-html</em>` conversion tool for writers.
```

## 强调 ##

### 斜体 ###

使用 * 或者 _ 符号将文本包含起来, 那么文本就会被显示为_斜体_.

```
This is *emphasized* _text_.
```

### 加黑 ###

使用 ** 或者 __ 符号将文本包含起来, 那么文本就会被显示为 __加黑__.

```
This is very heavily **emphasized** __text__.
```

## 标题 ##

可以在标题内容前输入特定数量的井号 # 来实现对应级别的HTML样式的标题(HTML提供六级标题).

```
# First-level heading
#### Fourth-level heading
```

## 水平线 ##

要生成水平分区线, 可以在单独一行里输入3个或以上的短横线, 星号或者下划线实现, 短横线和星号之间可以输入任意空格. 以下每一行都产生一条水平分区线.

```
* * *
***
*****
- - -
---------------------------------------
```

## 图片 ##

图片链接的语法和普通链接语法类似, 只是在前面加上一个 !符号即可.

```
![alt text](http://path/to/img.jpg "Title")
```

## 换行 ##

在文本中输入的换行会从最终生成的结果中删除, 浏览器会根据可用空间自动换行. 如果想强迫换行, 可以在行尾插入至少两个空格.

## 链接 ##

### 行内链接 ###

在某一行插入链接的语法如下:

```
This is an [example link](http://example.com/ "With a Title").
```

其中括号内的标题文本是可选的.

### 引用链接 ###

可以使用引用链接来引用文本中的其他地方定义的链接.

```
This is a guide on Markdown [Markdown][1].

[1]: http://en.wikipedia.org/wiki/Markdown "Markdown"
```

## 列表 ##

### 有序列表 ###

有序列表使用数字接着一个英文句点作为列表标记.

```
1.  Bird
2.  McHale
3.  Parish
```

### 无序列表 ###

无序列表使用 *, + 或者 - 这三个符号作为列表标记.

```
+ One
- Two
* Three
```

### 嵌套列表 ###

可以在列表中再次嵌入列表, 被嵌入的列表相对于上层列表需要再次缩进4个空格.

```
+ One
+ Two
+ Three
    - Nested One
    - Nested Two
```

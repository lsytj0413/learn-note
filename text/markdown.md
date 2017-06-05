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

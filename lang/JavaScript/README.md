# JavaScript 笔记 #

## 1 简介 ##

### 1.1 历史 ###

在上个世纪的 1995 年, Brendan Eich 在两周之内设计出了 JavaScript 语言，

### 1.2 ECMAScript ###

为了让 JavaScript 成为全球标准, 几个公司联合 ECMA 组织定制了 JavaScript 语言的标准, 被称为 ECMAScript 标准.

### 1.3 JavaScript 版本 ###

最新的 ES6 已经在 2015年6月正式发布.

## 2 快速入门 ##

JavaScript 代码可以直接嵌入网页的任何地方, 例如常见的放到 head 中:

```
<html>
    <head>
        <script>
            alert("Hello, world");
        </script>
    </head>
    <body>
        
    </body>
</html>
```

还可以将 JavaScript 代码保存到单独的 .js 文件, 然后再引入:

```
<html>
    <head>
        <script src="/static/js/abc.js" type="text/javascript">
        </script>
    </head>
    <body>

    </body>
</html>
```

其中的 type 字段可以省略.

### 如何编写 JavaScript ###

可以使用任何文本编辑器来编写 JavaScript 代码, 例如:

- Visual Studio Code
- Sublime Text
- Notepad++

### 如何运行 JavaScript ###

要让浏览器运行 JavaScript 必须先有一个 HTML 页面, 然后在页面中引入 JavaScript 即可.

### 调试 ###

可以使用 Chrome 来调试 JavaScript 代码:

1. 安装 Chrome
2. 在页面点击 F12 打开开发者工具

### 2.1 基本语法 ###

#### 2.1.1 语法 ####

JavaScript 语法类似 Java 语言的语法, 每个语句以 ; 结束, 语句块使用大括号包围.

```
if (2 > 1) {
    x = 1;
    y = 2;
    z = 3;
    if (x < y) {
        z = 4;
    }
    if (x > y) {
        z = 5;
    }
}
```

#### 2.1.2 注释 ####

以 // 开头直到行尾的字符被视为行注释, 也可以用 /* .. */ 把多行字符包裹起来作为块注释.

#### 2.1.3 大小写 ####

JavaScript 严格区分大小写.

### 2.2 数据类型和变量 ###

#### 2.2.1 Number ####

JavaScript 不区分整数和浮点数, 统一用 Number 表示:

```
123; // 整数123
0.456; // 浮点数0.456
1.2345e3; // 科学计数法表示1.2345x1000，等同于1234.5
-99; // 负数
NaN; // NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity; // Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值时，就表示为Infinity
```

#### 2.2.2 字符串 ####

字符串是以单引号或双引号括起来的任意文本.

#### 2.2.3 布尔值 ####

包括 true 和 false 两种.

#### 2.2.4 比较运算符 ####

在 JavaScript 中有两种相等运算符:

1. ==: 自动转换数据类型再比较, 一般不应该使用
2. ===: 不自动转换类型

NaN 这个特殊的 Number 和任意其他值都不等, 包括它自己, 需要通过 isNan 函数来判断.

#### 2.2.5 null 和 undefined ####

1. null 表示一个空值
2. undefined 表示未定义

大多数情况下都应该用 null, undefined 仅仅在判断函数参数是否传递的情况下使用.

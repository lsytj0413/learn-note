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

#### 2.2.6 数组 ####

数组用 [] 表示, 元素之间用逗号分隔, 也可以使用 Array() 函数实现. 数组的元素可以通过索引来访问, 默认的索引起始值为0.

#### 2.2.7 对象 ####

JavaScript 的对象是由一组键-值组成的无序集合, 所有的键都是字符串类型, 值可以是任意的数据类型.

#### 2.2.8 变量 ####

变量在 JavaScript 中使用一个变量名表示, 变量名是大小写英文, 数字, $ 和 _ 的组合, 而且不能是数字开头, 也不能是 JavaScript 的关键字. 可以使用如下方式申明一个变量:

```
var a;
```

变量只能使用 var 申明一次.

#### 2.2.9 strict模式 ####

在 JavaScript 中不强制要求用 var 申明变量, 如果一个变量没有通过 var 申明就被使用, 那么该变量自动被申明为全局变量.

为了修复这一设计缺陷, ECMA在后续规范中推出了 strict 模式, 在该模式下的代码强制通过 var 申明变量, 未申明即使用的将导致运行错误. 可以在 JavaScript 代码的第一行加上如下代码启用 strict 模式:

```
'use strict';
```

### 2.3 字符串 ###

JavaScript 的字符串就是用单引号或双引号括起来的字符.

#### 2.3.1 多行字符串 ####

可以使用反引号来表示多行字符串:

```
`这是一个
多行
字符串`;
```

#### 2.3.2 模板字符串 ####

可以使用加号连接多个字符串, 或使用 ES6 新增的模板字符串:

```
var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`;
alert(message);
```

#### 2.3.3 操作字符串 ####

- length: 获取长度
- [index]: 获取指定位置的字符
- toUpperCase(): 转换为大写
- toLowerCase(): 转换为小写
- indexOf(): 搜索指定字符串出现的位置
- substring(): 返回指定索引区间的子串

字符串是不可变的, 如果对字符串的某个索引赋值, 不会有任何错误也不会有任何效果.

### 2.4 数组 ###

JavaScript 的 Array 可以包含任意数据类型, 并通过索引来访问每个元素. 可以通过 length 属性来访问 Array 的长度:

```
var arr = [1, 2, 3.14, "Hello", null, true];
arr.length; // 6

var arr = [1, 2, 3];
arr.length; // 3
arr.length = 6;
arr; // arr变为[1, 2, 3, undefined, undefined, undefined]
arr.length = 2;
arr; // arr变为[1, 2]
```

当通过索引赋值时的索引超出了范围, 也会引起 Array 大小的变化.

常用的 Array 的函数如下:

- indexOf: 搜索一个指定的元素位置
- slice: 截取 Array 的部分元素并返回一个新的 Array
- push: 向末尾添加元素
- pop: 删除最后一个元素
- unshift: 向头部添加元素
- shift: 删除第一个元素
- sort: 排序
- reverse: 反转
- splice: 从指定的索引开始删除若干元素, 然后再从该位置添加若干元素
- concat: 连接当前 Array 和另一个 Array, 并返回一个新的 Array
- join: 把当前 Array 的每个元素都用指定的字符串连接, 然后返回连接后的字符串

### 2.5 对象 ###

JavaScript 的对象是一种无序的集合数据类型, 由若干键值对组成. 

```
var xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};
```

如上所示, 如果属性名包含特殊字符就必须用单引号括起来.

访问不存在的属性会返回 undefined, 而且可以在运行时自由的给一个对象增加或删除属性. 可以用 in 操作符来检查对象是否具有某一属性:

```
var xiaoming = {
    name: '小明'
};
xiaoming.age; // undefined
xiaoming.age = 18; // 新增一个age属性
xiaoming.age; // 18
delete xiaoming.age; // 删除age属性
xiaoming.age; // undefined
delete xiaoming['name']; // 删除name属性
xiaoming.name; // undefined
delete xiaoming.school; // 删除一个不存在的school属性也不会报错

'name' in xiaoming;
xiaoming.hasOwnProperty('name')
```

因为 in 操作符会检查继承得到的属性, 如果要判断是否是自身拥有的, 可以使用 hasOwnProperty 函数.

### 2.6 条件判断 ###

JavaScript 使用 if 来进行条件判断:

```
var age = 20;
if (age >= 18) { // 如果age >= 18为true，则执行if语句块
    alert('adult');
} else { // 否则执行else语句块
    alert('teenager');
}
```

### 2.7 循环 ###

#### for 循环 ####

通过初始条件, 结束条件和递增条件来循环执行语句块:

```
var x = 0;
var i;
for (i=1; i<=10000; i++) {
    x = x + i;
}
x; // 50005000
```

#### for...in 循环 ####

可以使用 for...in 来循环一个对象的所有属性:

```
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    if (o.hasOwnProperty(key)) {
        console.log(key); // 'name', 'age', 'city'
    }
}
```

#### while 循环 ####

```
var x = 0;
var n = 99;
while (n > 0) {
    x = x + n;
    n = n - 2;
}
x; // 2500
```

#### do...while 循环 ####

```
var n = 0;
do {
    n = n + 1;
} while (n < 100);
n; // 100
```

### 2.8 Map 和 Set ###

#### Map ####

在 JavaScript 对象中键必须是字符串. ES6 规范引入了新的数据类型 Map, 它的键可以是多种数据类型.

可以使用如下的方式来初始化一个 Map:

```
var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael'); // 95

var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined
```

#### Set ####

Set 是一组 key 的集合, 而且 key 不能重复.

```
var s2 = new Set([1, 2, 3]); // 含1, 2, 3

s.add(4);
s; // Set {1, 2, 3, 4}
s.add(4);
s; // 仍然是 Set {1, 2, 3, 4}
s.delete(3);
```

### 2.9 iterable ###

ES6 标准引入了新的 iterable 类型, Array, Map 和 Set 都属于 iterable 类型, 具有 iterable 类型的集合可以通过 for ... of 循环来遍历.

```
var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) { // 遍历Array
    console.log(x);
}
for (var x of s) { // 遍历Set
    console.log(x);
}
for (var x of m) { // 遍历Map
    console.log(x[0] + '=' + x[1]);
}
```

for ... in 循环遍历的是对象的属性名称, 而 for...of 循环只遍历集合本身的元素:

```
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
    console.log(x); // '0', '1', '2', 'name'
}
for (var x of a) {
    console.log(x); // 'A', 'B', 'C'
}
```

可以使用 iterable 内置的 forEach 方法(ES5.1引入)来遍历集合:

```
var a = ['A', 'B', 'C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    console.log(element + ', index = ' + index);
});

var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    console.log(element);
});

var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    console.log(value);
});
```

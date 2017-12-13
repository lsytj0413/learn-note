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

## 3 函数 ##

### 3.1 函数定义和调用 ###

#### 3.1.1 定义函数 ####

定义一个函数的方式如下:

```
function abs(x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```

其中:

- function 指出这是一个函数定义
- abs 是函数的名称
- (x) 括号内列出函数的参数, 多个参数使用逗号分割
- 大括号内部的代码是函数体

上述的定义方式也等价于如下的方式:

```
var abs = function (x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
};
```

#### 3.1.2 调用函数 ####

调用函数时按顺序传入参数即可:

```
abs(10); // 返回10
abs(-9); // 返回9
```

JavaScript 允许传入任意个参数而不影响调用, 因此可以传入多或者少的参数, 没有传入的参数被赋值为 undefined:

```
abs(10, 'blablabla'); // 返回10
abs(-9, 'haha', 'hehe', null); // 返回9

abs(); // 返回NaN
```

如果要避免收到 undefined, 可以对参数进行检查:

```
function abs(x) {
    if (typeof x !== 'number') {
        throw 'Not a number';
    }
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
}
```

#### 3.1.3 arguments ####

JavaScript 的关键字 arguments 只在函数内部起作用, 并且永远指向当前函数的调用者传入的所有参数. arguments 类似 Array 但并不是一个 Array:

```
function abs() {
    if (arguments.length === 0) {
        return 0;
    }
    var x = arguments[0];
    return x >= 0 ? x : -x;
}

abs(); // 0
abs(10); // 10
abs(-9); // 9
```

#### 3.1.4 rest参数 ####

ES6 引入了 rest 参数来获取额外的参数:

```
function foo(a, b, ...rest) {
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}

foo(1, 2, 3, 4, 5);
// 结果:
// a = 1
// b = 2
// Array [ 3, 4, 5 ]

foo(1);
// 结果:
// a = 1
// b = undefined
// Array []
```

### 3.2 变量作用域与结构赋值 ###

JavaScript 的函数在查找变量时从自身函数定义开始, 从内向外查找. 如果内部函数定义了与外部函数重名的变量, 则内部函数的变量将屏蔽外部函数的变量.

#### 3.2.1 变量提升 ####

JavaScript 会先扫描整个函数的语句, 并把所有申明的变量提升到函数顶部(只提升申明, 不提升赋值):

```
'use strict';

function foo() {
    var x = 'Hello, ' + y;
    console.log(x);
    var y = 'Bob';
}

foo();
```

等价于:

```
function foo() {
    var y; // 提升变量y的申明，此时y为undefined
    var x = 'Hello, ' + y;
    console.log(x);
    y = 'Bob';
}
```

#### 3.2.2 全局作用域 ####

不在任何函数内定义的变量就具有全局作用域, JavaScript 默认有一个全局对象 window, 全局作用域的变量实际上被绑定到 window 的一个属性.

JavaScript 只有一个全局作用域, 任何变量(包括函数) 如果没有在当前函数作用域中找到, 就会继续向上查找直到全局作用域, 如果仍然没有找到则报 ReferenceError 错误.

#### 3.2.3 名字空间 ####

全局变量会绑定到 window 上容易造成命名冲突, 减少冲突的一个方法是把自己的所有变量和函数全部绑定到一个全局变量中.

#### 3.2.4 局部作用域 ####

ES6 引入了新的关键字 let, 可以申明一个块级作用域.

#### 3.2.5 常量 ####

ES6 标准引入了新的关键字 const 来定义常量, const 具有块级作用域.

#### 3.2.6 解构赋值 ####

从 ES6 开始 JavaScript 引入了解构赋值, 可以同时对一组变量进行赋值.

```
let [x, [y, z]] = ['hello', ['JavaScript', 'ES6']];
let [, , z] = ['hello', 'JavaScript', 'ES6']; // 忽略前两个元素，只对z赋值第三个元素
```

也可以用解构赋值从一个对象中取出若干属性:

```
var person = {
    name: '小明',
    age: 20,
    gender: 'male',
    passport: 'G-12345678',
    school: 'No.4 middle school',
    address: {
        city: 'Beijing',
        street: 'No.1 Road',
        zipcode: '100001'
    }
};
var {name, address: {city, zip}} = person;
```

使用解构赋值对象属性时, 如果对应的属性不存在则变量被赋值为 undefined. 也可以使用以下的语法指定解构的变量名和默认值:

```
// 把passport属性赋值给变量id:
let {name, passport:id} = person;

// 如果person对象没有single属性，默认赋值为true:
var {name, single=true} = person;
```

如果已经声明了变量则有时赋值会报错:

```
// 声明变量:
var x, y;
// 解构赋值:
{x, y} = { name: '小明', x: 100, y: 200};
// 语法错误: Uncaught SyntaxError: Unexpected token =
```

这是因为 JavaScript 引擎把大括号开头的语句作为块处理, 于是赋值不再合法. 可以用小括号把整个语句括起来:

```
({x, y} = { name: '小明', x: 100, y: 200});
```

### 3.3 方法 ###

在一个对象中绑定函数, 称为这个对象的方法.

```
var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var y = new Date().getFullYear();
        return y - this.birth;
    }
};

xiaoming.age; // function xiaoming.age()
xiaoming.age(); // 今年调用是25,明年调用就变成26了
```

在一个方法内部, this 是一个特殊变量, 它始终指向当前对象. 但是如果修改为如下代码:

```
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 25, 正常结果
getAge(); // NaN
```

在上面的代码中单独调用 getAge 函数时返回了 NaN. 在 JavaScript 的函数内部如果使用了 this, 那么 this 的值分为以下的情况:

- 以对象的方法形式调用(xx.yy()), 那么该函数的 this 指向被调用的对象
- 单独的函数调用, 那么 this 指向全局对象即 window, 即使是如下的形式的代码：

```
var fn = xiaoming.age; // 先拿到xiaoming的age函数
fn(); // NaN
```

ECMA 规定, 在 strict 模式下让函数的 this 指向 undefined. 如果代码如下:

```
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - this.birth;
        }
        return getAgeFromBirth();
    }
};

xiaoming.age(); // Uncaught TypeError: Cannot read property 'birth' of undefined
```

上面的代码会抛出错误, 因为在 age 函数内部定义的函数, this 又指向的 undefined. 可以采用如下方式修复:

```
'use strict';

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var that = this; // 在方法内部一开始就捕获this
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - that.birth; // 用that而不是this
        }
        return getAgeFromBirth();
    }
};

xiaoming.age(); // 25
```

#### 3.3.1 apply ####

可以使用函数本身的 apply 方法来控制 this 的指向:

```
function getAge() {
    var y = new Date().getFullYear();
    return y - this.birth;
}

var xiaoming = {
    name: '小明',
    birth: 1990,
    age: getAge
};

xiaoming.age(); // 25
getAge.apply(xiaoming, []); // 25, this指向xiaoming, 参数为空
```

call 函数的作用与 apply 类似, 区别是:

- apply 函数把参数打包成 Array 再传入
- call 把参数按顺序传入

#### 3.3.2 装饰器 ####

可以利用 apply 来动态的改变函数的行为:

```
'use strict';

var count = 0;
var oldParseInt = parseInt; // 保存原函数

window.parseInt = function () {
    count += 1;
    return oldParseInt.apply(null, arguments); // 调用原函数
};
```

### 3.4 高阶函数 ###

当一个函数可以接收另一个函数作为参数, 这种函数就称为高阶函数.

```
function add(x, y, f) {
    return f(x) + f(y);
}
```

#### 3.4.1 map/reduce ####

##### map #####

map 方法定义在 JavaScript 的 Array 中, 可以将一个函数作用于 Array 的每一个元素并把结果生成一个新的 Array.

```
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
arr.map(String); // ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

##### reduce #####

reduce 把一个函数作用在 Arrat 上, 该函数接收两个参数, reduce 把结果继续和下一个元素做累积计算.

```
ar arr = [1, 3, 5, 7, 9];
arr.reduce(function (x, y) {
    return x + y;
}); // 25
```

#### 3.4.2 filter ####

filter 用于把 Array 的某些元素过滤掉, 然后返回剩下的元素.

```
var arr = [1, 2, 4, 5, 6, 9, 10, 15];
var r = arr.filter(function (x) {
    return x % 2 !== 0;
});
r; // [1, 5, 9, 15]
```

filter 接收的函数可以有多个参数:

```
var arr = ['A', 'B', 'C'];
var r = arr.filter(function (element, index, self) {
    console.log(element); // 依次打印'A', 'B', 'C'
    console.log(index); // 依次打印0, 1, 2
    console.log(self); // self就是变量arr
    return true;
});
```

#### 3.4.3 sort ####

Array 的 sort 方法默认把所有元素先转换为 string 再进行排序. sort 是一个高阶函数, 可以接收一个比较函数来实现自定义的排序:

```
var arr = [10, 20, 1, 2];
arr.sort(function (x, y) {
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
});
console.log(arr); // [1, 2, 10, 20]
```

### 3.5 闭包 ###

#### 3.5.1 函数作为返回值 ####

高阶函数除了可以接受函数作为参数外, 还可以把函数作为结果值返回:

```
function lazy_sum(arr) {
    var sum = function () {
        return arr.reduce(function (x, y) {
            return x + y;
        });
    }
    return sum;
}

var f = lazy_sum([1, 2, 3, 4, 5]); // function sum()
f();
```

在上面的例子中, sum 函数可以引用外部函数 lazy\_sum 的参数和局部变量, 当 lazy\_sum 返回函数 sum 时, 相关参数和变量都保存在返回的函数中, 这种结构称为闭包.

#### 3.5.2 闭包 ####

再看一个例子:

```
function count() {
    var arr = [];
    for (var i=1; i<=3; i++) {
        arr.push(function () {
            return i * i;
        });
    }
    return arr;
}

var results = count();
var f1 = results[0];
var f2 = results[1];
var f3 = results[2];

f1(); // 16
f2(); // 16
f3(); // 16
```

上面的代码之所以全部输出 16 , 是因为当 3 个函数都返回时它们所引用的变量 i 已经变成了 4, 所以结果是 16. 在使用闭包时应该注意: 返回函数不要引用任何循环变量, 或者是后续会发生变化的变量.

可以通过如下方式来解决上个问题:

```
function count() {
    var arr = [];
    for (var i=1; i<=3; i++) {
        arr.push((function (n) {
            return function () {
                return n * n;
            }
        })(i));
    }
    return arr;
}
```

这是因为当函数被调用时, 已经绑定到函数参数的值就会确定.

### 3.6 箭头函数 ###

#### 3.6.1 箭头函数 ####

ES6 新增了一种新的函数: 箭头函数. 定义如下:

```
x => x * x

// 相当于
function (x) {
    return x * x;
}
```

箭头函数相当于匿名函数, 并且简化了函数定义. 当函数体包含多条语句时, 大括号和 return 语句不能省略, 如果参数不只一个则可以将参数列表用小括号包围起来.

```
// 可变参数:
(x, y, ...rest) => {
    var i, sum = x + y;
    for (i=0; i<rest.length; i++) {
        sum += rest[i];
    }
    return sum;
}
```

#### 3.6.2 this ####

箭头函数和匿名函数还有个明显的区别: 箭头函数内部的 this 是词法作用域, 由上下文确定. 例如在如下的代码中:

```
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = () => new Date().getFullYear() - this.birth; // this指向obj对象
        return fn();
    }
};
obj.getAge(); // 25
```

箭头函数中的 this 指向外层调用者 obj, 而且用 call 或者 apply 调用箭头函数时, 无法对 this 进行绑定, 即传入的第一个参数被忽略.

### 3.6 generator ###

generator 是 ES6 标准引入的新的数据类型, 一个 generator 看上去像一个函数, 但可以返回多次. 一个简单的 generator 函数如下:

```
function* foo(x) {
    yield x + 1;
    yield x + 2;
    return x + 3;
}
```

generator 由 function* 定义, 并且除了 return 语句还可以用 yield 返回多次. 例如一个生成斐波那契数列的生成器如下:

```
function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 0;
    while (n < max) {
        yield a;
        [a, b] = [b, a + b];
        n ++;
    }
    return;
}

var f = fib(5);
f.next(); // {value: 0, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 1, done: false}
f.next(); // {value: 2, done: false}
f.next(); // {value: 3, done: false}
f.next(); // {value: undefined, done: true}
```

在 generator 中每次遇到 yield x; 就会返回一个对象 {value: x, done: true/false}, 然后暂停 generator 函数. 当 done 返回 true 时就不能在继续调用 next 了.

也可以使用 for...of 循环迭代 generator 对象, 这种方式不需要自己判断 done.

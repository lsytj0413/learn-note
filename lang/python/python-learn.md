# Python知识点 #

## 基础 ##

### 语句与表达式 ###

语句与表达式的区别如下:

1. 表达式是对某件事的描述, 例如 2*2 是表达式
2. 语句是指做某件事, 即告诉计算机做什么, 而且语句一般改变了事物.

### 通用序列操作 ###

1. 索引
2. 分片
3. 加法
4. 乘法
5. 成员资格
6. 长度, 最小值和最大值

### 列表操作 ###

1. 元素赋值
2. 删除元素, del l[x]
3. 分片赋值, name[1:3] = list('python')
4. append, count, extend, index, insert, pop, remove, reverse, sort

```
# 1.3
names = list('python')
print names[1::2]

names[1:3] = list('cpp')
print names

names = list('python')
names[1::2] = list('cpp')
print names
```

### 字符串操作 ###

1. find
2. join
3. lower
4. replace
5. split
6. strip
7. translate

### 字典操作 ###

1. clear
2. copy, deepcopy
3. fromkeys
4. get
5. has_key, python3中应该使用in
6. items, iteritems
7. keys, iterkeys
8. pop, popitem
9. setdefault
10. update
11. values, itervalues

```
# 1.5
names = {
    '1': 1,
    '2': 2
}
for k, v in names.iteritems():
    print k, v
    pass
```

## 高级特性 ##

### 迭代工具 ###

1. zip, 同时迭代多个序列
2. enumerate, 按索引迭代
3. reversed, sorted, 翻转和排序迭代

```
# 2.1

print zip([1, 2, 3], [2, 3, 4, 5], [7, 8])
print list(enumerate([5, 6, 7, 8]))
```

### 列表推导式 ###

1. [ xx for yy in zz if jj]

```
# 2.2

print [x*x for x in range(10) if x % 3 == 0]
print [(x, y) for x in range(3) for y in range(3)]
```

### 函数 ###

1. 默认值和关键字参数
2. 收集参数

```
# 2.3

def hello_1(name, g = 'Hello'):
    print g, name

hello_1('xxx')
hello_1('xxx', 'yyy')
hello_1(name='xxx')
hello_1(**{'name': 'dict'})
hello_1(**{'name': 'dict', 'g': 'dict'})

def hello_1_wrapper(**args):
    print 'hello_1_wrapper', args
    hello_1(**args)
    pass

hello_1_wrapper(**{'name': 'dict'})
hello_1_wrapper(**{'name': 'dict', 'g': 'dict'})

def hello_2(name, *g):
    print name, g

def hello_2_wrapper(name, *g):
    print 'hello_2_wrapper', g
    hello_2(name, *g)
    pass

hello_2('xxx')
hello_2_wrapper('xxx')
hello_2('xxx', 'yyy')
hello_2('xxx', 'yyy', 'zzz')
hello_2_wrapper('xxx', 'yyy')
hello_2_wrapper('xxx', 'yyy', 'zzz')
```

## 面向对象 ##

### 类 ###

1. 私有化: Python并不直接支持该特性, 可以在它的名字前加上双下划线即可, 类定义中所有以双下划线开始的名字都被翻译成前面加上单下划线和类名的形式
2. 类的定义就是执行代码块. 类作用域内的变量可以被所有实例访问
3. issubclass, 新式类可以使用type(s)查看实例所属的类
4. hasattr, getattr, setattr
5. 新式类, 使用super

```
# 3.1
class A(object):

    __a = 0

    def __init__(self):
        self.__b = 1

print A._A__a
print A()._A__b

class B(object):
    i = 0

print B.i
v1 = B()
print v1.i
v2 = B()
print v2.i

B.i = 10
print v1.i
print v2.i
```

### 异常 ###

1. 引发异常: raise

```
try:
    pass
except:
    pass
finally:
    pass
else:
    pass
```

### 魔法方法 ###

1. 在名称前后都有两个下划线
2. __init__, 构造方法
3. 序列和映射规则: __len__, __getitem__, __setitem__, __delitem__
4. 可以子类化内建类型
5. property
6. 类方法和静态方法
7. attr

```
# 3.3
def checkIndex(key):
    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence(object):

    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        checkIndex(key)

        try:
            return self.changed[key]
        except KeyError:
            return self.start + key*self.step

    def __setitem__(self, key, value):
        checkIndex(key)

        self.changed[key] = value

s = ArithmeticSequence()
print s[4]
s[4] = 2
print s[4]


class Rectangle(object):

    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, s):
        self.width, self.height = s

    def getSize(self):
        return self.width, self.height

    size = property(getSize, setSize)

o = Rectangle()
print o.size
o.size = (5, 10)
print o.size

class MyClass(object):

    @staticmethod
    def smeth():
        print 'staticmethod'

    @classmethod
    def cmeth(cls):
        print 'classmethod', cls

MyClass.smeth()
MyClass.cmeth()
```

### 属性 ###

1. __getattribute__(self, name): 当特性name被访问时使用, 新式类, 同时拦截对__dict__的访问, 在该函数中访问与self相关的属性时, 使用super函数是唯一安全的路径
2. __getattr__(self, name): 当特性name被访问且对象没有相应的特性时使用
3. __setattr__(self, name, value): 当试图给特性name赋值时调用
4. __delattr__(self, name): 当试图删除特性name时调用


```
# 3.4
class Rectangle2(object):

    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value # 避免递归死循环

    def __getattr__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError

o = Rectangle2()
print o.size
o.size = (5, 10)
print o.size
```

### 迭代器 ###

1. __iter__方法返回一个迭代器, 实现了方法则代表对象是可迭代的
2. 迭代器是实现了next方法的对象, python3中则是__next__

```
# 3.5
class Fibs(object):

    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
for f in Fibs():
    if f > 10:
        break
    print f
```

### 生成器 ###

生成器是一种用普通的函数语法定义的迭代器. 任何包含yield语句的函数都是生成器, 每次产生一个值(yield), 函数都会被冻结在该点, 并等待重新唤醒
生成器推导式相似于列表推导式, 返回的是生成器而不是列表, 外围使用() 而不是 []. 生成器推导式可以在当前圆括号内直接使用, 不用增加另外的括号

当生成器函数被调用时函数体中的代码不会被执行, 而是返回一个迭代器. 每次请求一个值, 就会执行生成器中的代码.

生成器方法:
1. 访问生成器的send方法, 向生成器发送消息
2. throw方法: 在生成器内部引发一个异常(yield表达式中)
3. close方法: 停止生成器, 引发一个GeneratorExit异常. 在生成器close之后再次使用则引发RuntimeError异常

```
# 3.6

def flatten(nested):
    try:
        try:
            nested + ""
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for e in flatten(sublist):
                yield e
    except TypeError:
        yield nested

print list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8]))

def repeator(value):
    while True:
        new  = (yield value)
        if new is not None:
            value = new
r = repeator(42)
print r.next()
print r.send('Hello world!')
```

## 其他 ##

### 模块和包 ###

1. 模块是一个文件. 导入一次和导入多次效果相同
2. 包是另一类模块, 可以包含其他模块. 当模块存储在文件中时, 包就是模块所在的目录, 而且它必须包含一个 __init__.py文件.

假设有以下包:
~/python/drawing/
~/python/drawing/__init__.py
~/python/drawing/colors.py
~/python/drawing/shapes.py

则:
import drawing               # __init__.py模块可用
import drawing.colors        # colors模块可用
from drawing import shapes   # shapes可用

__all__ 变量: 定义模块公有接口. 如果没有设置__all__, 则import *会导入模块中所有不以下划线开头的全局名称
__file__属性: 模块路径

### 标准库 ###

1. sys
2. os
3. fileinput: 轻松遍历文件所有行
4. 集合set(语言内建), frozenset(不可变集合)
5. heapq, 堆
6. collections.deque, 双端队列
7. time
8. random
9. shelve, 简单存储
10. re, 正则表达式
11. functools, difflib, hashlib, csv, timeit, profile, trace, datetime, itertools, logging, getopt, optparse, cmd

### 文件和流 ###

上下文管理器: 一种支持__enter__和__exit__这两个方法的对象, __enter__无参, 返回值绑定到as之后的变量, __exit__带三个参数(异常类型, 异常对象和异常回溯), 如果返回false则异常不被处理

1. 使用fileinput实现懒惰行迭代
2. 文件对象是可迭代的

### 高阶函数 ###

1. map, reduce
2. filter
3. 匿名函数: 只能有一个表达式, 不能有return

```
# 4.4
print map(lambda x: x+2, [1, 2, 3])
print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print filter(lambda x: x > 2, [2, 4, 5, 6, 7, 1, 3, 1, 2])
```

### 装饰器 ###

函数对象的__name__属性可以拿到函数的名字.
在代码运行期间动态增加功能的方式称为装饰器, 本质上是一个返回函数的高阶函数

```
# 4.5
def log(fn):
    def wrapper(*arg, **kw):
        print 'call {}'.format(fn.__name__)
        return fn(*arg, **kw)
    return wrapper

@log
def now():
    print 'now'
now()
print now.__name__

import functools
def log2(text):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*arg, **kw):
            print 'call {}, {}'.format(fn.__name__, text)
            return fn(*arg, **kw)
        return wrapper
    return decorator

@log2('log2text')
def now2():
    print 'now2'
now2()
print now2.__name__
```

### 偏函数 ###

functools模块的功能

```
# 4.6
import functools
int2 = functools.partial(int, base=2)
print int2('1000')
```

### 类装饰器 ###

```
# 4.7
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()
```

### MRO ###

http://www.360doc.com/content/16/0719/18/34574201_576833790.shtml

MRO: Method Resolution Order, 方法解析顺序. 当使用python中的多重继承时, 解决二义性问题

在python新式类中, MRO的顺序C3算法. 采用拓扑排序访问顺序.

解决单调性: 保证从根到叶, 从左到右的访问顺序
解决重写: 先访问子类, 再访问父类

首先找入度为0的点，只有一个A，把A拿出来，把A相关的边剪掉，再找下一个入度为0的点，有两个点（B,C）,取最左原则，拿B，这是排序是AB，然后剪B相关的边，这时候入度为0的点有E和C，取最左。这时候排序为ABE，接着剪E相关的边，这时只有一个点入度为0，那就是C，取C，顺序为ABEC。剪C的边得到两个入度为0的点（DF），取最左D，顺序为ABECD，然后剪D相关的边，那么下一个入度为0的就是F，然后是object。那么最后的排序就为ABECDFobject。

```
# 4.8
class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

class C(D, F):
    pass

class B(E, D):
    pass

class A(B, C):
    pass

print A.__mro__
```

### 元类 ###

http://blog.jobbole.com/21351/

在Python中, 类也是一种对象. 只要你使用class关键字, Python解释器在执行时
就会创建一个对象. 这个类对象自身拥有创建对象实例的能力.

可以在函数中创建类(通过class关键字), 也可以通过type函数.
type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
你可以看到，在Python中，类也是对象，你可以动态的创建类。这就是当你使用关键字class时Python在幕后做的事情，而这就是通过元类来实现的。

什么是元类:
元类就是用来创建类的东西. type函数实际上是一个元类.
Python会在类的定义中寻找__metaclass__属性，如果找到了，Python就会用它来创建类Foo，如果没有找到，就会用内建的type来创建这个类。
你可以在__metaclass__中放置些什么代码呢？答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。
元类的主要目的就是为了当创建类时能够自动地改变类。通常，你会为API做这样的事情，你希望可以创建符合当前上下文的类。假想一个很傻的例子，你决定在你的模块里所有的类的属性都应该是大写形式。有好几种方法可以办到，但其中一种就是通过在模块级别设定__metaclass__。

```
# 4.9
class ObjectCreator(object):
    pass

print ObjectCreator
print hasattr(ObjectCreator, 'new_attr')
print id(ObjectCreator)

def choose_class(name):
    if name == 'Foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar
print choose_class('Foo')

MyShinyClass = type('MyShinyClass', (object, ), {'bar': True})
print MyShinyClass
print MyShinyClass.__class__

# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr  #  这会作用到这个模块中的所有类


# 请记住，'type'实际上是一个类，就像'str'和'int'一样
# 所以，你可以从type继承
# class UpperAttrMetaClass(type):
#     # __new__ 是在__init__之前被调用的特殊方法
#     # __new__是用来创建对象并返回之的方法
#     # 而__init__只是用来将传入的参数初始化给对象
#     # 你很少用到__new__，除非你希望能够控制对象的创建
#     # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
#     # 如果你希望的话，你也可以在__init__中做些事情
#     # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
#     def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
#         attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
#         uppercase_attr = dict((name.upper(), value) for name, value in attrs)
#         return type(future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaclass(type):

    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    __metaclass__ = UpperAttrMetaclass
    bar = 'bip'

print hasattr(Foo, 'BAR')


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
```

## 其他 ##

### slot ###

可以使用 \_\_slot\_\_ 限制实例的属性(只对当前类生效):

```
class Student(object):
    __slots__ = ('name', 'age')
```

### 枚举类 ###

```
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0
```

## Python3 ##

### 异步IO ###

#### 协程 ####

Python 对协程的支持是通过 generator 实现的, 来看一个生产者消费者的例子:

```
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
```

#### asyncio ####

Python3.4 引入的标准库, 内置对异步 IO 的支持.

```
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
```

使用 @asyncio.coroutine 将一个 generator 标记为 coroutine 类型, 并通过 yield from 调用另一个 generator.

```
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

#### async/await ####

Python3.5 引入的新语法, 等价于:

- async 等价于 @asyncio.coroutine
- await 等价于 yield from


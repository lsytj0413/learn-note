# coding=utf-8

"""
一些Python的代码
"""

"""
语句与表达式的区别:

1: 表达式是某件事件. 例如 2*2 是表达式

2: 语句是做某件事件, 即告诉计算机做什么. 而语句一般改变了事物.

"""

"""
通用序列操作:

1. 索引
2. 分片
3. 加法
4. 乘法
5. 成员资格
6. 长度, 最小值和最大值
"""

"""
列表操作:

1. 元素赋值
2. 删除元素, del l[x]
3. 分片赋值, name[1:3] = list('python')
4. append, count, extend, index, insert, pop, remove, reverse, sort
"""

names = list('python')
print names[1::2]

names[1:3] = list('cpp')
print names

names = list('python')
names[1::2] = list('cpp')
print names

"""
字符串:

1. find
2. join
3. lower
4. replace
5. split
6. strip
7. translate
"""

"""
字典:

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
"""

names = {
    '1': 1,
    '2': 2
}
for k, v in names.iteritems():
    print k, v
    pass


"""
迭代工具:

1. zip, 同时迭代多个序列
2. enumerate, 按索引迭代
3. reversed, sorted, 翻转和排序迭代
"""

print zip([1, 2, 3], [2, 3, 4, 5], [7, 8])
print list(enumerate([5, 6, 7, 8]))

"""
列表推导式:

1. [ xx for yy in zz if jj]
"""

print [x*x for x in range(10) if x % 3 == 0]
print [(x, y) for x in range(3) for y in range(3)]

"""
函数:

1. 默认值和关键字参数
2. 收集参数
"""

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

"""
面向对象:

1. 私有化: Python并不直接支持该特性, 可以在它的名字前加上双下划线即可, 类定义中所有以双下划线开始的名字都被翻译成前面加上单下划线和类名的形式
2. 类的定义就是执行代码块. 类作用域内的变量可以被所有实例访问
3. issubclass, 新式类可以使用type(s)查看实例所属的类
4. hasattr, getattr, setattr
5. 新式类, 使用super
"""

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

"""
异常:

try:pass
except:pass
finally:pass
else:pass

1. 引发异常: raise
"""

"""
魔法方法

1. 在名称前后都有两个下划线
2. __init__, 构造方法
3. 序列和映射规则: __len__, __getitem__, __setitem__, __delitem__
4. 可以子类化内建类型
5. property
6. 类方法和静态方法
7. attr
"""

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


class MyClass(object):

    @staticmethod
    def smeth():
        print 'staticmethod'

    @classmethod
    def cmeth(cls):
        print 'classmethod', cls

MyClass.smeth()
MyClass.cmeth()


"""
__getattribute__(self, name): 当特性name被访问时使用, 新式类, 同时拦截对__dict__的访问, 在该函数中访问与self相关的属性时, 使用super函数是唯一安全的路径
__getattr__(self, name): 当特性name被访问且对象没有相应的特性时使用
__setattr__(self, name, value): 当试图给特性name赋值时调用
__delattr__(self, name): 当试图删除特性name时调用
"""

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


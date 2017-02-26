# coding=utf-8

"""
一些Python的代码
"""

# 1.3
names = list('python')
print names[1::2]

names[1:3] = list('cpp')
print names

names = list('python')
names[1::2] = list('cpp')
print names


# 1.5
names = {
    '1': 1,
    '2': 2
}
for k, v in names.iteritems():
    print k, v
    pass

# 2.1
print zip([1, 2, 3], [2, 3, 4, 5], [7, 8])
print list(enumerate([5, 6, 7, 8]))

# 2.2
print [x*x for x in range(10) if x % 3 == 0]
print [(x, y) for x in range(3) for y in range(3)]

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

# 4.4
print map(lambda x: x+2, [1, 2, 3])
print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print filter(lambda x: x > 2, [2, 4, 5, 6, 7, 1, 3, 1, 2])

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

# 4.6
import functools
int2 = functools.partial(int, base=2)
print int2('1000')

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


# 1个例子

i = 10
def demo1_lambda_on_int(i):
    return lambda : i

x = demo1_lambda_on_int(i)
i = 100
print x()

i = [1, 2]
def demo2_lambda_on_list(i):
    return lambda : i

x = demo2_lambda_on_list(i)
i.append(3)
print x()

i = [0]
print x()


# 例子
i = 10
def demo3_assign_on_int(i):
    i = 30
    print i
demo3_assign_on_int(i)
print i

i = [1, 2]
def demo4_assign_on_list(i):
    i = [0]
    print i
demo4_assign_on_list(i)
print i

i = [1, 2]
def demo5_modify_on_list(i):
    i.append(3)
    print i
demo5_modify_on_list(i)
print i

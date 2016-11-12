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


"""

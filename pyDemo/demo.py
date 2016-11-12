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
5. 成员资格
6. 长度, 最小值和最大值
"""

names = list('python')
print names[1::2]

names[1:3] = list('cpp')
print names

names = list('python')
names[1::2] = list('cpp')
print names

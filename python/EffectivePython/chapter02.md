# 函数 #

## 第14条: 尽量用异常来表示特殊情况, 而不要返回None ##

### 介绍 ###

编写工具函数时, Python程序员会返回None这个特殊值.

```
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

当分母是0时, 该函数会返回None表示这种错误情况. 但是这种情况可能会出现问题, 因为使用者可能不会去判断函数的返回值时None; 
而是会假定, 只要返回了和False等效的结果即表示出错:

```
result = divide(0, 5)
if not result:
    print('Invalid inputs')
```
可见, 令函数返回None可能会使调用它的人写出错误的代码, 有两种办法可以减少这种错误:

1. 返回一个二元组, 分别表示操作结果以及返回值

这种方式需要调用者解析返回的元组, 但是调用者可以通过下划线为名称的变量来跳过操作结果部分.

2. 把异常抛出到上一级函数, 使得调用者必须处理它.

```
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e
```
函数的提供者需要将这种抛出异常的行为写入开发文档. 这样, 调用者无需判断函数的返回值, 这样的代码也比较清晰.

### 要点 ###

1. 返回None来表示特殊意义的函数, 很容易使调用者犯错
2. 函数在遇到特殊情况时应该抛出异常, 并将这种行为写入开发文档

## 第15条: 了解如何在闭包里使用外围作用域中的变量 ##

### 介绍 ###

假设需要实现一个函数对一个全是数字的列表进行排序, 将出现在某个群组之内的数字放在群组之外的数字之前:

```
def sort_priority(values, group):
    def helper(x):
        if x in groups:
            return (0, x)
        return (1, x)
    values.sort(key=helper)
```
这个函数能够正常工作是因为以下3个原因:

1. Python支持闭包, 即一种定义在某个作用域中的函数, 引用了那个作用域里的变量. helper既是一个捕获了groups变量的闭包
2. Python的函数是一级对象
3. Python使用特殊的规则来比较两个元组. 它首先比较下标为0的元素, 如果相等, 然后比较下标为1的元素.

下面对函数再添加一个功能, 即返回是否出现了优先级较高的元素, 下面是一种实现方式:

```
def sort_priority(values, group):
    found = False
    def helper(x):
        if x in groups:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found
```

但是, 这个函数是错误的. 因为, 当表达式中引用变量时, Python按照以下顺序遍历各作用域以解析其引用:

1. 当前函数作用域
2. 任何外围作用域
3. 包含当前代码的模块作用域, 也叫全局作用域(global scope)
4. 内置作用域, 即包含len以及str等函数的作用域

如果以上作用域都没有定义过该变量, 则抛出NameError异常。

给变量赋值时, 规则有所不同: 如果当前作用域有该变量, 则进行赋值; 如果没有, 则视为对变量的定义. 这个原因既是上个实现方式会出现错误的解释.
如果想要实现上述效果, 可以采用如下的方式:

1. Python3 中获取闭包内的数据

```
def sort_priority(values, group):
    found = False
    def helper(x):
        nonlocal found
        if x in groups:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found
```

使用nonlocal语句表明found是上层作用域的变量, 但是这种方式不能延伸到模块级别, 以避免污染全局作用域. 而且该方式只能应用与Python3.

不应该随便使用nonlocal方式, 因为这种副作用难以追踪, 而且在比较长的函数中也难以理解.
如果使用nonlocal的函数太过复杂, 则应该采用辅助类的方式:

```
def sort_priority(values, group):
    class Sorter(object):
        def __init__(self, group):
            self.group = group
            self.found = False
        def __call__(self, x):
            if x in self.group:
                self.found = True
                return (0, x)
            return (1, x)
        
    sorter = Sorter(group)
    values.sort(key=sorter)
    return sorter.found
```

2. Python2

Python2中不支持nonlocal关键字, 为了实现这个功能, 可以利用作用域规则:

```
def sort_priority(values, group):
    found = [False]
    def helper(x):
        nonlocal found
        if x in groups:
            found[0] = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found[0]
```

上述作用域中的变量是字典, 集或者某个类的实例时也同样适用.

### 要点 ###

1. 闭包可以引用外围作用域中的变量
2. 使用默认方式在闭包内对变量赋值, 不会影响外围作用域中的变量
3. 在Python3中可以使用nonlocal关键字引用外围作用域中的变量
4. 在Python2中可以使用可变值来实现与nonlocal相似的功能
5. 除了简单函数, 尽量避免使用nonlocal关键字

## 第16条: 考虑用生成器来改写直接返回列表的函数 ##

### 介绍 ###

### 要点 ###

## 第17条: 在参数上面迭代时, 要多加小心 ##

### 介绍 ###

### 要点 ###

## 第18条: 用数量可变的位置参数减少视觉杂讯 ##

### 介绍 ###

### 要点 ###

## 第19条: 用关键字参数来表达可选的行为 ##

### 介绍 ###

### 要点 ###

## 第20条: 用None和文档字符串来描述具有动态默认值的参数 ##

### 介绍 ###

### 要点 ###

## 第21条: 用只能以关键字形式指定的参数来确保代码明晰 ##

### 介绍 ###

### 要点 ###

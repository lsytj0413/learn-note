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

很多时候当我们需要将一系列结果返回的时候, 一般都是将结果存放在一份列表里.
例如, 查出字符串中每个词的首字母在整个字符串中的索引并返回:

```
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result
```
但是这个函数有两个问题:

1. 这段代码比较拥挤. 每次找到新结果都需要调用append, 但是我们真正应该强调的应该是append的那个值, 而不是对append方法的调用. 函数的首尾还各有一行代码来创建及返回result结果列表.

所以这个函数改用生成器来实现更好. 生成器是使用yield表达式的函数, 调用生成器函数时, 它不会真的运行, 而是会返回迭代器.
每次在这个迭代器上面调用内置的next函数时, 迭代器会把生成器推进到下一个yield表达式那里, 生成器传给yield的每一个值都会由迭代器返回给调用者.

```
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
```

2. index_worlds函数将结果都放在列表里, 如果输出量太大则会将内存耗尽, 而使用生成器可以应对任意长度的输入数据.

使用生成器函数的时候应该注意, 函数返回的迭代器是有状态的, 不应该反复使用它.

### 要点 ###

1. 生成器对比把结果收集到列表中返回的函数更加清晰
2. 由生成器返回的迭代器可以把生成器函数体中传给yield表达式的值逐次产生出来
3. 生成器可以产生一系列输出, 但无论输入量有多大都不会影响它在执行时所耗的内存

## 第17条: 在参数上面迭代时, 要多加小心 ##

### 介绍 ###

如果函数接受的参数是一个列表, 则有可能需要在这个列表上多次迭代.
例如, 假设数据集是每个城市的人数, 现在要统计每个城市的人数占总人数的百分比:

```
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
```
当numbers是一个列表时, 可以得到正确的结果. 为扩大函数应用范围, 现在把人数放在文件里, 然后从文件中读取数据, 使用生成器来实现此功能:

```
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)
```

但是当使用上面的函数来调用 normalize时, 却每个产生任何结果.
这是因为迭代器只能产生一轮结果, 在抛出过StopIteration异常的迭代器或生成器上面继续迭代第二轮是不会有结果的.

而且normalize函数还不会抛出错误, 这是因为for循环, list构造器以及Python标准库里的其他许多函数都认为在正常的操作过程中完全可能出现StopIteration异常.

为解决这个问题, 可以明确的用该迭代器制作一份列表, 即将迭代器遍历一次并复制到新的列表里.

```
def normalize(numbers):
    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
```

这种写法的问题在于, 如果待复制的迭代器中含有大量数据, 则可能会消耗大量内存. 一种解决办法通过参数来接受一个返回新的迭代器的函数:

```
def normalize_func(get_iter):
    total = sum(get_iter())
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result
```
可以这样调用该函数:

```
percentages = normalize_func(lambda : read_visits(path))
```
以上方法能够达到想要的效果, 但是显得比较生硬.
使用一种新编的迭代器协议的容器内也能达到效果: Python在for循环及相关表达式中遍历某种容器时, 就需要依靠这个迭代器协议.
在执行类似for x in foo 这样的语句时, Python实际上会调用iter(foo), 内置的iter函数又会调用foo.\_\_iter\_\_这个特殊方法,
这个方法必须返回迭代器对象, 而那个迭代器对象则实现了名为 \_\_next\_\_的特殊方法, 此后for循环会在迭代器对象上返回调用内置的next函数, 直至其耗尽并产生StopIteration异常.

```
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path
        
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
                
percentages = normalize(ReadVisits(path))
```
我们可以修改normalize函数以确保调用者传进来的参数不是迭代器本身:

```
if iter(numbers) is iter(numbers):
    raise TypeError("Must supply a container")
```

### 要点 ###

1. 当在输入的迭代器参数上多次迭代时可能会导致奇怪的行为并错失某些值
2. Python迭代器协议, 描述了容器和迭代器应该如何与iter和next内置函数, for循环以及相关表达式相互配合
3. 把\_\_iter\_\_方法实现为生成器, 即可定义为自己的容器类型
4. 如果需要判断某个值是迭代器还是容器, 可以拿该值为参数两次调用iter函数, 若结果相同则是迭代器, 调用内置的next函数即可令该迭代器前进一步

## 第18条: 用数量可变的位置参数减少视觉杂讯 ##

### 介绍 ###

令函数接受可选的位置参数(星号参数, *args) 能够使代码更加清晰, 并能减少视觉杂讯:

```
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))
```
上面的函数即使只要打印一条消息也需要手工传入一份空列表, 这种写法即麻烦有杂乱. 最好是能令调用者把第二个参数完全省略掉.
若想在上个函数中实现这个功能, 只需要将第二个参数修改为 *values即可.

接受数量可变的位置参数, 会带来两个问题:

1. 变长参数在传给函数时, 总是会先转换为元组. 这意味着如果用带有 *操作符的生成器为参数来调用这种函数, 那么Python就必须先把该生成器完整的迭代一轮,
并把该生成器完整的迭代一轮, 并把生成器所生成的每一个值放入元组, 这可能会消耗大量内存
2. 如果以后需要给函数添加新的位置参数, 拿就必须修改原来调用该函数的就代码.

### 要点 ###

1. 在def语句中使用 *args, 即可令函数接受位置可变的位置参数
2. 调用函数时, 可以采用 *操作符, 把序列中的元素当成位置参数, 传给该函数
3. 对生成器使用 *操作符, 可能导致程序耗尽内存并崩溃
4. 在已经接受 *args参数的函数上面继续添加位置参数可能会产生难以排查的bug

## 第19条: 用关键字参数来表达可选的行为 ##

### 介绍 ###

### 要点 ###

## 第20条: 用None和文档字符串来描述具有动态默认值的参数 ##

### 介绍 ###

### 要点 ###

## 第21条: 用只能以关键字形式指定的参数来确保代码明晰 ##

### 介绍 ###

### 要点 ###

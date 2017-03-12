# 用Pythonic方式来思考 #

## 第1条: 确认自己所用的Python版本 ##

### 介绍 ###

1. 使用 **python --version** 命令确认所使用的具体的Python版本

2. 通常可以用 **python3** 来运行Python3

3. 通过sys模块查看:

```
import sys
print(sys.version_info)
print(sys.version)
```

### 要点 ###

1. 有两个版本的Python处于活跃状态: Python2和Python3

2. 有多种Python运行时环境, 包括 CPython, Jython, IronPython以及 PyPy

3. 应该优先考虑 Python3

## 第2条: 遵循PEP8风格指南 ##

### 介绍 ###

<Python Enhancement Proposal #8>(8号Python增强提案)又叫[PEP8](http://www.python.org/dev/peps/pep-0008), 它是针对Python代码格式而编订的风格指南.

下面列取几条绝对应该遵守的规则:

#### 空白 ####

1. 使用SPACE表示缩进, 不要使用TAB
2. 和语法相关的每一层缩进都用4个空格表示
3. 每行的字符数不应超过79
4. 对于占用多行的表达式, 除首行的其余行应该在缩进级别之上再加4个空格
5. 文件中的函数和类应该用两个空行隔开
6. 在同一个类中, 各方法之间用一个空行隔开
7. 在使用下标来获取列表元素, 调用函数或给关键字参数赋值的使用, 不用在两旁添加空格
8. 为变量赋值时, 赋值符号的左侧和右侧各加一个空格

#### 命名 ####

1. 函数, 变量和属性应该用小写字母来拼写, 各单词间用下划线分割
2. 受保护的实例属性, 以单个下划线开头
3. 私有的实例属性, 以两个下划线开头
4. 类与异常, 应该以每个单词首字母均大写的形式来命名
5. 模块级别的常量, 应该全部采用大写字母, 各单词间用下划线分割
6. 类中的实例方法, 应该把首个参数名命名为self
7. 类方法的首个参数, 应该命名为cls

#### 表达式和语句 ####

1. 采用内联形式的否定词, 而不要把否定词放在整个表达式的前面, 例如使用 if a is not b 而不是 if not a is b
2. 不要通过检测长度的办法来判断somelist是否为[]或 ''等值, 应该用 if not somelist
3. 不要编写单行的 if, for, while , except等复合语句
4. import 语句总应该放在文件开头
5. 引入模块的时候, 应该使用绝对名称
6. 如果需要以相对名称来import, 应采用 from . import foo这种明确的写法
7. import语句应该分为三个部分, 标准库模块, 第三方模块以及自用模块

### 要点 ###

1. 当编写Python代码时, 总是应该遵循PEP8风格
2. 可以使用pylint对代码进行静态分析

## 第3条: 了解bytes, str与unicode的区别 ##

### 介绍 ###

Python3有两种表示字符序列的类: bytes和str. 前者包含原始的8位值, 后者包含Unicode字符

Python2也有两种表示字符序列的类: str和unicode. str包含原始的8位值, unicode包含Unicode字符

Python3的str以及Python2的unicode没有和特定的二进制编码形式相关联, 要想把unicode字符转换为二进制数据, 需要使用encode方法.

编写Python程序的时候, 一定要把编码的解码操作放在界面的最外围处理, 程序的内部应该使用 unicode字符类型, 且不要对字符编码做任何假设.

Python3中的转换代码如下:

```
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value
    
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value
```

Python2中的转换代码如下:

```
def to_unicode(val):
    if isinstance(val, str):
        value = val.decode('utf-8')
    else:
        value = val
    return value
    
def to_str(val):
    if isinstance(val, unicode):
        value = val.encode('utf-8')
    else:
        value = val
    return value
```

还有以下两个问题需要注意:

1. 在Python2中, 如果str只包含ASCII字符, 则可以近似等价与unicode. 而在Python3中不存在这种等价
2. 在Python3中, 使用open函数获取的文件句柄默认是采用UTF-8编码格式操作, 不同于Python2中采用的二进制形式

### 要点 ###

1. 在Python3中不能混同操作 bytes和str
2. 使用辅助函数进行字符类型的转换
3. 在读取或写入文件二进制数据时, 总是应该采用二进制模式开启文件

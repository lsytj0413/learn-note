# 第六章: 内置模块 #

## 第42条: 用functools.wraps定义函数修饰器 ##

### 介绍 ###

Python使用修饰器来修饰函数, 能够在那个函数执行之前以及执行完毕之后分别运行一些附加代码.

假设要打印某个函数在受到调用时所接收的参数以及该函数的返回值:

```
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper
    
@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return (fibonacci(n - 1) + fibonacci(n - 2))
```
上面的修饰器虽然可以正常运作, 但是修饰器所返回的那个值其名称会和原来的函数不同, 而且help函数也会失效.

这个问题可以使用内置模块functools中名为wraps的辅助函数来解决, 将wraps修饰器运用到wrapper函数之后, 它就会把内部函数相关的重要元数据全部复制到外围函数.

### 要点 ###

1. Python为修饰器提供了专门的语法, 使得程序在运行的时候能够用一个函数来修饰另一个函数
2. 对于调试器这种依靠内省机制的工具, 直接编写修饰器会引发奇怪的行为
3. 内置的functools模块提供了名为wraps的修饰器, 开发者在定义自己的修饰器时应该用wraps对其做一些处理, 以避免一些问题

## 第43条: 考虑以contextlib和with语句来改写可复用的try/finally代码 ##

### 介绍 ###

开发者可以用内置的contextlib模块来处理自己所编写的对象和函数, 使它们能够支持with语句. 该模块提供了名为contextmanager的修饰器, 一个简单的函数只需经过contextmanager修饰即可用在with语句中. 如果按标准方式来做就需要定义新的类, 并提供名为 \_\_enter\_\_ 和 \_\_ext\_\_ 的特殊方法.

```
def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')
    
# 定义一个临时修改日志级别的修饰器
@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)
```
yield表达式所在的地方, 就是with块中的语句所要展开执行的地方. with块所抛出的任何异常都会由yield表达式重新抛出.

```
with debug_logging(logging.DEBUG):
    my_function()
```

传给with语句的那个情境管理器本身也可以返回一个对象, 开发者可以通过with复合语句中的as关键字来指定一个局部变量, Python会把那个对象赋值给这个局部变量.

我们只需要在情境管理器中通过yield语句返回一个值即可.

### 要点 ###

1. 可以用with语句来改写try/finally块中的逻辑, 以便提升复用度并使代码更加整洁
2. 内置的contextlib模块提供了名为contextmanager的修饰器, 开发者只需要用它来修饰自己的函数即可令该函数支持with语句
3. 情境管理器可以通过yield语句向with语句返回一个值, 这个值会赋值给as关键字所指定的变量

## 第44条: 用copyreg实现可靠的pickle操作 ##

### 介绍 ###

内置的pickle模块能够将Python对象序列化为字节流, 也能把这些字节反序列化为Python的内置对象. pickle的设计目标是提供一种二进制流, 使开发者能够在自己所控制的各程序之间传递Python对象.

pickle序列化的结果如果在不同版本间传递, 比如如果新版本增加了新的属性, 老的版本的字节反序列化的结果却不会出现新加的属性. 要解决这个问题, 开发者可以使用 copyreg模块注册一些函数来负责Python对象的序列化操作.

1. 为缺失的属性提供默认值

```
class GameState(object):
    def __init__(self, level=0, lives=4, points=6):
        self.level = level
        self.lives = lives
        self.points = points
        
def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs, )

def unpickle_game_state(kwargs):
    return GameState(**kwargs)
    
copyreg.pickle(GameState, pickle_game_state)
```

2. 用版本号来管理类

通过上面的实现方式, 可以解决增加字段的问题, 但是无法解决移除字段的问题. 因为移除过字段之后, 对旧版本的反序列化操作会传入无效的关键字参数.

解决办法是, 在pickle时向数据中增加一个代表版本号的参数, 反序列时通过版本号来选择不同的操作.

3. 固定的引入路径

在使用pickle模块时, 当类的名称改变之后原有的数据会无法进行反序列化操作, 因为序列化之后的数据会把该对象的引入路径写入数据中.

我们可以给函数指定一个固定的标识符, 令它采用这个标识符来对数据进行unpickle操作, 使得我们在反序列化操作的时候能把原来的数据迁移到名称不同的其他类上面.

```
copyreg.pickle(BetterGameState, pickle_game_state)
```

使用这种copyreg之后, 序列化之后的数据不再包含对象所属类的引入路径, 而是包含unpickle\_game\_state 函数的路径. 所以在这种情况下不能修改这个函数的引入路径.

### 要点 ###

1. 内置的pickle模块只适合在彼此信任的程序之间传递数据
2. 如果用法比较复杂, 那么pickle模块的功能也许就会出现问题
3. 我们可以把内置的copyreg模块和pickle结合使用, 以便为旧的数据添加缺失的属性值, 进行类的版本管理, 并给序列化之后的数据提供固定的引入路径

## 第45条: 应该用datetime模块来处理本地时间, 而不是用time模块 ##

### 介绍 ###

### 要点 ###

## 第46条: 使用内置算法与数据结构 ##

### 介绍 ###

### 要点 ###

## 第47条: 在重视精确度的场合, 应该使用decimal ##

### 介绍 ###

### 要点 ###

## 第48条: 学会安装由Python开发者社区所构建的模块 ##

### 介绍 ###

### 要点 ###

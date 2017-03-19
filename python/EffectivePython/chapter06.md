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

### 要点 ###

## 第44条: 用copyreg实现可靠的pickle操作 ##

### 介绍 ###

### 要点 ###

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

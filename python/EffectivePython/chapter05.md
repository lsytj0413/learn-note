# 第五章: 并发及并行 #

## 第36条: 用subprocess模块来管理子进程 ##

### 介绍 ###

用subprocess模块运行子进程, 读取子进程的输出信息并等待其终止:

```
proc = subprocess.Popen(
           ['echo', 'Hello from the child!'],
           stdout=subprocess.PIPE)
out, err = proc.communicate()
```

开发者也可以从Python程序向子进程输送数据, 然后获取子进程的输出数据.

```
def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Q13S\x11'
    proc = subprocess.Popen(
               ['openssl', 'enc', '-des3', '-pass', 'env:password'],
               env=env,
               stdin=subprocess.PIPE,
               stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()
    return proc
    
# 把一些随机生成的字节数据传给加密函数
procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)
    
# 等待输出
for proc in procs:
    out, err = proc.communicate()
    print(out[-10:0])
```

我们也可以把子进程的输出作为其余子进程的输入, 例如将ssl的输出作为md5的输入进行HASH:

```
def run_md5(input_stdin):
    proc = subprocess.Popen(
               ['md5'],
               stdin=input_stdin,
               stdout=subprocess.PIPE)
    return proc
```

如果担心子进程一直不终止, 或担心它的输出管道及输出管道由于某些原因发生了阻塞, 那么可以给communicate函数传入timeout参数, 以便没有给出响应时抛出异常。

不过, timeout参数仅在 Python3.3 及后续版本中有效, 对于之前的Python版本来说, 我们需要使用内置的select模块来处理, 以确保I/O操作的超时机制能够生效.

### 要点 ###

1. 可以用subprocess模块运行子进程, 并管理其输入流与输出流
2. Python解释器能够平行地运行多条子进程, 这使得开发者可以充分利用CPU的处理能力
3. 可以给communicate函数传入timeout参数, 以避免进程死锁或失去响应

## 第37条: 可以用线程来执行阻塞式I/O, 但不要用它做平行计算 ##

### 介绍 ###

标准CPython解释器中的多线程程序会受到GIL的影响, 并不能利用多线程的优势, 这样Python为何还要支持多线程呢?

1. 多线程使得程序看上去好像能够在同一时间做许多事情
2. 处理阻塞式的IO操作, 开发者可以借助线程把这些耗时的IO操作隔离开

尽管受制于GIL, 但是用多个Python线程来执行系统调用的时候可以平行的执行, 线程在执行系统调用的时候会释放GIL, 并且一直等到执行完成才会重新获取GIL.

### 要点 ###

1. 因为受到GIL的限制, 所以多条Python线程不能在多个CPU核心上面平行的执行字节码
2. Python多线程可以轻松地模拟出同一时刻执行多项任务的效果
3. 多个Python线程, 可以平行的执行多个系统调用, 使得程序在执行阻塞的IO操作的同时执行一些运算操作

## 第38条: 在线程中使用Lock来防止数据竞争 ##

### 介绍 ###

假设使用Counter类来进行计数:

```
class Counter(object):
    def __init__(self):
        self.count = 0
    def increment(self, offset):
        self.count += offset
        
# 工作线程
def worker(counter):
    counter.increment(1)
```
在多线程情况下count的计数会出现数据竞争而导致错误, 为了防止此类的数据竞争行为, Python在内置的threading模块里提供了一套健壮的工具, 例如Lock类来进行数据保护.

```
class Counter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0
    def increment(self, offset):
        with self.lock()
            self.count += offset
```

### 要点 ###

1. 虽然Python有全局解释器锁, 但是在编写自己的程序时依然要设法防止多个线程争用同一份数据
2. 如果在不加锁的情况下允许多条线程修改同一个对象, 那么程序的数据结构可能会遭到破坏
3. 在Python内置的threading模块中有个类名叫 Lock, 它用标准的方式实现了互斥锁

## 第39条: 用Queue来协调各线程之间的工作 ##

### 介绍 ###

### 要点 ###

## 第40条: 考虑用协程来并发地运行多个函数 ##

### 介绍 ###

### 要点 ###

## 第41条: 考虑用concurrent.futures来实现真正的并行计算 ##

### 介绍 ###

### 要点 ###

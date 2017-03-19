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

### 要点 ###

## 第38条: 在线程中使用Lock来防止数据竞争 ##

### 介绍 ###

### 要点 ###

## 第39条: 用Queue来协调各线程之间的工作 ##

### 介绍 ###

### 要点 ###

## 第40条: 考虑用协程来并发地运行多个函数 ##

### 介绍 ###

### 要点 ###

## 第41条: 考虑用concurrent.futures来实现真正的并行计算 ##

### 介绍 ###

### 要点 ###

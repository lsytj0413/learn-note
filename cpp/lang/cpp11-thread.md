---
title: C++11学习之多线程
date: 2016-09-10 20:32:41
description: 
catagories:
- blog
- 读书笔记
tags:
- C++
- 读书笔记
- C++11 
toc: true 文章目录
author: 小小笑儿
comments:
original:
permalink:
---
    C++11学习笔记之多线程库, 包括互斥量,条件变量,call_once以及用于异步操作的future,promise和task. ---《深入应用C++11》
+ <!-- more -->

# 线程 #

## 线程的创建 ##

使用std::thread创建线程很简单,只需要提供线程函数或者函数对象,并可以指定线程函数的参数:

    void func(int i){};
    
    std::thread t(func, 0);
    t.join();                // 等待线程结束
    
如果不希望阻塞到线程结束,可以调用detach()函数分离线程和线程对象.但是detach之后将不能再和线程发生联系.

注意:thread对象出了作用域会析构,如果线程函数还没有执行完则会发生错误.

线程不能复制,但可以移动:

    std::thread t1 = t;                 // error
    std::thread t1(std::move(t));       // ok

线程被移动之后,t将不再代表任何线程.

也可以通过std::bind和lambda表达式创建线程:

    std::thread t2([](int i){}, 1);

## 线程的基本用法 ##

获取当前线程ID,以及CPU核心数量:

    std::thread t([](){});
    cout << t.get_id() << endl;
    cout << std::thread::hardware_concurrency() << endl;

使线程休眠一段时间:

    std::this_thread::sleep_for(std::chrono::seconds(3));

# 互斥量 #

互斥量是一种同步原语, 一种线程同步的手段, 用来保护多线程访问时的数据共享.

## 独占互斥量std::mutex ##

不能递归调用的独占互斥量, 递归时发生死锁.

    std::mutex var_lock;
    
    void f(){
        var_lock.lock();
        // do something
        var_lock.unlock();
    };
    
    std::thread t1(f);
    std::thread t2(f);
    std::thread t3(f);

    t1.join();
    t2.join();
    t3.join();

如上例, 使用lock方法(阻塞)获取互斥量,使用unlock方法解除所有权, lock和unlock必须成对出现.
也可以使用try\_lock方法(不阻塞)尝试获取互斥量, 成功则返回true, 否则返回false.

可以使用lock\_guard简化lock/unlock的写法,也更安全(使用RAII技术).

## 递归互斥量std::recursive_mutex ##

递归互斥量允许同一线程多次获取该互斥量, 用来解决同一线程需要多次获取互斥量的问题.用法与std::mutex相同.

在实际使用中应尽量避免使用递归互斥量, 原因如下:

1. 应尽量简化需要递归互斥的代码, 因为这种代码容易引起晦涩问题;
2. 相比独占互斥量, 递归互斥量效率会低一些;
3. 虽然可以递归获取,但递归的最大次数有限, 超出次数会抛出std::system错误.

## 带超时的互斥量std::timed_mutex和std::recursive_timed_mutex ##

std::timed\_mutex是超时的互斥量, std::recursive\_timed\_mutex是超时的递归互斥量.
主要用于增加超时等待功能, 避免一直等待获取互斥量.主要新增try\_lock\_for和try\_lock\_until接口.

    std::timed\_mutex mutex;
    
    void f(){
        std::chrono::seconds timeout(1);
        while(true){
            if (mutex.try_lock_for(timeout)){
                mutex.unlock();
            }
        };
    };

    std::thread t1(f);
    std::thread t2(f);

    t1.join();
    t2.join();

# 条件变量 #

条件变量是C++11提供的另一种用于等待的同步机制, 能阻塞一个或多个线程, 直到收到另一个线程发出的通知或超时, 才唤醒阻塞的线程.
需要和互斥量配合使用.

C++11提供以下两种条件变量:

1. condition\_variable: 配合std::unique\_lock<std::mutex>进行wait操作
2. condition\_variable\_any: 和任意带有lock,unlock语义的mutex配合使用, 更灵活, 但效率低一些

条件变量的使用过程如下:

1. 拥有条件变量的线程获取互斥量
2. 循环检查某个条件, 如果条件不满足则阻塞到满足, 如果满足则向下执行
3. 某个线程满足条件之后调用notify\_once或notify\_all唤醒一个或多个等待的线程

下面是一个同步队列的例子:

    template <typename T>
    class SyncQueue
    {
    private:
        std::list<T> m_queue;
        std::mutex m_mutex;
        std::condition_variable_any m_not_empty;
        std::condition_variable_any m_not_full;
        int m_max;
        
        bool fullimp() const {
            return m_queue.size() == m_max;
        };
        
        bool emptyimp() const {
            return m_queue.empty();
        };
        
    public:
        SyncQueue(int max) : m_max(max)
        {};
        
        void put(const T& x){
            std::lock_guard<std::mutex> locker(m_mutex);
            while(fullimp()){
                m_not_full.wait(m_mutex);
            }
            
            m_queue.push_back(x);
            m_not_empty.notify_one();
        };
        
        void take(T& x){
            std::lock_guard<std::mutex> locker(m_mutex);
            while(emptyimp()){
                m_not_empty.wait(m_mutex);
            }
            
            x = m_queue.front();
            m_queue.pop_front();
            m_not_full.notify_one();
        };
        
        bool full() {
            std::lock_guard<std::mutex> locker(m_mutex);
            return fullimp(); 
        };
        
        bool empty() {
            std::lock_guard<std::mutex> locker(m_mutex);
            return emptyimp();
        };
        
        size_t size() {
            std::lock_guard<std::mutex> locker(m_mutex);
            return m_queue.size();
        };
    };

条件变量的wait还有一个重载方法,可以接收一个条件:

    m_not_full.wait(m_mutex, [this](){
        return !fullimp();
    });
    
需要注意的是, wait函数中会释放互斥量, 而lock\_guard此时还拥有互斥量, 并且只在出作用域时释放.
从语义上看这时会产生矛盾, 但其实并不会出问题, 因为wait释放互斥量之后会处于等待状态, 在被notify\_one或
notify\_all唤醒之后会先获取互斥量, 这相当于lock\_guard的互斥量在释放之后又获取到, 因此lock\_guard析构时
释放互斥量不会出问题.

这里使用unique\_lock更好,因为它可以随时释放锁, 从语义上看更加准确.

相关代码可以更改如下:

    std::unique_lock<std::mutex> locker(m_mutex);
    m_not_empty.wait(locker, 
        [this](){
            return !m_queue.empty();
        }
    );

# 原子变量 #

C++11提供了一个原子类型std::atomic<T>, 可以使用任意类型作为模板参数, 并内置了整型的原子变量, 这样使用原子变量就不需要
使用互斥量进行保护, 更加简洁.

一个计数器的示例如下:

    struct AtomicCounter{
        std::atomic<int> value;
        
        void incr(){
            ++value;
        };
        
        void decr(){
            ++value;
        };
        
        int get(){
            return value.load();
        };
    };

# call_once和once_flag的使用 #

为了保证在多线程环境下某个函数仅被调用一次, 可以使用std::call\_once进行保证, 该函数需要一个once\_flag作为参数.

    std::once_flag flag;
    
    void do_once(){
        std::call_once(flag, [](){
            cout << "once" << endl;
        });
    };
    
    std::thread t1(f);
    std::thread t2(f);

    t1.join();
    t2.join();

    // output
    // once                 // 只会输出一次
    
# 异步操作 #

C++11提供的异步操作相关类, 主要包括std::future, std::promise和std::package\_task.

1. std::future:  作为异步结果的传输通道, 可以方便的获取异步操作的返回值
2. std::promise: 包装一个值, 将数据和future绑定, 方便异步操作赋值
3. std::package\_task: 包装一个可调用对象, 将函数和future绑定, 以便异步调用

## std::future ##

future拥有3种状态(future\_status)来确定异步操作的结果:

1. Deferred: 异步操作未开始
2. Ready: 异步操作已完成
3. Timeout: 异步操作超时

获取异步操作结果的方式有3种:

1. get: 等待异步操作结束并获取结果
2. wait: 等待异步操作完成
3. wait\_for: 具有超时功能的等待异步操作完成

## std::promise ##

在线程函数中为promise赋值, 在线程函数执行完成之后就可以通过promise的future获取值.
取值是间接的通过promise内部的future实现的.

    std::promise<int> p;
    std::thread t([](std::promise<int>& p){
        p.set_value_at_thread_exit(9);
    }, std::ref(p));

    std::future<int> f = p.get_future();
    auto r = f.get();

## std::package_task ##

类似于promise, promise保存的是一个共享状态的值, 而package\_task保存的是一个函数.

    std::package_task<int()> task([](){
        return 7;
    });
    std::thread t(std::ref(task));
    std::future<int> f = task.get_future();
    auto r = f.get();
    
## 三者的关系 ##

future被promise和package\_task用来作为异步操作和异步结果的连接通道, 用future和shared\_future来获取异步操作的结果.
future是不可拷贝,只能移动的. 而shared\_future可以拷贝.

    int f(int x){
        return x+2;
    };
    
    std::pacakge_task<int(int)> tsk(f);
    std::future<int> fut = tak.get_future();
    
    std::thread(std::move(tsk), 2).detach();
    
    int value = fut.get();
    cout << value << endl;                 // 4
    
    vector<std::shared_future<int>> v;
    atuo f = std::async(std::launch::async, [](int a, int b){
        return a + b;
    }, 2, 3);
    
    v.push_back(f);
    cout << v[0].get() << endl;            // 5

# 线程异步操作函数async #

std::async可以直接建立异步task,将返回的结果保存在future中.

async的第一个参数是线程的创建策略, 有两种可选, 默认是立即创建线程.

1. std::launch::async: 在调用async时创建线程,, 默认;
2. std::launch::deferred: 在调用future的get或wait方法时创建线程

示例代码如下:

    std::future<int> f1 = std::async(std::launch::async, [](){
        return 8;
    });
    cout << f1.get() << endl;

std::async是更高层次的异步操作, 使我们不用关注线程创建的内部细节, 就能方便的获取异步执行状态和结果, 还可以指定线程创建策略.

应该使用std::async替代线程的创建, 作为异步操作的首选.

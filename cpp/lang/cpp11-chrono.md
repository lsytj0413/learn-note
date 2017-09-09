---
title: C++11学习之处理日期和时间
date: 2016-09-10 21:14:08
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
    C++11学习笔记之使用chrono库处理日期和时间. ---《深入应用C++11》
+ <!-- more -->

# 简介
chrono是C++11中方便的处理日期和时间的库, 主要包含三种类型: 

1. duration: 时间间隔
2. clocks: 时钟
3. time\_point: 时间点

# duration
duration表示一段时间间隔, 用来记录时间长度, 可以表示几秒, 几分钟或者几小时的时间间隔.原型如下:

    template <class Rap, class Period=std::ratio<1,1>>
    class duration;
    
第一个参数Rep是一个数值类型, 表示时钟数;

第二个参数是一个默认模板参数std::radio, 表示时钟周期; 原型如下:

    template <std::intmax_t Num, std::intmax_t Denom = 1>
    class ratio;
    
它表示每个时钟周期的秒数, 其中Num代表分子, Denom代表分母. 例如ratio<2>代表一个时钟周期为2秒;
ratio<1, 1000>代表一毫秒. 为方便使用, 标准库定义了一些常用的时间间隔, 如下:

    typedef duration<Rep, ratio<3600, 1>> hours;
    typedef duration<Rep, ratio<60, 1>> minutes;
    typedef duration<Rep, ratio<1, 1>> seconds;
    typedef duration<Rep, ratio<1, 1000>> milliseconds;
    typedef duration<Rep, ratio<1, 1000000>> microseconds;
    typedef duration<Rep, ratio<1, 1000000000>> nanoseconds;

通过使用这些间隔类型, 可以方便的定义时间间隔:

    std::chrono:::seconds(3);            // 3秒
    
chrono还提供了获取时间间隔的时钟周期数的方法count(), 基本用法如下:

    std::chrono::milliseconds ms(3);
    std::chrono::microseconds us = 2*ms;
    
    std::chrono::duration<double, std::ratio<1, 30>> hz30(3.5);
    
    cout << ms.count() << endl;          // output: 3 个时钟周期
    cout << us.count() << endl;          // output: 6000个时钟周期

    std::chrono::minutes t1(10);
    std::chrono::seconds t2(60);
    std::chrono::seconds t3 = t1 - t2;
    
    cout << t3.count() << endl;          // output: 540, 即(600-60)/1
    
duration的加减运算有一定的规则, 当两个duration时钟周期不相同时, 则会统一成一种时钟:

对于ratio<x1, y1>和ratio<x2, y2>, 设x1,x2的最大公约数为x, 而y1,y2的最小公倍数为y,
则统一的ratio为ratio<x, y>.

    std::chrono::duration<double, std::ratio<9, 7>> d1(3);
    std::chrono::duration<double, std::ratio<6, 5>> d2(1);

    auto d3 = d1 - d2;             // d3 = std::chrono::duration<double, std::ratio<3, 35>>

可以通过duration\_cast<>()将当前时钟周期转换为其他时钟周期.

    cout << chrono::duration_cast<chrono::minutes>(t3).count() << endl;
    // output: 9

# time_point

time\_point表示一个时间点, 用来获取从它的clock的纪元开始所经过的duration和当前的时间, 
可以做一些时间的比较和算数运算, 可以和ctime库结合起来显示时间. time\_clock必须用clock来计时.
time\_point有一个函数time\_from\_eproch()来获取1970年1月1日到time\_point时间经过的duration.

    using duration<int, std::ratio<60*60*24>> days_type;
    
    time_point<system_clock, days_type> today = time_point_cast<days_type>(system_clock::now());
    cout << today.time_from_eproch().count() << endl;
    
    // 输出今天到1970年1月1日的天数
    
time\_point还支持一些算术运算, 比如两个time\_point的差值时钟周期数, 
还可以和duration相加减. 不过不同的clock的time\_point是不能进行算术运算的.

    system_clock::time_point now = system_clock::now();
    std::time_t last = system_clock::to_time_t(now - hours(24));
    std::time_t next = system_clock::to_time_t(now + hours(24));

    cout << std::put_time(std::localtime(&last), "%F %T") << endl;
    cout << std::put_time(std::localtime(&next), "%F %T") << endl;

# clocks
clocks代表当前的系统时钟, 内部有time\_point, duration, Rep和Period等信息.包含以下3种信息:

1. system_clock: 代表真实世界的挂钟时间, 具体时间依赖于系统. system_clock保证提供一个可读时间
2. steady_clock: 不能被调整的时钟, 并不一定代表真实时间. 保证先后调用now获得的时间值是递增的
3. high_resolution_clock: 高精度时钟, 实际上是上两者之一的别名. 可以通过now获取当前时间点

# 计时器Timer
可以利用high\_resolution\_clock来实现一个类似于boost.timer的计时器.

    class Timer
    {
    private:
        time_point<high_resolution_clock> m_begin;
        
    public:
    
        Timer() : m_begin(high_resolution_clock::now())
        {};
        
        void reset() {
            m_begin = high_resolution_clock::now();
        };
        
        template <typename Duration=milliseconds>
        int64_t elapsed() const {
            return duration_cast<Duration>(high_resolution_clock::now() - m_begin).count();
        };
   
        int64_t elapsed_micro() const {
            return elapsed<microseconds>();
        };
        
        int64_t elapsed_nano() const {
            return elapsed<nanoseconds>();
        };
        
        int64_t elapsed_seconds() const {
            return elapsed<seconds>();
        };
        
        int64_t elapsed_minutes() const {
            return elapsed<minutes>();
        };
        
        int64_t elapsed_hours() const {
            return elapsed<hours>();
        };
    }

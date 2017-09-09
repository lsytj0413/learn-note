---
title: C++11学习之使用智能指针管理内存
date: 2016-09-07 20:32:41
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
    C++11学习笔记之智能指针, shared_ptr, unique_ptr和weak_ptr. ---《深入应用C++11》
+ <!-- more -->

# 什么是智能指针 #

在C#和java语言中有垃圾回收机制, .NET运行时和Java虚拟机可以管理分配的堆内存, 在对象失去引用的时候自动回收, 一般不用关心内存管理.
但在C++中,必须自己去释放分配的内存,否则会内存泄漏.解决这个问题最有效的办法是使用智能指针管理分配的内存.

智能指针是存储指向动态分配对象的指针的类, 用于生存期控制, 确保在离开指针所在作用域时, 自动正确的销毁动态分配的对象, 防止内存泄漏.
一种通用的实现技术是使用引用计数, 每引用一次计数+1, 析构一次-1, 当计数减为0时, 释放内存.

# shared_ptr: 共享的智能指针 #

shared\_ptr使用引用计数, 每一个shared\_ptr的拷贝都指向相同的内存, 在最后一个shared\_ptr析构时释放内存.

## 基本用法 ##

### 初始化 ###

可以通过构造函数, std::make\_shared<T>辅助函数和reset方法初始化shared\_ptr:

    std::shared_ptr<int> p(new int(10));
    std::shared_ptr<int> p2 = p;
    std::shared_ptr<int> ptr;
    ptr.reset(new int(1));
   
    p2 = std::make_shared(1);
    
    if (p2) {
        cout << "p2 is not null" << endl;
    } 

应该优先使用make\_shared函数构造智能指针, 因为它更高效.

不能将一个原始指针赋值给智能指针:

    std::shared_ptr<int> p = new int(1);         // error

### 获取原始指针 ###

可以通过get函数返回原始指针:

    std::shared_ptr<int> p(new int{1});
    int* p1 = p.get();

### 指定删除器 ###

智能指针初始化时可以指定删除器:

    void delete_p(int* p){
        delete p;
    };
    
    std::shared_ptr<int> p(new int{1}, delete_p);
    
当引用计数为0时,自动调用删除器来释放对象的内存, 删除器可以是一个lambda表达式.

当用shared\_ptr管理动态数组时需要指定删除器, 因为默认的删除器不支持数组对象.

    std::shared_ptr<int> p(new int[10], [](int* p){
        delete [] p;
    });

可以封装一个make\_shared\_array使shared\_ptr支持数组:

    template <typename T>
    shared_ptr<T> make_shared_array(size_t size){
        return shared_ptr<T>(new T[size], default_delete<T[]>());
    };

其中default\_delete内部是通过调用delete实现功能的.

## 注意点 ##

### 不要用一个原始指针初始化多个shared_ptr ###

这种情况会造成重复delete:

    int* ptr = new int{1};
    shared_ptr<int> p1(ptr);
    shared_ptr<int> p2(ptr);         // double delete 

### 不要在实参中创建shared_ptr ###

例如下面的写法:

    function (shared_ptr<int>(new int{1}), g());          // 可能造成内存泄漏
    
因为C++中函数实参的求值顺序在不同的编译器,不同的调用约定下可能是不同的, 一般为从右到左, 也可能从左到右.
所以如上代码中, 可能先new, 然后调用g, 如果此时g中发生异常, 而shared\_ptr还没有创建, 则int内存泄漏.
正确的写法如下:

    shared_ptr<int> p(new int{1});
    function (p, g());

### 要通过shared_from_this返回this指针 ###

不要直接将this指针作为shared\_ptr返回, 这样可能导致重复析构.
正确的做法是让目标类从enable\_shared\_from\_this派生, 使用基类的成员函数shared\_from\_this返回this的智能指针:

    class A : public std::enable_shared_from_this<A>
    {
        shared_ptr<A> self(){
            return shared_from_this();
        };
    };
    
    shared_ptr<A> spy(new A());
    shared_ptr<A> p = spy->self();
    
### 避免循环引用 ###

循环引用会导致内存泄漏:

    struct A;
    struct B;

    struct A{
        shared_ptr<B> p;
    };
    
    struct B{
        shared_ptr<A> p;
    };

    shared_ptr<A> pa(new A);
    shared_ptr<B> pb(new B);
    pa.p = pb;
    pb.p = pa;

上例中存在内存泄漏,循环引用导致pa和pb的引用计数为2, 当离开作用域之后也只会变为1.
解决办法是将shared\_ptr使用weak\_ptr替换.

### 侵入性 ###

shared\_ptr具有侵入性, 即一个指针一旦交由shared\_ptr控制, 则再不能取出.

# unique_ptr: 独占的智能指针 #

unique\_ptr是独占型的智能指针, 不允许其他的智能指针共享内部的指针, 不允许通过赋值给另一个unique\_ptr.

    unique_ptr<A> p(new A);
    unique_ptr<A> p1 = p;            // error

虽然不能赋值,但可以通过函数返回给其他unique\_ptr,也可以使用std::move移动到其他unique\_ptr.

    unique_ptr<A> p(new A);
    unique_ptr<A> p1 = std::move(p);    

C++11没有提供make\_unique方法,将在C++14中提供.可以简单实现如下:

    template <typename T, typename... TArgs> 
    inline 
    typename enable_if<!is_array<T>::value, unique_ptr<T>>:type
    make_unique(TArgs&&... args){
        return unique_ptr<T>(new T(std::forward<TArgs>(args)...));
    };
    
    template <typename T> 
    inline 
    typename enable_if<is_array<T>::value && extent<T>::value==0, unique_ptr<T>>:type
    make_unique(size_t size){
        using U = typename remove_extent<T>::type;
        return unique_ptr<T>(new U[size]());
    };
    
    template <typename T, typename... TArgs> 
    typename enable_if<extent<T>::value!=0, void>:type
    make_unique(TArgs&&... args) = delete; 

unique\_ptr可以指向一个数组:

    std::unique_ptr<int[]> ptr(new int[10]);

unique\_ptr指定删除器时需要取定删除器的类型:

    unique_ptr<int, void(*)(int*)> ptr(new int{1}, [](int* p){
        delete p;
    });    

# weak_ptr: 弱引用的智能指针 #

弱引用的智能指针weak\_ptr是用来监视shared\_ptr的,不会增加引用计数.
它不管理shared\_ptr内部的指针, 主要是为了监视shared\_ptr的生命周期, 是shared\_ptr的一个助手.
weak\_ptr没有重载操作符*和->, 不能操作资源.

### 基本用法 ###

1. 通过use\_count()获取引用计数值 
2. 通过expire()判断资源是否已经释放
3. 通过lock方法获取所监视的shared\_ptr 

示例如下:
    
    shared_ptr<int> sp(new int{10});
    weak_ptr<int> wp(sp);
    
    cout << wp.use_count() << endl;
    cout << wp.expire() << endl;
    
    shared_ptr<int> sp1 = wp.lock();
    cout << *sp1 << endl;

## 返回this指针 ##

之前提到需要通过派生enable\_shared\_from\_this, 然后用shared\_from\_this返回智能指针.
因为enable\_shared\_from\_this中有一个weak\_ptr, 调用shared\_from\_this时正是由weak\_ptr的lock方法返回指针.

## 解决循环引用 ##

示例如下:

    struct A;
    struct B;

    struct A{
        shared_ptr<B> p;
    };
    
    struct B{
        weak_ptr<A> p;
    };

    shared_ptr<A> pa(new A);
    shared_ptr<B> pb(new B);
    pa.p = pb;
    pb.p = pa;

将其中一个成员修改为weak\_ptr之后, 不会造成循环引用.

# 使用智能指针管理第三方库分配的内存 #

一般第三方库分配的内存都需要调用相应的第三方库接口释放, 容易造成内存泄漏, 使用智能指针加上删除器管理第三方库分配的内存,
即可避免内存泄漏.

但是, 因为内存分配有可能不能跨模板边界释放, 所以一般都需要使用第三方库的释放接口作为智能指针的删除器.

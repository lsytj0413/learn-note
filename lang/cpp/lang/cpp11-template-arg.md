---
title: C++11学习之可变模板参数
date: 2016-09-05 21:53:22
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
    C++11学习笔记之可变模板参数. ---《深入应用C++11》
+ <!-- more -->

# 什么是可变模板参数 #

在C++11之前, 类模板和函数模板只能含有固定数量的模板参数, 在C++11之后的新特性可变模板参数允许包含0到任意个模板参数.
声明可变模板参数时需要在typename和class后面带上省略号'...'.

省略号的作用有两个:

1. 声明一个参数包, 这个参数包可以包含0到任意个模板参数
2. 在模板定义的右边, 可以将参数包展开称为一个一个独立的参数.

# 可变参数模板函数 #

一个可变参数模板函数的定义如下:

    template <class... T>
    void f(T... args)
    {
        cout << sizeof...(args) << endl;
    };
    
    f();                      // output: 0
    f(1, 2);                  // output: 2
    f(1, 2.5, "");            // output: 3

如果需要参数包中的参数,则需要将参数包展开.有两种方式展开参数包, 递归或者逗号表达式和初始化列表.

## 递归方式展开参数包 ##

使用递归方式展开参数包,需要一个参数包展开的函数和一个递归终止的函数.

    void print()
    {
        cout << "end" << endl;
    };
    
    template <typename T, typename... TArgs>
    void print(T&& t, TArgs&&... args)
    {
        cout << t << endl;
        print(args...);
    };
    
    print(1, 2, 3, 4);
    
还可以使用type_traits展开:

    template <size_t I = 0, typename Tuple>
    typename std::enable_if<I == std::tuple_size<Tuple>::value>::type 
    printtp(Tuple&& tp){
    };

    template <size_t I = 0, typename Tuple>
    typename std::enable_if<I < std::tuple_size<Tuple>::value>::type 
    printtp(Tuple&& tp){
        cout << std::get<I>(tp) << endl;
        printtp<I+1>(t);
    };
    
    template <typename... TArgs>
    void print(TArgs&&... args){
        printtp(std::make_tuple(std::forward<TArgs>(args)...));
    };

## 逗号表达式和初始化列表方式展开参数包 ##

递归方式展开参数包是一种标准做法,也很好理解. 但是必须有一个终止递归的重载函数, 增加了复杂度.
通过借助逗号表达式和初始化列表, 我们也可以展开参数包.

    template <typename T>
    void printarg(T&& t){
        cout << t << endl;
    };
    
    template <typename... TArgs>
    void expand(TArgs&&... args){
        int arr[] = {(printarg(args), 0)...};
    };

    expand(1, 2, "3");

在上面的例子中,printarg不是终止函数, 是一个处理每个参数的函数, 利用逗号表达式会按顺序执行的特性实现展开.
在执行完成之后, arr会是一个所有元素都为0的数组, 在arr构造的过程中将参数包展开. 这个数组的目地只是为了在构造过程中展开参数包.
利用std::initializer_list可以改进以上代码:

    template <typename... TArgs>
    void expand(TArgs&&... args){
        std::initializer_list<int>{(printarg(args), 0)...};
    };

利用lambda表达式可以消除printarg函数的定义:

    template <typename... TArgs>
    void expand(TArgs&&... args){
        std::initializer_list<int>{([&]{cout << args << endl;}(), 0)...};
    };
    
# 可变参数模板类 #

可变参数模板类的参数包需要通过模板特化或继承方式展开.

## 模板递归和特化方式展开参数包 ##

一般需要包括声明类和特化的模板类:

    template <typename... TArgs>
    struct Sum;
    
    template <typename First, typename... Rest>
    struct Sum<First, Rest...>{
        enum {
            value = Sum<First>::value + Sum<Rest...>::value,
        };
    };
    
    template <typename Last>
    struct Sum<Last>{
        enum {
            value = sizeof(Last),
        };
    };
    
上例中Sum的作用是计算参数包中类型的size之和.

如果使用std::integral_constant来消除枚举定义, 则可以实现如下:

    template <typename... TArgs>
    struct Sum;
    
    template <typename First, typename... Rest>
    struct Sum<First, Rest...> : std::integral_constant<int, Sum<First>::value + Sum<Rest...>::value>
    {};
    
    template <typename Last>
    struct Sum<Last> : std::integral_constant<int, sizeof(Last)>
    {};

## 继承方式展开参数包 ##

看一个生成整数序列的例子:

    template <int...>
    struct IndexSeq{};
    
    template <int N, int... Indexes>
    struct MakeIndexes : MakeIndexes<N-1, N-1, Indexes...>
    {};
    
    template <int... Indexes>
    struct MakeIndexes<0, Indexes...>{
        using type = IndexSeq<Indexes...>;
    };

    using T = typename MakeIndexes<3>::type;           // T = IndexSeq<0, 1, 2>

上例中通过继承递归调用, 最终得到整数序列IndexSeq.

也可以使用using的方式实现如下:

    template <int N, int... Indexes>
    struct MakeIndexes{
        using type = MakeIndexes<N-1, N-1, Indexes...>::type;
    };
    
    template <int... Indexes>
    struct MakeIndexes<0, Indexes...>{
        using type = IndexSeq<Indexes...>;
    };

可变参数模板类比可变参数模板函数要复杂,功能也更为强大, 因为可变模板参数类可以带有状态, 通过一些type_traits在编译期
对类型进行一些判断,选择和转换等操作.

# 利用可变模板参数消除重复代码 #

可变参数模板中的参数包的数量和类型都可以是任意的, 因此可以使用更泛化的方式处理一些问题.

## 打印函数 ##

    template <typename T>
    void Print(T t){
        cout << t << endl;
    };
    
    template <typename T, typename... TArgs>
    void Print(T t, TArgs... args){
        cout << t << endl;
        Print(args...);
    };
    
## 泛化对象创建 ##

    template <typename... TArgs>
    T* Instance(TArgs&&... args){
        return new T(std::forward<TArgs>(args)...);
    };
    
## 泛化求和 ##

    template <typename T, typename ...TArgs>
    auto variadic_sum(T&& v1, TArgs&&... args) -> decltype(v1 + variadic_sum(args...))
    {
        return v1 + variadic_sum(std::forward<TArgs>(args)...);
    }
    
    template <typename T>
    T variadic_sum(T&& v)
    {
        return v;
    }

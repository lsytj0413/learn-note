---
title: C++11学习之类型萃取
date: 2016-09-04 10:55:55
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
    C++11学习笔记之type_traits. ---《深入应用C++11》
+ <!-- more -->

# 什么是类型萃取

type\_traits提供了丰富的编译期计算,查询,判断,选择和转换的帮助类.

type\_traits的类型选择功能,在一定程度上可以消除冗长的switch-case或者if-else语句,降低程序的圈复杂度, 提高代码的可维护性.
type\_traits的类型判断功能,在编译期可以检查出是否是正确的类型, 以便能编写更安全的代码.

# 基本的type_traits 

## 简单的type_traits 
先看一个在C++11之前,在一个类中定义编译期常量的方法非:

    template <typename T>
    struct GetLeftSize0{
        static const int value = 1;
    };

    template <typename T>
    struct GetLeftSize1{
        enum {
            value = 1,
        };
    };

上述代码可以通过value获取编译期常量1, 在C++11之后的等价写法更简洁:

    template <typename T>
    struct GetLeftSize : std::intergral_constant<int, 1>
    {};

一个integral\_constant可以实现如下:

    template <class T, T v>
    struct intergral_constant{
        static const T value = v;
        using value_type = T;
        using type = intergral_constant<T, v>;
        operator value_type() {
            return value;
        };
    };

intergral\_constant类有一个value成员, 可以通过它获取值. 常见的用法是从integral\_constant派生.

在标准库中有 std::true\_type和std::false\_type定义了true和false类型.

    using true_type = intergral_constant<bool, true>;
    using false_type = intergral_constant<bool, false>;

相对于直接使用bool值, true\_type和false\_type有以下几个优势:

1. true\_type等可以被继承,而true不行;
2. true\_type和false\_type是不同的类型, 可以用作函数重载等, 而true和false是相同的类型(bool);
3. true\_type和false\_type更符合元编程的要求.

## 类型判断的type_traits
类型判断的type\_traits从std::intergral\_constant派生,用来检查模板类型是否符合为某种类型.

一些常用的类型判断模板如下表:

| traits类型 | 说明 |
|:--|:--|
| is\_void | T是否为void |
| is\_floating\_piont | 是否为浮点类型 |
| is\_array | 是否为数组 |
| is\_pointer | 是否为指针(包括函数指针,但不包括成员函数指针) |
| is\_enum | 是否为枚举 |
| is\_union | 是否为非union的class/struct |
| is\_class | 是否为类类型而不是union |
| is\_function | 是否为函数 |
| is\_reference | 是否为引用(左值引用或右值引用) |
| is\_arithmetic | 是否为整数和浮点类型 |
| is\_fundamental | 是否为整数,浮点,void或nullptr类型 |
| is\_object | 是否为一个对象类型(不是函数,引用,void) |
| is\_scalar | 是否为arithmetic, enumeration, pointer, pointer to member或std::nullptr_t类型 |
| is\_compound | 是否为非fundamental类型构造的 |
| is\_member\_pointer | 是否为成员函数指针 |
| is\_polymorphic | 是否有虚函数 |
| is\_abstract | 是否为抽象类 |
| is\_signed | 是否为有符号类型 |
| is\_unsigned | 是否为无符号类型 |
| is\_const | 是否为const修饰的类型 |

判断类型的traits一般和enable\_if结合使用,通过SFINAE特性来实现功能更强大的重载.

## 判断两个类型之间关系的traits

在需要检查两个类型之间的关系时,可以使用以下traits:

| traits类型 | 说明 |
|:--|:--|
| is\_same | 类型是否相同 |
| is\_base\_of | 是否是继承关系 |
| is\_convertible | 第一个类型是否能转换为第二个类型 |

## 类型转换的traits
常用的类型转换的traits包括对const的修改和添加,引用的移除和添加, 数组的修改和指针的修改等, 如下表:

| traits类型 | 说明 |
|:--|:--|
| remove\_const | 移除const |
| add\_const | 添加const |
| remove\_reference | 移除引用 |
| add\_lvalue\_reference | 添加左值引用 |
| add\_rvalue\_reference | 添加右值引用 |
| remove\_extent | 移除数组顶层的维度 |
| remove\_all\_extend | 移除数组所有的维度 |
| remove\_pointer | 移除指针 |
| add\_pointer | 添加指针 |
| decay | 移除cv或添加指针 |
| common\_types | 获取公共类型 |

对于普通类型来说,decay是移除引用和cv限定符.decay还可以作用于数组和函数, 具体的规则如下:
1. 先移除T的引用,得到类型U, U = remove\_reference<T>::type;
2. 如果is\_array<T>::value为true,修改类型type为remove\_extent<U>::type*;
3. 否则, 如果是is\_function<U>::value为true, 修改类型type为add\_pointer<U>::type;
4. 否则, 修改类型type为remove\_cv<U>::type;

# 根据条件选择的traits
std::conditional在编译期根据一个判断式选择两个类型中的一个, 类似于一个三元表达式:

    template <bool B, typename T, class F>
    struct conditional;
    
如果B为true, 则conditional::type为T,否则为F.

# 获取可调用对象返回类型的traits
当某个类型没有模板参数时,要获取函数的返回类型会比较困难:

    struct A{
        A() = delete;
    
        int operator()(int i){
            return i;
        };
    };
    
    decltype(A()(0)) i = 4;            // error, 因为A没有默认构造函数

在上面这种情况下,我们可以借助std::declval:

    decltype(std::declval<A>()(std::declval<int>())) i = 4;

std::declval可以获取任何类型的临时值,不论该类型是否有默认构造函数.

在C++11中提供了更简洁的std::result\_of,用来在编译期获取一个可调用对象的返回类型:

    std::result_of<A(int)>::type i = 4;

    int fn(int){
        return int();
    };
    
    std::result_of<decltype(fn)&(int)>::type i = 4; 
    std::result_of<decltype(fn)*(int)>::type i = 4; 
    std::result_of<typename std::decay<decltype(fn)>::type(int)>::type i = 4; 

在上例中, 因为fn是一个函数类型而不是一个可调用对象, 所以不能直接适用于std::result\_of.
需要先转换为一个可调用对象.

# 根据条件禁用或启用某种或某些类型的traits
编译器在匹配重载函数时会匹配所有的重载函数,找到一个最精确匹配的函数,在匹配过程中可能会有一些失败的尝试,当匹配失败时会再次尝试匹配其他的重载函数.

    template <typename T>
    void p(T*){};
    
    template <typename T>
    void p(T){};
    
    p(1);                // void p(T);

如上代码会匹配到第二个函数. 当匹配到p(T*)时匹配失败,但是编译器并不会报错, 会尝试匹配其他的重载, 只要有一个能匹配上就不会报错.
这个规则就是SFINAE(substitution-failure-is-not-an-error).

std::enable\_if利用SFINAE规则实现根据条件选择重载函数.

    template <class T>
    typename std::enable_if<std::is_arithmetic<T>::value, T>::type
    foo (T t){
        return t;
    };
    
    auto r = foo(1);              // r = 1
    auto r1 = foo(1.2);           // r1 = 1.2
    auto r2 = foo("test");        // error

在上面的例子中,我们限定了T只能是arithmetic,否则编译不通过.

std::enable\_if实现了强大的重载机制, 使得只有返回值不同时也能进行重载.

例如, 将一些基本类型转换为string类型的函数, 普通实现如下:

    template <typename T>
    string ToString(T& t){
        if (typeid(T) == typeid(int)
            || typeid(T) == typeid(double)
            || typeid(T) == typeid(float)
        )
        {
            std::stringstream s;
            s << t;
            return s.str();
        }
        else if (typeid(T) == typeid(string)){
            return t;
        }
    };

而使用enable\_if消除if语句之后的实现如下:

    template <class T>
    typename std::enable_if<std::is_arithmetic<T>::value, string>::type 
    ToString (T& t){
        return std::to_string(t);
    };

    template <class T>
    typename std::enable_if<std::is_same<T, string>::value, string>::type 
    ToString (T& t){
        return t;
    };

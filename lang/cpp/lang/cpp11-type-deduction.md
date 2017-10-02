---
title: C++11学习之类型推导
date: 2016-08-16 20:21:17
description: 
catagories:
- blog
- 读书笔记
tags:
- C++
- 读书笔记
- C++11 
- auto
toc: true 文章目录
author: 小小笑儿
comments:
original:
permalink:
---
    C++11学习笔记之类型推导部分, 包括auto, decltype等. ---《深入应用C++11》
+ <!-- more -->

# 类型推导 #

C++11引入了auto和decltype关键字实现类型推导，以获取复杂的类型，简化书写，提高编码效率。

# auto类型推导 #

auto是一个隐式的类型推导，发生在编译器。作用是让编译器自动推导出这个变量的类型，而不需要显示指定。以下是一些基本用法:

    auto x = 5;                      // OK, x=int
    auto pi = new auto(1);           // OK, pi=int*
    const auto *v = &x, u = 6;       // OK, v=const int*, u=const int
    static auto y = 0.0;             // OK, y=double
    auto int r;                      // ERROR, auto不再表示存储类型指示符
    auto s;                          // ERROR, 无法推导

有以下两点需要注意:

1. 第３行中，虽然经过ｖ的推导之后已经可以确定ｕ的类型，但是u仍然必须进行赋值;
2. 第３行中，ｕ的初始化不能使编译器推导产生二义性.

## auto推导规则 ##

先看例子:

    int x = 0;                     
    
    auto *a = &x;                 // a=int*, auto=int
    auto b = &x;                  // b=int*, auto=int*
    auto &c = x;                  // c=int&, auto=int
    auto d = c;                   // d=int, auto=int
    
    const auto e = x;             // e=const int, auto=int
    auto f = e;                   // f=int, auto=int
    
    const auto& g = x;            // g=const int&, auto=int
    auto &h = g;                  // h=const int&, auto=const int

1. auto可以推导出指针类型;
2. auto会抛弃引用类型;
3. 当表达式带有const属性时，auto会抛弃const;
4. 当auto与引用/指针结合时，会保留const;

经过以上例子，得出规则如下:

1. 当不声明为指针或者引用时，auto的推导结果和初始化表达式抛弃引用和cv限定符(const/volatile)后的类型一致;
2. 当声明为指针或引用时, auto的推导结果将保留cv属性.

在C++11中, auto不能用于函数参数，在C++14中则可用于lambda表达式的参数声明.

## auto的限制 ##

1. 不能用于函数参数;
2. 不能用于非静态成员变量, 仅能用于static const的整形或枚举成员，因为其他类型在C++中无法就地初始化;
3. 无法定义数组;
4. 无法推导出模板参数, 例如 **Bar<auto> bb = bar; **.

## 什么时候使用auto ##

1. 已知类型时使用auto简化书写, 如:

        vector<int>::iterator itor = v.begin();
        auto itor = v.begin();

2. 利用auto处理泛型

        struct Foo{
            static int get(void){};
        }
        
        struct Bar{
            static char* get(void){};
        }
        
        template <typename T>
        void func(void){
            auto val=A::get();
        }
此时可使用auto获取get函数的返回类型.

3. auto会造成代码可读性和可维护性下降,需衡量使用.

# decltype #

## 获取表达式类型 ##

C++11新增了decltype关键字, 用于在编译期获取表达式的类型.语法格式如下:

    decltype(exp)

decltype类似于sizeof, 推导过程是在编译期完成，且不会计算表达式的值.例子如下:

    int x = 0;
    decltype(x) y = 1;                  // y=int
    decltype(x + y) z = 0;              // z=int
    
    const int& i = x;                   
    decltype(i) j = y;                  // j=const int&
    
    const decltype(z) *p = &z;          // p=const int*
    decltype(z) *pi = &z;               // pi=int*
    decltype(pi) *pp = &pi;             // pp=int**

1. j的结果表明decltype可以保留表达式的引用以及const限定符; 对于一般的标记表达式, decltype精确的推导出表达式本身的类型, 不会舍弃引用和cv限定符;
2. decltype可以像auto一样加上引用和指针, 以及cv限定符;
3. decltype和引用结合的推导结果, 与C++11新增的引用折叠规则有关;

## decltype的推导规则 ##

1. exp是标识符/类访问表达式, decltype(exp)和exp的类型一致：
2. exp是函数调用, decltype(exp)和返回值类型一致;
3. 其他情况下, 若exp是左值, 则decltype(exp)是exp类型的左值引用, 否则和exp类型一致;

### 标识符和类访问表达式 ###

    struct Foo{
        static const int Number = 0;
        int x;
    }
    int n = 0;
    volatile const int &x = n;
    
    decltype(n) a = n;               // a=int
    decltyep(x) b = n;               // b=const volatile int&
    
    decltype(Foo::Number) c = 0;     // c=const int
    
    Foo foo;
    decltyep(foo.x) d = 0;           // d=int

### 函数调用 ###

    int& func_int_r(void);                    // lvalue
    int&& func_int_rr(void);                  // xvalue, 右值引用本身是一个xvalue
    int func_int(void);                       // prvalue
    
    const int& func_cint_r(void);             
    const int&& func_cint_rr(void);
    const int func_cint(void);
    
    const Foo func_cfoo(void);

    int x = 0;
    
    decltype(func_int_r()) a1 = x;            // a1=int&
    decltype(func_int_rr()) b1 = 0;           // b1=int&&
    decltype(func_int()) c1 = 0;              // c1=int
    
    decltype(func_cint_r()) a2 = x;           // a2=const int&
    decltype(func_cint_rr()) b2 = 0;          // b2=const int&&
    decltype(func_cint()) c2 = 0;             // c2=int
    
    decltype(func_cfoo()) ff = Foo();         // ff=const Foo

注意c2的类型是int而不是const int，对于rvalue而言, 只有类类型可以携带cv限定符.

### 带括号表达式和加法表达式 ###

    struct Foo { int x;};
    const Foo foo = Foo();

    decltype(foo.x) a = 0;              // a=int
    decltype((foo.x)) b = a;            // b=const int&
    
    int n = 0, m = 0;
    decltype(m + n) c = 0;              // c=int
    decltype(n += m) d = c;             // d=int&

1. 对于b, foo.x是一个左值，则b是左值引用：
2. m+n返回一个右值
3. n+=m返回一个左值

## 实际使用 ##

decltype多用于泛型编程中.

    template <typename ContainerT>
    struct Foo{
        typename ContainerT::iterator it_;
        
        void f(ContainerT& c){
            it_ = c.begin();
        }
    }
    
    int main(void){
        typedef const std::vector<int> c_t;
        c_t v;
        
        Foo<c_t> foo;
        foo.f(v);
        
        return 0;
    }

上述代码不能通过编译，因为ContainerT::iterator不能包括const类型的迭代器.

在C++98/03时只能通过特化const类型的容器进行处理, 而在C++11中则可以利用decltype, 代码如下:

    template <typename ContainerT>
    struct Foo{
        decltype(ContainerT().begin()) it_;
    }

# 结合使用auto/decltype--返回类型后置语法 #

考虑以下场景:

    template <typename R, typename T, typename U>
    R add(T t, U u){
        return t+u;
    }

上述模板在使用时需显示给出R的类型，对使用造成了很多不便, 更改的写法如下:

    template <typename T, typename U>
    decltype(T() + U()) add(T t, U u){
        return t+u;
    }

上述模板没有考虑没有无参构造函数的类, 正确的写法如下:

    template <typename T, typename U>
    decltype((*(T*)0) + (*(U*)0)) add(T t, U u){
        return t+u;
    }
    
虽然正确，但是写法太过于晦涩，代码可读性太低, 利用返回类型后置语法，最终的写法如下:

    template <typename T, typename U>
    auto add(T t, U u) -> decltype(t + u){
        return t+u;
    }

在 C++14 之后, 拥有一个更为简洁的语法:

```
template <typename T, typename U>
auto add(T t, U u) {
    return t + u;
}
```

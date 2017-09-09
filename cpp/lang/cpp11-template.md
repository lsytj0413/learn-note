---
title: C++11学习之模板的细节改进
date: 2016-08-17 21:43:19
description: 
catagories:
- blog
- 读书笔记
tags:
- C++
- 读书笔记
- C++11 
- 模板
toc: true 文章目录
author: 小小笑儿
comments:
original:
permalink:
---
    C++11学习笔记之模板的细节改进部分，包括模板别名及函数模板的默认模板参数. ---《深入应用C++11》
+ <!-- more -->

# 模板的右尖括号
在C++98/03中，连续两个右尖括号(>>)会被编译器解释为右移操作符，而不是模板参数列表:
    
    vector<map<int, int>> v;
在这种代码中需要在>>中加一个空格.

在C++11中这个限制被取消掉了,但在如下的代码中会引出问题:

    template <int T>
    struct Foo{};
    
    Foo< 100>>2 > v;
在这种情况下需要引入括号:

    Foo<(100>>2)> v;
这种加括号的方式也是一种良好的编程习惯，在书写时写出无二义性的代码.

# 模板别名
在C++中，可以通过typedef定义类型别名:

    typedef unsigned int uint_t;
但是这种方式有一些限制:

    typedef map<int, int> map_int_t;
    typedef map<string, int> map_int_t;
这种类型定义不能处理泛型的代码，例如定义一个key为泛型，而value为Int的类型．要达到这种效果，往往需要一层wrapper:

    template <typename T>
    struct int_map{
        typedef map<T, int> type;
    }
    
    int_map<int>::type v1;
    int_map<string>::type v2;
这种方式引入了额外的复杂性, 在C++11中可以通过using轻松达到以上要求:

    template <typename T>
    using int_map_1 = map<T, int>;
   
    int_map_1<int>::type v1;
    int_map_1<string>::type v2;

# 函数模板的默认模板参数
在C++98/03中，函数不能有默认模板参数, 在C++11中被解除了．
但函数模板的默认模板参数和其他的默认参数有些不同:

1. 没有必须写在参数表最后的限制;
        
        template <typename R = int, typename U>
        R func(U val){
            return val;
        }

        int main(void){
            func(123);        // 返回值为int
            return 0;
        }

2. 若指定模板参数，则:

        func<long>(123);     // 返回值为long

3. 当默认模板参数和模板参数自动推导同时使用时，若函数模板无法自动推导出参数类型，则使用默认模板参数.

        template <typename T>
        struct identity{
            using type = T;
        }
       
        // 通过identity模板禁用val的类型自动推导
        template <typename T = int>
        void func(typename identity<T>::type val, T = 0){}
        
        int main(void){
            func(123);                // T=int
            func(123, 123.0);         // T=double
            return 0;
        }

---
title: C++11学习之其他特性
date: 2016-09-10 21:16:53
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
    C++11学习笔记之委托/继承构造函数, 原始字面量, 新增关键字等. ---《深入应用C++11》
+ <!-- more -->

# 委托构造函数和继承构造函数 #

## 委托构造函数 ##

委托构造函数允许在同一个类中一个构造函数可以调用另外一个构造函数, 从而可以在初始化时简化变量的初始化:

    class class_c {
    public:
        int max;
        int min;
        int middle;
        
        class_c (int my_max){
            max = my_max > 0 ? my_max : 10;
        };
        
        class_c (int my_max, int my_min){
            max = my_max > 0 ? my_max : 10;
            min = my_min > 0 && my_min < my_max ? my_min : 1;
        };
        
        class_c(int my_max, int my_min, int my_middle){
            max = my_max > 0 ? my_max : 10;
            min = my_min > 0 && my_min < my_max ? my_min : 1;
            middle = my_middle < max && my_middle > min ? my_middle : 5;
        };
    };

在上例中, 每个构造函数都需要对成员变量赋值, 很烦琐也容易出错, 利用委托构造函数简化如下:

    class class_c {
    public:
        int max;
        int min;
        int middle;
        
        class_c (int my_max){
            max = my_max > 0 ? my_max : 10;
        };
        
        class_c (int my_max, int my_min) : class_c(my_max)
        {
            min = my_min > 0 && my_min < my_max ? my_min : 1;
        };
        
        class_c(int my_max, int my_min, int my_middle) : class_c(my_max, my_min)
        {
            middle = my_middle < max && my_middle > min ? my_middle : 5;
        };
    };

有以下两个注意点:

1. 链式调用委托构造函数不能形成环, 否则会在运行期抛出异常
2. 使用了委托构造函数之后就不能使用类成员初始化

## 继承构造函数 ##

C++11的继承构造函数可以让派生类直接使用基类的构造函数, 而无须自己再写构造函数, 尤其是在基类有很多构造函数的情况下.

    struct Base
    {
        int x;
        double y;
        string s;
        
        Base(int i) : x(i), y(0){};
        Base(int i, double j) : x(i), y(j){};
        Base(int i, double j, const string& str) : x(i), y(j), s(str){};
    };

如果有一个派生类, 希望这个派生类也和基类采取一样的构造方式, 那么直接派生于基类是不能获取基类构造函数的, 因为C++派生类会隐藏基类的同名函数.

一个做法是在派生类中定义这些构造函数, 重复且烦琐. C++11的继承构造函数正是用于解决这个问题, 通过using Base::SomeFunction 来表示使用基类的同名函数, 通过using Base::Base来声明使用基类构造函数.

    struct Derived : Base 
    {
        using Base::Base;
    };
    
需要注意的是:

1. 继承构造函数不会初始化派生类新定义的成员
2. 这个特性对其他同名函数同样使用

# 原始字面量 #

原始字面量可以直接表示字符串的实际含义, 通过原始字面量R可以直接得到其原始意义的字符串:

    string s = R"(<HTML>
    <HEAD>
    <TITLE>This is a test</TITLE>
    </HEAD>
    <BODY>
    <P>Hello, C++ HTML World!</P>
    </BODY>
    </HTML>
    )";

原始字符串字面量的定义是R"xxx(raw string)xxx", 其中原始字符串必须用括号包含, 括号的前后可以添加其他字符串, 
所加字符串会被忽略, 而且必须在括号两边同时出现.

# final和override关键字 #

final关键字: 限制某个类不能被继承, 或者某个虚函数不能被重写.

    struct A
    {
        virtual void foo() final;
    };
    
    struct B final : A 
    {
        void foo();                // error
    };
    
    struct C : B                   // error
    {};

override关键字: 确保在派生类中声明的重写函数与基类的虚函数有相同的签名, 同时也明确表明会重写基类的虚函数, 
还可以防止因疏忽把本来想重写基类的虚函数声明成重载.

    struct A{
        virtual void func(){}; 
    };
    
    struct D : A {
        void func() override {};
    };

# 新增算法 #

| 算法 | 描述 |
|:--:|:--|
| all\_of | 检查区间中所有元素是否满足判断式 |
| any\_of | 检查区间中是否有至少一个元素满足判断式 |
| none\_of | 检查区间中所有元素是否不满足判断式 |
| find\_if\_not | 查找不符合条件的某个元素 |
| copy\_if | 复制满足条件的元素 |
| itoa | 生成一个有序序列 |
| minmax\_element | 获取最大和最小元素 |
| is\_sorted | 判断序列是否有序 |
| is\_sorted\_until | 返回序列中已排序部分 |


---
title: C++11学习之列表初始化
date: 2016-08-20 20:36:46
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
    C++11学习笔记之列表初始化. ---《深入应用C++11》
+ <!-- more -->

# 统一的初始化
对于普通数组和POD[^POD]类型, 在C++98/03中可以使用初始化列表进行初始化:

    int i_arr[3] = {1, 2, 3};
    long l_arr[] = {1, 2, 3, 4};
    
    struct A{
        int x;
        int y;
    } a = {1, 2};

[^POD]: 即plain old data类型,简单来说,就是可以直接使用memcpy复制的对象.

但是这种初始化方式在C++98/03中只能适用于以上两种数据类型.而在C++11中,列表初始化可以用于任何类型对象的初始化:

    class Foo{
    public:
        Foo(int) {};
    private:
        Foo(const Foo&);
    }
    
    int main(void){
        Foo a1(123);
        Foo a2 = 123;      // Error
        
        Foo a3 = {123};
        Foo a4{123};
        
        int a5 = {3};
        int a6{3};
        
        return 0;
    }
    
1. a3与a4使用新的初始化方式来初始化对象,效果如何a1.
2. a5与a6是基本数据类型,初始化方式和其他变量是统一的.
3. a3虽然使用的是等号,但是依然是列表初始化,不受拷贝构造的影响.
4. a4和a6的写法,不能使用在C++98/03中.
5. 这种变量名直接加上初始化列表的方式同样适用于普通数组和POD类型.
6. 列表初始化中使用等号与否不影响初始化的行为.
7. new操作符等可以使用()进行初始化的地方,也可以使用初始化列表.

        int *a = new int{1};
        double b = double {12.2};
        int *arr = new int[3] {1, 2, 3};

8. 列表初始化可以直接使用在函数的返回值上.

        struct Foo{
            Foo(int ,double){};
        };
        
        Foo func(void){
            return {1233, 1.0};         // 等价于 return Foo(1233, 1.0);
        }

# 列表初始化的使用细节

先看以下示例代码:

    struct A{
        int x;
        int y;
    } a = {1, 2};        // a.x=1, a.y=2
    
    struct B{
        int x;
        int y;
        B(int, int):x(0),y(1){};
    } b = {2, 3};        // b.x=0, b.y=1
    
1. a的初始化过程是C++98/03中就存在的聚合类型(Aggregates)初始化, 以拷贝的形式,用初始化列表中的值来初始化A中的成员;
2. B定义了一个构造函数,所以实际上的初始化是以构造函数进行的.

聚合体的定义如下:
1. 类型是一个普通数组(如 int[10]);
2. 类型是一个类(class, struct, union), 且:

    1. 无用户自定义构造函数
    2. 无私有或保护的非静态数据成员
    3. 无基类
    4. 无虚函数
    5. 不能有{}和=直接初始化的非静态数据成员

对于数组,只要该类型是一个普通数组,即使数组的元素并非聚合类型,这个数组本身也是一个聚合类型.

    int x[] = {1, 2};
    float y[4][3] = {
        {1, 3, 5},
        {2, 4, 6},
        {3, 5, 7},
    };
    char cv[4] = {'a', 'b', 'c', 'd'};
    std::string sa[3] = {"123", "456", "789"};
    
当类型是一个类时, 如果存在用户自定义的构造函数:

    struct Foo{
        int x;
        double y;
        int z;
        Foo(int x, int y){};
    };
    Foo foo {1, 2.5, 1};      // error
此时无法将Foo看作聚合类型,必须以自定义的构造函数来构造对象.

私有或保护的非静态数据成员情况如下:

    struct ST{
        int x;
        double y;
    protected:
        int z;
    } s {1, 2.5, 1};          // error
    
    struct Foo{
        int x;
        double y;
    protected:
        static int z;
    } foo {1, 2.5, 1};       // ok

对于规则5:

    struct ST{
        int x;
        double y = 0.0;
    } s {1, 2.5};            // error
在C++98/03中,y不能在声明时进行初始化,但C++11中放宽了限制.

对于非聚合类型, 如果要使用初始化列表,则需要自定义一个构造函数:

    struct ST{
        int x;
        double y;
        virtual void F(){};
    private:
        int z;
    public:
        ST(int i, double j, int k):x(i), y(j), z(k){};
    } s = {1, 2.5, 1};

聚合类型的定义不是递归的,即当一个类的非静态成员是非聚合类型时,它可以是聚合类型:

    struct ST{
        int x;
        double y;
    private:
        int z;
    };
    
    ST s = {1, 2.5, 1};       // error
    
    struct Foo{
        ST st;
        int x;
        double y;
    } foo {{}, 1, 2.5};       // ok
在对st进行初始化时使用了空的{}, 相当于调用ST无参构造函数.

总结:
1. 对聚合类型, 使用初始化列表相当于对其中的每个元素分别赋值;
2. 对非聚合类型, 则需要先自定义一个构造函数,使用初始化列表相当于调用对应的构造函数;

#  初始化列表
##  任意长度的初始化列表

    int arr[] {1, 2, 3};
    std::vector<int> arr = {
        1,
        2
    };
在以上代码中初始化列表可以是任意长度, 而以前的代码中的Foo确不具备这种能力.

实际上, stl中的容器是通过std::initializer\_list这个类模板来完成任意长度的支持的.
我们只需要为Foo添加一个std::initializer\_list 构造函数, 它也将拥有任意长度初始化的能力.

    struct Foo{
        Foo(std::initializer_list<int>) {};
    } foo = {1, 2, 3, 4};

我们可以通过std::initializer_list 接收初始化列表,并取出列表中的每个元素.

    void func(std::initializer_list<int> v){
        for(auto&& value: v){
            cout << value << endl;
        }
    }
如上,可通过std::initializer_list 作为参数一次传递同类型的多个数据.

## std::initializer_list 的一些细节
1. 是一个轻量级的容器,内部定义了iterator等容器必须的概念;
2. 对std::initializer_list<T>, 可以接收任意长度的初始化列表,但元素必须是同种类型T(或可转换为T);
3. 具有3个成员接口, size/begin/end;
4. 只能被整体初始化或赋值;
5. 遍历时取得的迭代器是只读的, 因此无法修改某一个元素的值, 但可以通过初始化列表的赋值做整体修改
6. std::initializer_list 不保存每个元素的拷贝,只存储引用,因此非常高效;

# 防止类型收窄
类型收窄只导致数据内容发生变化或者精度丢失的隐式类型转换,包括以下情况:
1. 从浮点数到整形
2. 从高精度浮点数到低精度浮点数
3. 从整形到浮点数且超出浮点数的表示范围
4. 从整形到一个长度较短的整形, 并超出长度较短的整形数表示范围

在C++98/03中, 编译器对类型收窄不会报错(给出一个警告), 而在C++11中,可以通过初始化列表防止类型收窄.

    int a = 1.1;                           // ok
    int b { 1.1 };                         // error
    
    float fa = 1e40;                       // ok
    float fb { 1e40 };                     // error
    
    float fc = (unsigned long long)-1;     // ok
    float fd { (unsigned long long)-1 };   // error
    float fe = (unsigned long long)1;      // ok
    float ff { (unsigned long long)1 };    // ok
    
    const int x = 1024, y = 1;
    char c = x;                            // ok
    char d { x };                          // error
    char e = y;                            // ok
    char f {y};                            // ok
其中变量x/y被定义为const int, 如果去掉const限定符, 则f的定义也会因为类型收窄而报错.

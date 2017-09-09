---
title: C++11学习之std::function与lambda
date: 2016-08-23 19:59:11
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
    C++11学习笔记之std::function, std::bind与lambda表达式. ---《深入应用C++11》
+ <!-- more -->

# 可调用对象
在C++中,存在可调用对象这个概念, 有如下几种定义:
1. 函数指针
2. 具有operator()成员函数的对象, 即仿函数
3. 是一个可被转换为函数指针的对象
4. 是一个类成员函数指针
   > 函数类型不能直接用来定义对象,而函数引用可看作一个const的函数指针
   
# std::function
std::function是一个可调用对象的包装器.它是一个类模板,可以容纳除了类成员函数指针之外的所有可调用对象.

通过指定它的模板参数,可以用统一的方式处理函数,函数对象,函数指针, 并允许保存和延迟调用.

    #include <functional>
    #include <iostream>
    using std::cout;
    using std::endl;
    using std::function;
    
    void func(void){
        cout << __FUNCTION__ << endl;
    } 
    
    struct Foo{
        static int foo_func(int a){
            cout << __FUNCTION__ << "(" << a << ")" << endl;
            return a;
        }
    }

    struct Bar{
        static int operator()(int a){
            cout << __FUNCTION__ << "(" << a << ")" << endl;
            return a;
        }
    }
   
    int main(void){
       function<void(void)> fr1 = func;        // 绑定一个普通函数
       fr1();
       
       std::function<int(int)> fr2 = Foo::foo_func;     // 绑定一个静态成员函数
       cout << fr2(123) << endl;
       
       Bar bar;
       fr2 = bar;           // 绑定一个仿函数
       cout << fr2(456) << endl;
       
       return 0;
    }
std::function可以取代函数指针的作用,比函数指针更灵活,便利,适合作为回调函数, 类似于C#中的委托.   

# std::bind
std::function并不能绑定成员函数,这是它的缺陷.利用std::bind可以弥补这个缺点.

std::bind的作用是将一个可调用对象与其参数一起绑定,绑定后的结果可以通过std::function进行保存.主要包括以下两个作用:
1. 将可调用对象与其参数一起绑定成为一个仿函数;
2. 将多元可调用对象转换为一元或多元可调用对象, 即绑定一部分参数.

例子如下:
    
    #include <iostream>
    #include <functional>
    
    void call_when_even(int x, const std::funciton<void(int)>& f){
        if (!(x&1)){
            f(x);
        }
    }

    void output(int x){
        std::cout << x << " ";
    }
    
    void output_add_2(int x){
        std::cout << x + 2 << " ";
    }

    int main(void){
        {
            auto fr = std::bind(output, std::placeholder::_1);
            for (int i=0; i<10; ++i){
                call_when_even(i, fr);
            }
            std::cout << std::endl;
        }
        {
            auto fr = std::bind(output_add_2, std::placeholder::_1);
            for (int i=0; i<10; ++i){
                call_when_even(i, fr);
            }
            std::cout << std::endl;
        }
        
        return 0;
    }
    // output
    // 0 2 4 6 8
    // 2 4 6 8 10

1. 可以使用auto或者std::function保存bind的返回值,其实std::bind的返回值时一个stl内部定义的仿函数;
2. std::placeholder是一个占位符,代表这个位置将在调用时被传入的对应位置的参数替代;

参数绑定的使用实例如下:

    struct A{
        int m_i = 0;
        
        void outpur(int x, int y){
            cout << x << "  " << y << endl;
        }
    }
    
    int main(void){
        A a;
        function<void(int, int)> fr = bind(&A::output, &a, placeholder::_2, placeholder::_1);
        fr(1, 2);          // output: 2  1
        
        std::function<int&(void)> fr_i = bind(&A::m_i, &a);
        fr_i() = 123;         
        cout << a.m_i << endl;      // output: 123
        
        return 0;
    }

bind具有非常强大的功能,使用bind与function配合,所有的可调用对象都有了统一的操作方法.
## 使用bind简化bind1st和bind2nd
假设我们需要查找大于10和小于10的元素个数, 使用bind1st和bind2nd 实现如下:

    // > 10
    int count = std::count_if(coll.begin(), 
        coll.end(),
        std::bind1st(less<int>(), 10)
    );
    
    // < 10
    int count = std::count_if(coll.begin(), 
        coll.end(),
        std::bind2nd(less<int>(), 10)
    );
 
 这种实现方式并不友好,需要我们区分开bind1st和bind2nd;
 
 使用bind简化如下:
 
    // > 10
    int count = std::count_if(coll.begin(), 
        coll.end(),
        std::bind(less<int>(), 10, placeholder::_1)
    );
    
    // < 10
    int count = std::count_if(coll.begin(), 
        coll.end(),
        std::bind(less<int>(), placeholder::_1, 10)
    );

## 组合bind
bind可以组合多个函数,形成一个功能更强大的函数.

    // 找出>5 and <=10的元素个数
    auto f = bind(logical_and<bool>(),
        bind(greater<int>(), placeholder::_1, 5),
        bind(less_equal<int>(), placeholder::_1, 10)
    );
    int count = count_if(coll.begin(), coll.end(), f);

# lambda表达式
lambda来源于函数式编程的概念,也是现代编程语言的一个特点.lambda表达式有以下优点:

1. 声明式编程风格: 就地匿名定义目标函数或函数对象, 具有更好的可读性和可维护性
2. 简洁: 避免定义只使用一次的函数或函数对象, 避免代码膨胀和功能分散
3. 实现闭包

## 概念和基本用法
lambda表达式定义了一个匿名函数,并且可以捕获一定范围内的变量.语法如下:

    [ capture ] (params) opt -> ret { body; };

其中, capture是捕获列表,params是参数表, opt是函数选项, ret是返回值类型, body是函数体.

一个简单的例子如下:

    auto f = [](int a) -> int {
        return a + 1;
    };
    std::cout << f(1) << std::endl;     // output: 2

其中,返回值类型可以省略,编译器会根据return语句自动推导返回类型.但是初始化列表不能用于自动推导:

    auto x1 = [](int i){ return i; };    // ok
    auto x2 = []{ return {1, 2}; };    // error

lambda表达式可以通过捕获列表捕获一定范围内的变量:
1. []: 不捕获任何变量
2. \[&\]: 按引用捕获外部作用域的所有变量
3. \[=\]: 按值捕获外部作用域的所有变量
4. \[=, &foo\]: 按引用捕获foo,并按值捕获其余变量
5. \[bar\]: 按值捕获bar,不捕获其余变量
6. \[this\]: 捕获当前类中的this指针,让lambda表达式拥有和this类成员函数相同的访问权限.如果使用&或=,默认添加此选项.

默认状态下的lambda表达式无法修改按值捕获的外部变量.如果需要修改,可以按引用捕获, 或者指定lambda表达式为mutable, 且必须写出参数表.

    int a = 0;
    auto f1 = [=]{return a++;};              // error
    auto f2 = [=]() mutable {return a++;};   // ok

在C++11中,lambda表达式的类型被称为闭包类型, 它是一个特殊的, 匿名的非nunion的类类型.
因此,我们可以认为它是一个带operator()的类(默认为const), 即仿函数.可以使用std::function和std::bind来存储和操作lambda表达式.

对于没有捕获任何变量的lambda表达式,可以转换为一个普通的函数指针:

    using func_t = int(*)(int);
    func_t f = [](int a){return a;};
    f(123);

lambda表达式是就地定义仿函数的语法糖, 被捕获的变量会成为闭包类型的成员变量.

## 声明式编程风格
先看一个例子:

    std::vector<int> v{1, 2, 3, 4, 5};
    int even_count = 0;
    for_each(v.begin(), v.end(), [&even_count](int val){
        if (!(val & 1)){
            ++even_count;
        }
    });
    std::cout << even_count << std::endl;
    // output: 2

lambda表达式可以就地封装短小的闭包功能,让上下文紧密结合.

## 实现闭包
计算集合中大于5小于10的元素个数:

    int count = count_if(coll.begin(), coll.end(), [](int x){
        return x > 5 && x < 10;
    });

可以看到,lambda表达式比bind灵活性更好,也更为简洁.

# 其他细节
## bind的参数个数

    void func(int i, int j)
    {
        cout << "i=" << i << endl;
        cout << "j=" << j << endl;
    }
    
    int main(int argc, char* argv[])
    {
        auto f = std::bind(func, placeholders::_1, placeholders::_1);
        f(2);
        // output:
        // i=2
        // j=2
        
        f(4, 5, 7);
        // output:
        // i=4
        // j=4
        
        return 0;
    }
从上可以看出,bind可以传递多的参数,只不过参数会被忽略;

## lamdba表达式的类型

    auto f1 = [](int i){return i;};
    auto f2 = [](int i){return i;};

    cout << is_same<decltype(f1), decltype(f2)>::value << endl;
    // output: 
    // 0
从上可以看出, 就算是完全相同的两个lambda表达式,也是不同的类型.

## bind与lambda对比
lambda相对与bind来说更简洁,而且可以实现bind的所有功能. 所以在C++中, 应该尽可能使用lambda来替代bind.

在[stack overflow](http://stackoverflow.com/)上有个提问,对比了bind和lamdba.

[Why use `std::bind` over lambdas in C++14?](http://stackoverflow.com/questions/17363003/why-use-stdbind-over-lambdas-in-c14/17545183)

简要介绍如下:
### 实现template
使用bind可以实现绑定模板函数:

    struct Foo{
        using result_type void;
        
        template <typename A, typename B>
        void operator()(A a, B b){
            cout << a << "  " << b;
        }
    };
    
    auto f = bind(Foo(), _1, _2);
    f("test", 1.2f);
    // output:
    // test 1.2
在C++11中lambda不能实现这种功能, 但在C++14中引入了auto参数,等价版本如下:

    auto f = [](auto a, auto b){
        cout << a << "  " << b << endl;
    };
    f("test", 1.2f);

### 调用重载函数
    
    struct F {
        bool operator()(char, int);
        std::string operator()(char, char);
    };

    auto f = std::bind(F(), 'a', std::placeholders::_1);
    bool b = f(1);
    std::string s = f('b');
lambda暂时不能实现此功能.

### Scott Meyers的观点

Scott.Meyers[^Scott.Meyers]探讨过[这个问题](http://www.meetup.com/ocppug/events/122753582/), 他的观点如下:

[^Scott.Meyers]: 世界顶级的C++软件开发技术权威之一.著有Effective C++三卷本, 强烈推荐阅读.

1. 在C++14中bind并不比lambda更强大;
2. 在C++11中lambda还不能实现以下功能:

    * 不能在捕获变量时使用std::move, 即 auto f1 = bind(f, 42, _1, std::move(v));
    * 不能捕获表达式, 即auto f1 = bind(f, 42, _1, a + b);
    * 函数重载, 即template式;
    * 参数的完美转发;

3. 在C++14中都可以实现:
   
    * auto f1 = [v = std::move(v)](auto arg){ f(42, arg, std::move(v));};
    * auto f1 = [sum = a + b](auto arg){f(42, arg, sum);};
    * 见上方**实现template**小节
    * auto f1 = [=](auto&& arg){f(42, std::forward<decltype(arg)>(arg));};

4. bind的缺陷
   
    * bind更难进行inline
    * bind通过名字进行捕获, 有时会出现编译错误.
      
            void f(int);
            void f(char);
            auto f1 = bind(f, _1, 42);    // compile error
    

5. lambda的缺陷
   
    * lambda更容易造成代码膨胀, 因为会产生更多的**template code**.

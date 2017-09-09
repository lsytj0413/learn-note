---
title: C++11学习之移动语义与右值引用
date: 2016-08-27 09:08:39
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
    C++11学习笔记之移动语义与右值引用. ---《深入应用C++11》
+ <!-- more -->

# 右值引用 #

C++11新增加了一个类型,称为右值引用(R-value reference), 标记为T&&,与左值相对.

+ 左值: 表达式结束后依然存在的持久对象;
+ 右值: 表达式结束后不再存在的临时对象;

一个区分左值和右值的便捷方法是: 看能不能对表达式取地址,如果能,则为左值;否则为右值.所有的具名变量和对象都是左值, 而右值不具名.

在C++11中,右值由两个概念构成,一个是将亡值(xvalue, expiring value);另一个是纯右值(prvalue,PureRvalue).

比如,非引用返回的临时变量,运算表达式产生的临时变量,原始字面量和lambda表达式都是纯右值.

而将亡值是X++11新增加的与右值引用相关的表达式,例如将要被移动的对象,T&&函数返回值,std::move返回值和转换为T&&类型的转换函数的返回值.

    int i = 0;  // i为左值,0为右值

## &&的特性 ##

右值引用就是对一个右值进行引用的类型.因为右值不具名,所以只能通过引用的方式得到它.

    template <typename T>
    void f(T&& param);
    
    f(10);         // 右值
    int x = 10;
    f(x);          // 左值

在上例中, param有时是左值,有时是右值. 可以认为param实际上是一个未定的引用类型, 称之为universal reference. 它由左值初始化即为左值, 由右值初始化即为右值.

需要注意, 只有当发生类型推导(函数模板的类型自动推导,或auto)时,&&才是一个universal reference, 且只在T&&下发生.

    template <typename T>
    void f(T&& param);          // universal reference
    
    template <typename T>
    class Test{
        Test(Test&& rhs);       // 右值引用
    };
    
    void f(Test&& param);       // 右值引用 
   
    template <typename T>
    void f(std::vector<T>&& param);          // 右值引用

    template <typename T>
    void f(const T&& param);                 // 右值引用

universal reference具体推导出的类型遵守C++11的引用折叠规则. 规则如下:

1. 所有的右值引用叠加到右值引用仍然为右值引用;
2. 所有的其他引用类型的叠加都得到左值引用.

例子如下:
    
    int&& var1 = x;            
    auto&& var2 = var1;        // var2 = int&
    
    int w1, w2;
    auto&& v1 = w1;            // v1 = int&
    decltype(w1)&& v2 = w2;    // error
    decltype(w1)&& v3 = std::move(w2);

编译器会将已命名的右值引用视为左值, 将未命名的右值引用视为右值.

    void f(int& i){
        cout << "lvalue" << endl;
    }
    
    void f(int&& i){
        cout << "rvalue" << endl;
    }

    void forward(int&& i){
        f(i);
    }
    
    int main(){
        int i = 0;
        f(i);               // lvalue
        f(1);               // rvalue
        forward(2);         // lvalue
        
        return 0;
    }

在T&&中,需要注意推导出的T的类型.

    template <typename T>
    void f(T&& t);
    
    int main(){
        string s = "";
        f(s);                      // T = string&
        f(std::move(s));           // T = string
    }

总结如下:

1. 左值和右值是独立于它们的类型的, 右值引用类型可能是左值,也可能是右值;
2. auto&&或自动推导的T&&是一个未定的引用类型, 被称为universal reference, 它是左值还是右值取决于初始化值的类型;
3. 所有的右值引用叠加到右值引用仍然为右值引用, 其他引用叠加则为左值引用.当T&&为模板参数时,输入左值为左值引用,输入右值则为具名的右值引用;
4. 编译器将命名的右值引用视为左值, 将未命名的右值引用视为右值.

## 右值引用优化性能,避免深拷贝 ##

对于含有堆内存的类,我们需要提供深拷贝的拷贝构造函数,否则默认的构造函数会导致堆内存的重复释放.

    class A{
    public:
        A():m_ptr(new int(10)){};
        ~A(){delete m_ptr};
    private:
        int* m_ptr;
    };
        
    A get(bool flag){
        A a;
        A b;
        if (flag){                // 避免返回值优化(RVO)
            return a;
        }
        else{
            return b;
        }
    };
    
    int main(){
        A a = get(true);         // 重复delete
        return 0;
    }
   
在这种情况下,需要提供深拷贝函数来保证安全性.但是有些时候这种拷贝是不需要的,比如在上面的代码中,

get函数返回的临时变量会马上被销毁,而如果这时候进行深拷贝,会带来额外的性能损耗.在C++11中可以通过移动构造来避免这个问题.
  
移动语义可以将资源通过浅拷贝的方式从一个对象移动到另一个对象,这样可以减少不必要的临时对象的创建,拷贝以及销毁.可以大幅度提高C++应用程序的性能,消除临时变量对性能的影响.
    
    class MyString{
    private:
        char* m_dta;
        size_t m_len;
        
        void copy_data(const char* s){
            m_data = new char[m_len+1];
            memcpy(m_data, s, m_len);
            m_data[m_len] = '\0';
        };
        
    public:
        MyString(){
            m_data = nullptr;
            m_len = 0;
        };
        
        MyString(const char* p){
            m_len = strlen(p);
            copy_data(p);
        };
        
        MyString(const MyString& str){
            m_len = str.m_len;
            copy_data(str.m_data);
        };
        
        MyString& operator=(const MyString& str){
            if(this != &str){
                m_len = str.m_len;
                copy_data(str.m_data);
            }
        };
        
        virtual ~MyString(){
            if (m_date){
                delete []m_data;
                m_data = nullptr;
            }
        };
        
        MyString(MyString&& str){
            m_len = str.m_len;
            m_data = str.m_data;
            str.m_data = nullptr;
            str.m_len = 0;
        };
        
        MyString& operator=(MyString&& str){
            if (this != &str){
                m_len = str.m_len;
                m_data = str.m_data;
                str.m_data = nullptr;
                str.m_len = 0;
            }
        }; 
    }

可以看到在上例中,我们可以通过移动构造与移动拷贝避免无谓的内存分配和释放.

在提供移动构造和移动拷贝的时候,我们也需要提供常量左值引用的构造和拷贝,以处理不能移动的情况.

# move语义 #

通过以上内容我们知道,移动语义是通过右值引用来匹配临时值的.C++11提供了std::move来使普通左值也能够利用移动语义来优化性能.

std::move只是将对象的状态或所有权转移到另一个对象,并没有内存拷贝.std::move实际上并不能移动任何东西,它只是将一个左值引用转换为一个右值引用.

    A foo();
    A a;
    a = foo();

在C++中最后一个赋值会发生以下动作:

1. 销毁a所持有的资源;
2. 复制foo返回的临时变量所拥有的资源;
3. 销毁临时对象,释放其资源.

但是当A所持有的资源比较大时,销毁和复制的代价很大,性能很低.正确的做法是交换a和foo返回值的资源,让临时对象去销毁a所持有的以前的资源.

    {
        vector<string> tokens;
        vector<string> t = tokens;      // 拷贝,代价大
    }
    {
        vector<string> tokens;
        vector<string> t = std::move(tokens);    // 移动,代价小.但此句执行后tokens将不再持有资源
    }

# forward和完美转发 #

我们知道,右值引用类型是独立于值的.当一个右值引用参数作为函数的形参,在函数内部再进行转发的时候该参数就是一个左值了.

因此,我们需要一种方法能按照参数原来的类型转发到另外一个函数,这种转发被称为完美转发.

所谓完美转发,是指在函数模板中,完全依照模板的产生的类型(即保持左右值特征),将参数传递给函数模板中调用的另外一个函数.

    template <typename T>
    void p(T& t){
        cout << "lvalue" << endl;
    };
    
    template <typename T>
    void p(T&& t){
        cout << "rvalue" << endl;
    };
    
    template <typename T>
    void forward(T&& v){
        p(v);
        p(std::forward<T>(v));
        p(std::move(v));
    };
    
    int main(){
        forward(1);
        int x = 1;
        forward(x);
        forward(std::forward<int>(x));
        p(std::forward<int&>(x));
        return 0;
    }; 
   
    // output
    // lvalue
    // rvalue
    // rvalue
    // lvalue
    // lvalue
    // rvalue
    // lvalue
    // rvalue
    // rvalue
    // lvalue
    
1. forward(1): 由于1是右值,所以T&&被推导为右值引用, 但在p(v)时v是一个左值,所以得出该输出;
2. forward(x): 由于x是左值,所以T&&被推导为左值引用,得到该输出
3. forward(std::forward<int>(x)): 由于std::forward<int>(x)得到一个右值,所以得到该输出
4. p(std::forward<int&>(x)): 由于std::forward<int>(x)得到一个左值,所以得到该输出

完美转发在编写模板的时候很有用,使我们可以根据模板参数的具体类型进行处理.

    template <typename F, typename... TArgs>
    inline auto Wrapper(F&& f, TArgs&&... args) -> decltype(f(std::forward<TArgs>(args)...))
    {
        return f(std::forward<TArgs>(args)...);
    };

# emplace_back减少内存拷贝和移动 #

在C++11中,标准容器提供了emplace\_back函数,该函数能就地通过参数构造对象,不需要拷贝或者移动内存,
相比push\_back能更好的避免内存的拷贝和移动,使容器插入元素的性能得到进一步提升.

所有的标准库容器(除array)都增加了类似方法,例如emplace, emplace\_hint, emplace\_front, emplace\_after和emplace\_back.

    struct A{
        int x;
        double y;
        A(int a, double b): x(a), y(b){};
    };
    
    int main(){
        vector<A> v;
        v.emplace_back(1, 2);
        return 0;
    };

emplace等函数比之前的函数性能更高,我们应该尽可能用emplace函数替代以前的函数.

但是如果容器中的size_type没有提供相应的构造函数,则emplace函数就不能使用.

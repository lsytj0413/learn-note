---
title: C++11学习之内存对齐
date: 2016-09-01 21:47:15
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
    C++11学习笔记之内存对齐. ---《深入应用C++11》
+ <!-- more -->

# 什么是内存对齐
内存对齐,或者说字节对齐,是指一个数据类型所能存放的内存地址的属性.这个属性是一个无符号整数,并且这个整数必须是2的N次方.
当我们说一个数据类型的内存对齐为8时,是指这个数据类型所定义出的所有变量的内存地址都是8的倍数.

当一个基本数据类型(Fundamental Types)的对齐属性和这个数据类型的大小相等时,这种对齐方式称为自然对齐.

为什么需要内存对齐呢?因为不是所有的硬件平台都能访问任意位置的内存.有些CPU,比如Alpha, IA-64, MIPS还有SuperH架构,
若读取的数据是未对齐的,将拒绝访问或抛出硬件异常.考虑到CPU处理内存的方式,使用内存对齐也会提高系统的性能.比如将一个int放在奇数地址上,
32位CPU需要两次读取,而对齐之后一次读取就可以了.

在有内存对齐之后,数据在内存中的存放就可能会出现一个空隙(Data Structure Padding).所以sizeof的结果有些时候和想象中的大小会不同:

    struct MyStruct{
        char a;                // 1 Byte
        int b;                 // 4 Byte
        short c;               // 2 Byte
        long long d;           // 8 Byte
        char e;                // 1 Byte
    };

可以看到,MyStruct的所有成员的直接相加结果为16,但在32位MSVC中它的sizeof结果是32.这是因为编译器在某些位置插入了Padding.

假设MyStruct的整体偏移从0x00开始,则结构体的整体内存分布如图:

| 偏移 | 大小 | 说明 |
|:--:|:--:|:--|
| 0 | 1 | char a |
| 1 | 3 | padding |
| 4 | 4 | int b |
| 8 | 2 | short c |
| 10 | 6 | padding |
| 16 | 8 | long long d |
| 24 | 1 | char e |
| 25 | 7 | padding |

整体的结构填充结果如下:

    struct MyStruct{
        char a;                // 1 Byte
        char pad_0[3];
        int b;                 // 4 Byte
        short c;               // 2 Byte
        char pad_1[6];
        long long d;           // 8 Byte
        char e;                // 1 Byte
        char pad_2[7];
    };

在以上结果中我们看到,在结构体的最后还跟了7个字节的padding,这是因为结构体的整体大小必须是能被对齐值整除的.
所以在char e;之后还填充了7个字节,让结构体的整体大小是8的倍数32.

如果你在GCC+32位Linux中测试sizeof(MyStruct), 得到的结果会是24.这是因为GCC中的对齐规则和MSVC不同,
不同平台下使用的默认对齐值可能是不同的.在GCC+32位Linux中,超过4字节的基本类型仍然按照4字节对齐.

    struct MyStruct{
        char a;                // 1 Byte
        char pad_0[3];
        int b;                 // 4 Byte
        short c;               // 2 Byte
        char pad_1[2];
        long long d;           // 8 Byte
        char e;                // 1 Byte
        char pad_2[3];
    };
    
对于结构体本身的对齐值来说,为了保证结构体内的每个成员都能放在自然对齐的位置上,结构体本身最理想的对齐值是结构体内最大对齐数值成员的对齐值.
对MyStruct来说,结构体本身的对齐值应该是8.并且,当我们强制对齐值小于8时(比如为2), 结构体内部成员的对齐值也将被强制为不超过2.
因为对于一个数据类型来说,其内部成员的位置应该是固定的,如果结构体按照1字节对齐,而成员却按照各自的方式对齐,有可能出现成员的相对偏移量随内存位置而改变的问题.

例如: 假设MyStruct的起始地址为0x01,那么a和b之间会有2个字节的padding;而如果MyStruct的起始地址为0x03,那么a和b之间就不会有padding.

# 堆内存的内存对齐

在讨论内存对齐的时候一般忽略堆内存.实际上,malloc一般使用当前平台默认的最大内存对齐数对齐内存,所以当我们自定义的内存对齐超出了这个范围,则不能直接使用malloc获取内存.

当我们需要分配一块具有特定内存对齐的内存块时,在MSVC下应该使用\_aligned\_malloc,在GCC下一般使用memalign等函数.

其实自己实现一个aligned\_malloc很简单,代码如下:

    #include <assert>
    
    inline void* aligned_malloc(size_t size, size_t alignment)
    {
        assert(!(alignment & (alignment - 1)));
        
        size_t offset = sizeof(void*) + (--alignment);
        char *p = static_cast<char*>(malloc(offset + size));
        if (!p){
            return nullptr;
        }
        
        void *r = reinterpret_cast<void*>(reinterpret_cast<size_t>(p + offset) & (~alignment));
        static_cast<void**>(r)[-1] = p;
        return r;
    }
    
    inline void aligned_free(void* p)
    {
        free(static_cast<void**>(p)[-1]);
    }

# 利用alignas指定内存对齐大小

有时我们不希望按照默认的方式来对齐,这时可以使用alignas来指定内存对齐的大小:

    alignas(32) long long a = 0;
    
    #define XX 1
    struct alignas(XX) MyStruct_1{
    };

    template <size_t YY = 1>
    struct alignas(YY) MyStruct_2{};
    
    static const unsigned ZZ = 1;
    struct alignas(ZZ) MyStruct_2{};

    alignas(int) char c;
    
注意:
1. 在C++11中,只要是一个编译期常数都支持alignas;
2. alignas只能改大不能改小;
3. 如需要改小可使用#pragma pack,或使用C++11中的等价物 _Pragma

示例如下:

    _Pragma("pack(1)")
    struct MyStruct{};
    _Pragma("pack()")

# 利用alignof 和std::alignment_of获取内存对齐大小

alignof可以获取内存对齐大小(也可作用与变长参数类型,同sizeof), 使用方式如下:

    MyStruct xx;
    cout << alignof(xx) << endl;
    cout << alignof(MyStruct) << endl;
    
std::alignment\_of 的功能是编译期计算类型的内存对齐, 以补充alignof的功能.
alignof只能返回一个size\_t, 而alignment\_of继承自std::intergral\_constant, 拥有value\_type, type和value等成员.

    cout << std::alignment_of<MyStruct>::value;
    cout << alignof(MyStruct);
    
std::alignment\_of的简单实现方式如下:

    template <class T>
    struct alignment_of : std::intergral_constant< std::size_t, alignof(T)>
    {};

# 内存对齐的类型std::aligned_storage

std::aligned\_storage可以看作一个内存对齐的缓冲区, 原型如下:

    template <std::size_t len, std::size_t Align = /**/>
    struct aligned_storage;
    
其中len表示所存储类型的size,Align表示该类型内存对齐的大小.
通过sizeof和alignof可以获取size和内存对齐大小,所以std::aligned\_storage的声明是: std::aligned\_storage<sizeof(T), alignof(T)>.
alignof是VS2013 CTP才支持的,如果没有该版本可以使用std::alignment_of来代替.

std::aligned\_storage一般和placement new结合使用, 用法如下:

    struct A{
        int avg;
        A(int a, int b): avg((a+b)/2){};
    };
    
    using Aligned_A = std::aligned_storage<sizeof(A), alignof(A)>::type;
    
    int main(){
        Aligned_A a, b;
        new (&a) A(10, 20);
        b = a;
        cout << reinterpret_cast<A&>(b).avg << endl;
        return 0;
    }

为什么要使用std::aligned\_storage?很多时候我们需要分配一块内存块, 然后使用placement new构造对象:

    char xx[32];
    ::new (xx) MyStruct;
    
但是char[32]是1字节对齐的,xx可能不再MyStruct指定的对齐位置上, 从而引起效率问题或出错.
这时可以使用std::aligned\_storage来构造内存块:

    std::aligned_storage<sizeof(MyStruct), alignof(MyStruct)>::type xx;
    ::new (&xx) MyStruct;
    
注意: 当使用堆内存时可能还需要aligned_malloc.

# std::max_align_t和std::align操作符

std::max\_align\_t返回当前平台的最大默认对齐值, 对于malloc返回的内存, 其对齐和std::max\_align\_t的对齐大小应当是一致的.

std::align用来在一块内存中获取一个符合指定内存要求的地址:

    char buf[32];
    void *pt = buffer;
    std::size_t space = sizeof(buffer) - 1;
    std::align(alignof(int), sizeof(char), pt, space);
    
说明: 在buffer这个内存块中, 指定内存对齐为alignof(int), 找一块sizeof(char)的内存, 将地址放入pt,将buffer从pt开始的长度放入space.

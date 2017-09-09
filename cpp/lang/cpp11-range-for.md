---
title: C++11学习之基于范围的for循环
date: 2016-08-22 20:42:01
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
    C++11学习笔记之基于范围的for循环. ---《深入应用C++11》
+ <!-- more -->

# 新的for循环语法
在C++中,我们经常需要遍历一个容器,针对每个元素进行处理, 代码如下:

    std::vector<int> arr;
   
    // 直接迭代
    for(auto it = arr.begin(); it != arr.end(); ++it){
        // do something
    }
    
    // 借助algorithm中的for_each
    // 其中functor是一个函数对象
    std::for_each(arr.begin(), arr.end(), functor);
在以上两种写法中,都需要提供begin和end.
对比python中的迭代方式:

    l = [1, 2, 3, 4]
    for num in l:
        print num
可以看出python代码更简洁, 表现力也更强.
在C++11中引入了基于范围的for循环,使得我们也可以编写出更简洁的循环代码, 示例如下:

    std::vector<int> arr;
    for (auto num : arr){
        // do something
    }

# 使用细节
## 循环变量的类型
先看一个例子:

    std::map<std::string, int> m = {
        { "1", 2 },
        { "2", 4 },
        { "3", 6 }
    };
    
    for(auto& val : m){
        std::cout << val.first << "->" << val.second << std::endl;
    }
    // output
    // 1 -> 2
    // 2 -> 4
    // 3 -> 6
可以看出以下两点:
1. val的类型是std::pair, 所以需要使用val.first和val.second来取值;
2. auto自动推导出的类型是容器中的value_type,而不是迭代器

## 容器本身的约束
在使用基于范围的for循环时,也要遵循容器本身的约束.

    std::set<int> ss = { 1, 2, 3};
    for(auto& val : ss){
        val++;        // error, val is read-only reference
    }
因为set内部的元素是只读的,所以val被推导为 const int&.

## 求值次数

    std::vector<int> arr;
    std::vector<int>& get_range(){
        return arr;
    }
    
    for(auto val : get_range()){
        // do something
    }
执行以上代码, 可以发现get_range只被调用一次,所以:
1. 对于基于范围的for循环,冒号后面的表达式只会执行一次.

## 修改容器

    std::vector<int> arr = { 1, 2, 3, 4};
    for(auto val : arr){
        std::cout << val << std::endl;
        arr.push_back(0);
    }
    // output
    // 1
    // 5189584
    // -17891602
    // -17891602
    // -17891602
可以看出有迭代器失效的情况出现, 这是因为基于范围的for循环只是一个语法糖, 等价的for语句如下:

    std::vector<int> arr = { 1, 2, 3, 4};
    auto&& __range = (arr);
    for (auto __begin = __range.begin(), __end = __range.end();
        __begin != __end;
        ++__begin
    ){
        auto val = *__begin;
        std::cout << val << std::endl;
        arr.push_back(0);
    }

# 让自定义类型支持基于范围的for循环
基于范围的for循环使用以下方式查找容器的begin和end:
1. 若容器是一个array, 则begin为arr的首地址, end为首地址加容器长度
2. 如果是类, 则使用类的成员函数begin和end;
3. 否则,使用全局的begin和end函数来定位begin,end迭代器;

由上述可知, 我们只需要为自定义类型实现begin和end函数揭开.
具体例子为一个range对象, 使用方式为:

    for(int i : range(3)){
        cout << i << endl;
    }
    // output
    // 0
    // 1
    // 2

具体代码可参看:
[range的实现](https://github.com/lsytj0413/liter/blob/master/liter/utils/range.h)

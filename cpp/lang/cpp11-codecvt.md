---
title: C++11学习之字符转换
date: 2016-09-10 21:15:26
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
    C++11学习笔记之数值和字符串的转换, 宽窄字符转换. ---《深入应用C++11》
+ <!-- more -->

# 数值类型和字符串的相互转换 #

C++11提供了to\_string方法,可以方便的将各种数值类型转换为字符串类型.

    std::string to_string(int value);
    std::string to_string(long value);
    std::string to_string(long long value);
    std::string to_string(unsigned value);
    std::string to_string(unsigned long value);
    std::string to_string(unsigned long long value);
    std::string to_string(float value);
    std::string to_string(double value);
    std::string to_string(long double value);

    std::wstring to_wstring(int value);
    std::wstring to_wstring(long value);
    std::wstring to_wstring(long long value);
    std::wstring to_wstring(unsigned value);
    std::wstring to_wstring(unsigned long value);
    std::wstring to_wstring(unsigned long long value);
    std::wstring to_wstring(float value);
    std::wstring to_wstring(double value);
    std::wstring to_wstring(long double value);

C++11还提供了字符串转换为整型和浮点型的方法:

    int std::atoi(const char*);
    long std::atol(const char*);
    long long std::atoll(const char*);
    float std::atof(const char*);

# 宽窄字符转换 #

C++11增加了unicode字面量的支持, 可以通过L来定义字符:

    std::wstring str = L"中国人";
    
将宽字符串转换为窄字符串需要用到codecvt库中的std::wstring\_convert.
std::wstring\_convert需要借助以下几个unicode转换器:

1. std::codecvt_utf8: 封装了UTF-8到UCS2及UTF-8到UCS4的编码转换
2. std::codecvt_utf16: 封装了UTF-16与UCS2及UTF-16与UCS4的编码转换
3. std::codecvt_utf8_utf16: 封装了UTF-8与UTF-16的编码转换

std::string和std::wstring之间的转换示例如下:

    std::wstring str = L"中国人";
    std::wstring_convert<std::codecvt<wchar_t, char, std::mbstate_t>> 
    converter(new std::codecvt<wchar_t, char, std::mbstate_t>("CHS"));
    
    std::string narrowStr = converter.to_bytes(str);
    std::wstring wstr = converter.from_bytes(narrowStr);
    
    cout << narrowStr << endl;
    
    wcout.imbue(std::locale("chs"));
    wcout << wstr << endl;

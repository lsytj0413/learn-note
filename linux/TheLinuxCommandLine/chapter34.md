# 第三十四章: 字符串和数字 #

## 34.1 参数扩展 ##

### 34.1.1 基本参数 ###

参数扩展的最简单形式体现在平常对变量的使用中, 例如 $a 扩展后称为变量a所包含的内容, 简单参数也可以被大括号包围, 例如 ${a}.

### 34.1.2 空变量扩展的管理 ###

有的参数扩展用于处理不存在的变量和空变量, 形式如下:

```
${parameter:-word}
```

如果parameter未被设定或者是空参数, 则其扩展为word的值; 如果parameter非空, 则扩展为parameter的值.

另外一种扩展形式如下:

```
${parameter:=word}
```

如果parameter未被设定或者是空参数, 则其扩展为word的值, 同时将值赋值给parameter; 如果parameter非空, 则扩展为parameter的值.

需要注意的是, 位置参数和其他特殊参数不能使用这种方式赋值.

第三种扩展形式如下:

```
${parameter:?word}
```

如果parameter未被设定或者是空参数, 则扩展会导致脚本出错而退出, 同时word的内容会输出到标准错误; 如果parameter非空, 则扩展为parameter的值.

第四种扩展形式如下:

```
${parameter:+word}
```

若parameter未设定或为空, 将不产生任何扩展; 若parameter非空, word的值将取代parameter的值, 但是parameter的值不发生变化.

### 34.1.3 返回变量名的扩展 ###

shell具有返回变量名的功能, 形式如下:

```
${!prefix*}
${!prefix@}
```

该扩展返回当前以prefix开头的变量名, 根据bash文档, 这两种扩展形式执行效果相同.

### 34.1.4 字符串操作 ###

对字符串的操作存在着大量的扩展集合, 其中一些扩展尤其适用于对路径名的操作, 形式如下:

```
${#parameter}
```

扩展为parameter内包含的字符串的长度, 一般来说参数parameter是个字符串, 如果parameter是 @ 或 *, 那么扩展结果就是位置参数的个数.

提取字符串的扩展形式如下:

```
${parameter:offset}
${parameter:offset:length}
```

这个扩展可以提取一部分包含在参数parameter中的字符串, 扩展以offset字符开始, 直到字符串末尾, 除非length特别指定.

如果offset的值为负, 则表示从字符串末尾开始, 需要注意的是, 负值前必须有一个空格, 如果有length的话, length不能小于0.

如果参数是@的话, 扩展的结果则是从offset开始, length为位置参数.

去除字符串内容的扩展形式如下:

```
${parameter#pattern}
${parameter##pattern}
${parameter%pattern}
${parameter%%pattern}
```

根据pattern的定义, 这些扩展去除了包含在pattern中的字符串的主要部分, pattern是一个通配符模式. # 形式去除最短匹配, ## 形式去除最常匹配, %和%%形式则是从字符串末尾去除文本.

对字符串进行替换的扩展如下:

```
${parameter/pattern/string}
${parameter//pattern/string}
${parameter/#pattern/string}
${parameter/%pattern/string}
```

这种形式的展开对 parameter 的内容执行查找和替换操作. 如果找到了匹配通配符 pattern 的文本, 则用 string 的内容替换它.
在正常形式下, 只有第一个匹配项会被替换掉, 在 // 形式下, 所有的匹配项都会被替换掉.  /# 要求匹配项出现在字符串的开头, 而 /% 要求匹配项出现在字符串的末尾. /string 可以省略掉, 这样会导致删除匹配的文本.

参数扩展是一个重要的功能, 进行字符串操作的扩展可以替代其他常用的命令, 例如set和cut命令. 扩展通过取代外部程序, 也改善了脚本的执行效率.
使用参数扩展修改 longest-word程序如下:

```
#!/bin/bash
# longest-word3 : find longest string in a file
for i; do
    if [[ -r $i ]]; then
        max_word=
        max_len=
        for j in $(strings $i); do
            len=${#j}
            if (( len > max_len )); then
                max_len=$len
                max_word=$j
            fi
        done
        echo "$i: '$max_word' ($max_len characters)"
    fi
    shift
done
```

## 34.2 算术计算和扩展 ##

算术扩展的基本形式如下:

```
$((expression))
```

### 34.2.1 数字进制 ###

shell支持任何进制表示的整数, 如下表:

| 符号 | 描述 |
|:--|:--|
| Number | 十进制, 默认情况 |
| 0Number | 八进制, 以0开始的数字 |
| 0xNumber | 十六进制, 以0x开始 |
| base#Number | base进制的数字 |

例如:

```
echo $((0xff))
echo $((2#11111111))
```

### 34.2.2 一元运算符 ###

### 34.2.3 简单算术 ###

### 34.2.4 赋值 ###

### 34.2.5 位操作 ###

### 34.2.6 逻辑操作 ###

## 34.3 bc: 一种任意精度计算语言 ##

### 34.3.1 bc的使用 ###

### 34.3.2 脚本例子 ###

## 34.4 本章结尾语 ##

## 34.5 附加项 ##

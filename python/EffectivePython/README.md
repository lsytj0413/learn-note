# <Effective Python 读书笔记> #

[《Effective Python》](https://book.douban.com/subject/26312313/) 是由 [Brett Slatkin](https://github.com/bslatkin)  撰写的, 讲述如何以符合Python风格的 (Pythonic) 方式来编写程序. 
书中的每一个条目都是一项独立的教程, 并包含它自己的源代码, 给出了相当精炼而又符合主流观点的建议.

以下是各章节的内容:

- [第一章: 用Pythonic方式思考](https://github.com/lsytj0413/practice/blob/master/python/EffectivePython/chapter01.md)

    - 第1条: 确认自己所用的Python版本
    - 第2条: 遵循PEP8风格指南
    - 第3条: 了解bytes, str和unicode的区别
    - 第4条: 用辅助函数来取代复杂的表达式
    - 第5条: 了解切割序列的方法
    - 第6条: 在单次切片操作中, 不要同时指定start, end和stride
    - 第7条: 用列表推导来取代map和filter
    - 第8条: 不要使用含有两个以上表达式的列表推导
    - 第9条: 用生成器表达式来改写数据量较大的列表推导
    - 第10条: 尽量使用enumerate取代range
    - 第11条: 用zip函数同时遍历两个迭代器
    - 第12条: 不要在for和while循环后面写else块
    - 第13条: 合理利用try/except/else/finally结构中的每个代码块

- [第二章: 函数](https://github.com/lsytj0413/practice/blob/master/python/EffectivePython/chapter02.md)

    - 第14条: 尽量用异常来表示特殊情况, 而不要返回None
    - 第15条: 了解如何在闭包里使用外围作用域中的变量
    - 第16条: 考虑用生成器来改写直接返回列表的函数
    - 第17条: 在参数上面迭代时, 要多加小心
    - 第18条: 用数量可变的位置参数减少视觉杂讯
    - 第19条: 用关键字参数来表达可选的行为
    - 第20条: 用None和文档字符串来描述具有动态默认值的参数
    - 第21条: 用只能以关键字形式指定的参数来确保代码明晰

- [第三章: 类与继承](https://github.com/lsytj0413/practice/blob/master/python/EffectivePython/chapter03.md)

    - 第22条: 尽量用辅助类来维护程序的状态, 而不要用字典和元组
    - 第23条: 简单的接口应该接受函数, 而不是类的实例
    - 第24条: 以 @classmethod形式的多态取通用地构建对象
    - 第25条: 用super初始化父类
    - 第26条: 只在使用Mix-in组件制作工具类时进行多重继承
    - 第27条: 多用public属性, 少用private属性
    - 第28条: 继承collections.abc 以实现自定义的容器类型

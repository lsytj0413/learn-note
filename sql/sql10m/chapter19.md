# 第19章: 使用存储过程 #

## 19.1 存储过程 ##

存储过程是为以后使用而保存的一条或多条 SQL 语句.

## 19.2 为什么要使用存储过程 ##

- 通过把处理封装在一个易用的单元中可以简化复杂的操作
- 简化对变动的管理
- 通常以编译过的形式存储, 提高了性能

## 19.3 执行存储过程 ##

可以使用如下语句执行存储过程:

```
EXECUTE AddNewProduct('JTS01',
    'Stuffed Eiffel Tower',
    6.49,
    'Plush stuffed toy with the text');
```

## 19.4 创建存储过程 ##

每个 DBMS 的语法都可能不同.


# 第12章: 联结表 #

## 12.1 联结 ##

SQL 最强大的功能之一就是能在数据查询的执行中联结表, 联结是利用 SQL 的 SELECT 能执行的最重要的操作.

### 12.1.1 关系表 ###

关系表的设计是把信息分解成多个表, 一类数据一个表, 各表之间通过某些共同的值互相关联.

### 12.1.2 为什么使用联结 ###

如果数据存储在多个表中, 就需要使用联结来检索出数据.

## 12.2 创建联结 ##

```
SELECT vend_name, prod_name, prod_price
FROM Vendors, Products
WHERE Vendors.vend_id = Products.vend_id;
```

以上语句联结了两个表.

### 12.2.1 WHERE 子句的重要性 ###

在联结两个表时, 其实是将第一个表中的每一行与第二个表中的每一行配对, WHERE 子句作为过滤条件可以只包含那些匹配给定条件的行. 如果没有过滤条件则两个表的每一行都会匹配.

- 要保证所有联结都有 WHERE 子句

### 12.2.2 内联结 ###

上面的示例语句称为等值联结, 也称为内联结. 等价与以下语句:

```
SELECT vend_name, prod_name, prod_price
FROM Vendors INNER JOIN Products
    ON Vendors.vend_id = Products.vend_id;
```

### 12.2.3 联结多个表 ###

SQL 不限制一个 SELECT 语句中可以联结的表的数目:

```
SELECT prod_name, vend_name, prod_price, quantity
FROM OrderItems, Products, Vendors
WHERE Products.vend_id = Vendors.vend_id
    AND OrderItems.prod_id = Products.prod_id
    AND order_num = 20007;
```

- 联结的表越多, 性能越差
- SQL 本身不限制联结的数目, 但是多数 DBMS 都有限制


# 第13章: 创建高级联结 #

## 13.1 使用表别名 ##

SQL 中除了可以给列名和计算字段使用别名, 也可以给表使用别名. 例如:

```
SELECT cust_name, cust_contact
FROM Customers AS C, Orders AS O, OrderItems AS OI
WHERE C.cust_id = O.cust_id
    AND OI.order_num = O.order_num
    AND prod_id = 'RGAN01';
```

- 表别名只在查询执行中使用, 不返回到客户端

## 13.2 使用不同类型的联结 ##

### 13.2.1 自联结 ###

可以使用表别名在一条 SELECT 语句中不止一次引用相同的表:

```
SELECT c1.cust_id, c1.cust_name, c1.cust_contact
FROM Customers AS c1, Customers AS c2
WHERE c1.cust_name = c2.cust_name
    AND c2.cust_contact = 'Jim Jones';
```

### 13.2.2 自然联结 ###

内联结返回所有数据, 相同的列甚至多次出现. 自然联结排除多次出现, 每一列只返回一次.

```
SELECT C.*, O.order_num, O.order_date,
    OI.prod_id, OI.quantity, OI.item_price
FROM Customers AS C, Orders AS O, OrderItems AS OI
WHERE C.cust_id = O.cust_id
    AND OI.order_num = O.order_num
    AND prod_id = 'RGAN01';
```

### 13.2.3 外联结 ###

联结中包含了那些在相关表中没有关联行的行, 称为外联结.

```
SELECT Customers.cust_id, Orders.order_num
FROM Customers LEFT OUTER JOIN Orders
    ON Customers.cust_id = Orders.cust_id;
```

在使用 OUTER JOIN 时必须使用 RIGHT 或 LEFT 关键字指定包括其所有行的表, 也可以使用 FULL 关键字指定为全外联结.

## 13.3 使用带聚集函数的联结 ##

聚集函数可以和联结一起使用. 例如:

```
SELECT Customers.cust_id,
    COUNT(Orders.order_num) AS num_ord
FROM Customers INNER JOIN Orders
    ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_id;
```

## 13.4 使用联结和联结条件 ##

- 一般使用内联结
- 保证使用正确的联结条件
- 总是提供联结条件
- 在一个联结中可以包含多个表, 甚至可以对每个联结采用不同的联结类型

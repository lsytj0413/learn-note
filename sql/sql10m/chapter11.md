# 第11章: 使用子查询 #

## 11.1 子查询 ##

SQL 允许创建子查询, 即嵌套在其他查询中的查询.

## 11.2 利用子查询进行过滤 ##

现在我们有订单表, 订单物品表, 顾客表, 假如要列出购买了物品 RGAN01 的所有顾客, 普通的查询语句如下:

```
# 使用伪代码描述
R1 = SELECT order_num FROM OrderItems WHERE prod_id = 'RGAN01';
R2 = SELECT cust_id FROM Orders WHERE order_num IN (R1);
```

上述语句通过两次查询得到了顾客ID. 使用子查询可以将两次查询结合起来得到同样的结果:

```
SELECT cust_id
FROM Orders
WHERE order_num IN (SELECT order_num
                    FROM OrderItems
                    WHERE prod_id = 'RGAN01');
```

子查询总是从内向外处理.

- 子查询的 SELECT 语句只能查询单个列
- 子查询并不总是执行这类数据检索最有效的方法

## 11.3 作为计算字段使用子查询 ##

```
SELECT cust_name,
       cust_state,
       (SELECT COUNT(*) 
        FROM Orders 
        WHERE Orders.cust_id = Customers.cust_id) AS orders
FROM Customers
ORDER BY cust_name;
```

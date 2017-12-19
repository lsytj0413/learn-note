# 第18章: 使用视图 #

## 18.1 视图 ##

视图是虚拟的表, 只包含使用时动态检索数据的查询. 例如下列语句:

```
SELECT cust_name, cust_contact
FROM Customers, Orders, OrderItems
WHERE Customers.cust_id = Orders.cust_id
    AND OrderItems.order_num = Orders.order_num
    AND prod_id = 'RGAN01';
```

上述查询从3个表中获取数据, 使用者必须理解相关表的结构. 可以使用视图将其包装起来:

```
SELECT cust_name, cust_contact
FROM ProductCustomers
WHERE prod_id = 'RGAN01';
```

- 所有 DBMS 一致的支持视图创建语法

### 18.1.1 为什么使用视图 ###

- 重用SQL语句
- 简化复杂的 SQL
- 使用表的一部分而不是整个表
- 保护数据
- 更改数据格式和表示

视图仅仅是用来查看存储在别处数据的手段, 本身不包含数据.

### 18.1.2 视图的规则和限制 ###

一些常见的规则和限制如下:

- 视图名称必须唯一
- 视图数目没有限制
- 创建视图时必须有足够的访问权限
- 视图可以嵌套
- 许多 DBMS 禁止在视图查询中使用 ORDER BY
- 有些 DBMS 要求对返回的所有列进行命名
- 视图不能有索引, 也不能有触发器或默认值
- 有些 DBMS 把视图作为只读的查询

## 18.2 创建视图 ##

可以使用 CREATE VIEW 语句创建视图, 使用 DROP VIEW 语句删除视图.

### 18.2.1 利用视图简化复杂的联结 ###

视图语句如下:

```
CREATE VIEW ProductCustomers AS
SELECT cust_name, cust_contact, prod_id
FROM Customers, OrderItems, Orders
WHERE Customers.cust_id = Orders.cust_id
    AND OrderItems.order_num = Orders.order_num;
```

可以如下使用:

```
SELECT cust_name, cust_contact
FROM ProductCustomers
WHERE prod_id = 'RGAN01';
```

### 18.2.2 用视图重新格式化检索出的数据 ###

可以创建如下的视图来组合数据:

```
CREATE VIEW VendorLocations AS
SELECT RTRIM(vend_name) || '(' RTRIM(vend_country) || ')'
AS vend_title
FROM Vendors;
```

### 18.2.3 用视图过滤不想要的数据 ###

可以创建如下的视图来过滤没有电子邮件地址的用户:

```
CREATE VIEW CustomerEMailList AS
SELECT cust_id, cust_name, cust_email
FROM Customers
WHERE cust_email IS NOT NULL;
```

### 18.2.4 使用视图与计算字段 ###

```
CREATE VIEW OrderItemsExpanded AS
SELECT order_num,
    prod_id,
    quantity,
    item_price,
    quantity*item_price AS expanded_price
FROM OrderItems;
```

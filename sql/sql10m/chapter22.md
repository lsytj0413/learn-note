# 第22章: 高级SQL特性 #

## 22.1 约束 ##

### 22.1.1 主键 ###

主键是一种特殊的约束, 用来保证一列中的值是唯一的, 而且也不应该改动.

```
CREATE TABLE Vendors
(
    vend_id CHAR(10) NOT NULL PRIMARY KEY,
    vend_name CHAR(50) NOT NULL,
    vend_address CHAR(50) NULL,
    vend_city CHAR(50) NULL,
    vend_state CHAR(5) NULL,
    vend_zip CHAR(10) NULL,
    vend_country CHAR(50) NULL
);
```

### 22.1.2 外键 ###

外键是表中的一列, 其值必须列在另一表的主键中, 可以保证引用完整性.

```
CREATE TABLE Orders
(
    order_num INTEGER NOT NULL PRIMARY KEY,
    order_date DATETIME NOT NULL,
    cust_id CHAR(10) NOT NULL REFERENCES Customers(cust_id)
);
```

### 22.1.3 唯一约束 ###

唯一约束用来保证一列中的数据是唯一的, 它与主键的区别是:

- 表可包含多个唯一约束, 但每个表只允许一个主键
- 唯一约束列可以包含 NULL
- 唯一约束列可修改和更新
- 唯一约束列的值可重复使用
- 唯一约束列不能用来定义外键

### 22.1.4 检查约束 ###

检查约束常见的用途有以下几点:

- 检查最小或最大值
- 指定范围
- 只允许特定的值

```
CREATE TABLE OrderItems
(
    order_num INTEGER NOT NULL,
    order_item INTEGER NOT NULL,
    prod_id CHAR(10) NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    item_price MONEY NOT NULL
);
```

## 22.2 索引 ##

索引用来排序数据以加快搜索和排序操作的速度.

```
CREATE INDEX prod_name_ind
ON PRODUCTS (prod_name);
```

## 22.3 触发器 ##

触发器是特殊的存储过程, 在特定的数据库活动发生时自动执行.

## 22.4 数据库安全 ##

安全性使用 SQL 的 GRANT 和 REVOKE 语句来管理.

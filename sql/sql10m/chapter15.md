# 第15章: 插入数据 #

## 15.1 数据插入 ##

可以使用 INSERT 来插入数据到表中, 有以下几种方式:

- 插入完整的行
- 插入行的一部分
- 插入某些查询的结果

### 15.1.1 插入完整的行 ###

例如:

```
INSERT INTO Customers
VALUES('1000000006',
    'Toy Land',
    '123 Any Street',
    'New York',
    'NY',
    '11111',
    'USA',
    NULL,
    NULL);
```

上述的语法是可用的, 但是依赖于表中列的定义次序. 更好的方法如下:

```
INSERT INTO Customers(cust_id,
    cust_name,
    cust_address,
    cust_city,
    cust_state,
    cust_zip,
    cust_country,
    cust_contact,
    cust_email)
VALUES('1000000006',
    'Toy Land',
    '123 Any Street',
    'New York',
    'NY',
    '11111',
    'USA',
    NULL,
    NULL);
```

- 不要使用没有明确g诶出列的 INSERT 语句
- VALUES 的数目必须正确

### 15.1.2 插入部分行 ###

INSERT 语句中可以省略列:

```
INSERT INTO Customers(cust_id,
    cust_name,
    cust_address,
    cust_city,
    cust_state,
    cust_zip,
    cust_country)
VALUES('1000000006',
    'Toy Land',
    '123 Any Street',
    'New York',
    'NY',
    '11111',
    'USA');
```

省略的列必须满足以下某个条件:

- 该列定义为允许 NULL 值
- 在表定义中给出默认值, 此时将使用默认值

### 15.1.3 插入检索出的数据 ###

INSERT 可以将 SELECT 语句的结果插入表中, 即 INSERT SELECT.

```
INSERT INTO Customers(cust_id,
    cust_name,
    cust_address,
    cust_city,
    cust_state,
    cust_zip,
    cust_country)
SELECT cust_id,
    cust_name,
    cust_address,
    cust_city,
    cust_state,
    cust_zip,
    cust_country
FROM CustNew;
```

SELECT 语句中可以包含 WHERE 子句.

## 15.2 从一个表复制到另一个表 ##

如果需要将一个表的数据复制到另一个全新的表, 可以使用 SELECT INTO 语句.

```
SELECT *
INTO CustCopy
FROM Customers;
```

- 新表是运行时创建
- 有的 DBMS 会覆盖已存在的表

有些 DBMS(例如 MySQL) 使用如下语法:

```
CREATE TABLE CustCopy AS
SELECT * FROM Customers;
```

- 任何 SELECT 选项和子句都可以使用
- 可利用联结从多个表插入数据
- 数据只能插入到一个表

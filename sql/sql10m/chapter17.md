# 第17章: 创建和操纵表 #

## 17.1 创建表 ##

可以使用 CREATE TABLE 语句创建表.

### 17.1.1 表创建基础 ###

使用 CREATE TABLE 创建表必须给出以下信息:

- 新表的名字
- 表列的定义和名字
- 有的 DBMS 需要指定表的位置

```
CREATE TABLE Products
(
    prod_id CHAR(10) NOT NULL,
    vend_id CHAR(10) NOT NULL,
    prod_name CHAR(254) NOT NULL,
    prod_price DECIMAL(8, 2) NOT NULL,
    prod_desc VARCHAR(1000) NULL
);
```

### 17.1.2 使用 NULL 值 ###

- 在不指定 NOT NULL 时, 多数 DBMS 认为指定的是 NULL
- 允许 NULL 值的列不能作为主键
- NULL 是指没有值, 而不是空字符串或0

### 17.1.3 指定默认值 ###

可以使用 DEFAULT 关键字指定默认值.

```
CREATE TABLE OrderItems
(
    order_num INTEGER NOT NULL,
    order_item INTEGER NOT NULL,
    prod_id CHAR(10) NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    item_price DECIMAL(8, 2) NOT NULL
);
```

## 17.2 更新表 ##

可以使用 ALTER TABLE 语句更新表, 所有的 DBMS 都支持 ALTER TABLE, 但是它们允许的更新内容差别较大. 使用 ALTER TABLE 时需要注意如下的事项:

- 一般不要在表中包含数据时更新
- 允许增加列, 但是对该列的数据类型, NULL 和 DEFAULT 有所限制
- 有些 DBMS 不允许删除或更改列
- 多数 DBMS 支持重命名列
- 有些 DBMS 限制对已经有数据的列进行更改

增加列的示例如下:

```
ALTER TABLE Vendors
ADD vend_phone CHAR(20);
```

## 17.3 删除表 ##

使用 DROP TABLE 语句即可删除表:

```
DROP TABLE CustCopy;
```

## 17.4 重命名表 ##

MySQL 可以使用 RENAME 语句重命名表.

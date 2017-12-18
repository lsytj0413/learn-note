# 第2章: 检索数据 #

## 2.1 SELECT语句 ##

如果要使用 SELECT 检索表数据, 需要至少给出两个信息: 需要检索什么, 以及从什么地方选择.

## 2.2 检索单个列 ##

例如从 Products 表中检索 prod_name 列:

```
SELECT prod_name FROM Products;
```

- 在上面的语句中返回的数据是没有特定的顺序的
- 多条 SQL 语句必须使用分号分割
- SQL 语句不区分大小写, 表名, 列名和值可能会区分大小写(依赖与具体的 DBMS 配置)

## 2.3 检索多个列 ##

例如从 Products 表中检索三个列:

```
SELECT prod_id, prod_name, prod_price FROM Products;
```

- 列名使用逗号分割

## 2.4 检索所有列 ##

在实际列名处使用星号通配符即可:

```
SELECT * FROM Products;
```

- 列的顺序一般是列在表定义中出现的物理顺序, 但不总是如此
- 最好不要使用星号通配符
- 使用星号通配符能检索出名字未知的列

## 2.5 检索不同的值 ##

可以使用 DISTINCT 关键字来指示数据库只返回不同的值:

```
SELECT DISTINCT vend_id FROM Products;
```

- DISTINCT 关键字必须直接放在列名之前
- DISTINCT 关键字作用于所有的列

## 2.6 限制结果 ##

如果只需要返回一定数量的行, 在 MySQL, MariaDB, PostgreSQL 或 SQLite 中可以这样使用:

```
SELECT prod_name FROM Products LIMIT 5;
```

上述语句指定返回最多 5 行数据, 如果想返回 6-10 行数据:

```
SELECT prod_name FROM Products LIMIT 5 OFFSET 5;
```

- 第一个被检索的行是第0行
- MySQL 和 MariaDB 支持简化的 LIMIT 3,4 语法, 等同于 LIMIT4 OFFSET 3
- 并非所有的 SQL 实现都相同

## 2.7 使用注释 ##

行内注释的语法如下:

```
SELECT prod_name     -- 这是一条注释
FROM Products;
```

整行注释:

```
# 这是一条注释
SELECT prod_name FROM Products;
```

多行注释:

```
/* SELECT prod_name, vend_id 
FROM Products; */
SELECT prod_name FROM Products;
```

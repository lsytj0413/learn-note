# NoSQL #

## MongoDB ##

### 工具 ###

#### mongoexport ####

可以使用 mongoexport 命令导出 MongoDB 中表的数据.

```
mongoexport -d database -c table -o file --type json -u username -p password
```

#### mongoimport ####

可以使用 mongoimport 命令导入数据到 MongoDB 的表中.

```
mongoimport -d database -c table --file file --type json -u username -p password
```

#### mongo ####

可以使用 mongo 命令连接 MongoDB.

```
mongo -u username -p password
```

### 语法 ###

在 MongoDB 中的集合对应 SQL 中的表的概念.

#### 创建数据库 ####

```
use DATABASE_NAME
```

#### 显示所有数据库 ####

```
show dbs
```

#### 删除数据库 ####

```
db.dropDatabase()
```

#### 显示所有表 ####

```
show collections;
```

#### 更新文档 ####

```
# 使用 update 来更新文档
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)

# 使用 save 来替换文档
db.collection.save(
   <document>,
   {
     writeConcern: <document>
   }
)
```

例如向表中增加字段:

```
 db.table.update({"detail.id": "123456"}, {$set: {"detail.data2": "update-data2", "detail.data3": "update-data3"}}, {multi: true})
```

#### 查找存在某个字段的文档 ####

```
db.table.count({"detail.nameCn": {$exists: true}})
```

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
mongo HOST:PORT/DB -u username -p password
```

#### mongodump ####

可以使用 mongodump 备份数据库:

```
mongodump -h HOST -d DB -u USERNAME -p PASSWORD -o DEST
```

#### mongorestore ####

可以使用 mongorestore 恢复备份的数据库:

```
mongorestore -h HOST -u USERNAME -p PASSWORD --authenticationDatabase DB DEST
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

#### 容量统计 ####

```
# 统计数据库容量
db.stats()         # 以字节为单位
db.stats(1024)     # 以 1024字节为单位

# 统计表容量
db.table.stats()
db.table.stats(1024)
```

#### Log Rotate ####

```
# 使用以下命令启动 mongod
mongod -v --logpath /var/log/mongodb/server1.log
# 或者
mongod -v --logpath /var/log/mongodb/server1.log --logRotate reopen --logappend

# 然后在 mongo client 中执行以下命令:
db.adminCommand( { logRotate : 1 } )
```

#### 创建用户 ####

```
use xxx;
db.createUser({user: 'username', pwd: 'password', roles: [{role: 'dbOwner', db: 'xxx'}]})

# 查看用户
use admin;
db.system.users.find()
```

#### 记录慢日志 ####

```
db.setProfilingLevel(1);
```

#### mongostat ####

使用 mongostat 命令来监控 mongodb 的运行状况, 首先需要创建一个角色:

```
use admin;
db.createRole(
   {
     role: "mongostatRole",
     privileges: [
       { resource: { cluster: true }, actions: [ "serverStatus" ] }
     ],
     roles: []
   }
)
```

然后将角色赋予用户:

```
db.grantRolesToUser("username",
[
    {
        role: "mongostatRole",
        db: "admin"
    }
])
```

最后使用以下命令即可:

```
mongostat -u username -p pwd --authenticationDatabase admin
```

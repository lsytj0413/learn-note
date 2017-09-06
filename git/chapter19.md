# 第十九章: 高级操作 #

## 使用 git filter-branch ##

git filter-branch 是一个通用的分支操作命令, 可以通过自定义命令来利用它操作不同的 git 对象, 从而重写分支上的提交. 一些过滤器可以对提交起作用, 一些对树对象和目录结构起作用, 还有一些则可以操作 git 环境.

filter-branch 命令会在版本库中的一个或多个分支上运行一系列过滤器, 每个过滤器可以搭配一条自定义的过滤器命令, 这些过滤器按照顺序执行(可以不必全部执行), 于是前面的过滤器可以影响后面的过滤器的行为.

在 git 1.7.9 版本中, git filter-branch 是一个 shell 脚本, 除了 commit-filter 之外的每个 command 都利用 eval 在 shell 上下文中执行. 每个过滤器的说明如下:

- env-filter command: 用来创建或改变 shell 环境变量
- tree-filter command: 允许修改一个目录中将要被树对象所记录的内容, .gitignore 文件对该指令不起作用
- index-filter command: 在提交之前变更索引的内容
- parent-filter command: 允许重建每个提交的父子关系
- msg-filter command: 在真正创建一个提交之前执行, 允许编辑提交信息
- commit-filter command: 执行提交操作步骤的控制权, 接受一个新的 tree object 和一系列 -p parent-obj 参数, 提交消息通过 stdin 传入
- tag-name-filter command: 重写已经存在的标签
- subdirectory-filter command: 将历史记录改写行为限制在影响特定目录的几个提交中

git filter-branch 完成后, 原先包含整个旧的提交历史记录的引用将会以 refs/original 新引用存在, 在执行该操作前需要保证该目录为空, 执行之后可以将该目录删除.

### 使用 git filter-branch 的例子 ###

一个比较常见的使用场景是: 你创建了一个充满了提交历史记录的版本库, 想清理它或做大规模的修改, 从而使得别人能够克隆和使用它.

**使用 git filter-branch 删除文件**

Git 维护版本库中每个文件的完整历史记录, 因此简单的使用 git rm 删除文件是达不到彻底删除文件的效果的. 使用 git filter-branch 就可以从版本库的任何或者每个提交中删除文件, 使得这个文件看起来就是从来没有在版本库中出现过一样.

首先创建一个版本库, 其中包含一些读书笔记, 这时我们要删除 1984 文件的一切记录. 我们可以使用 tree-filter 和 index-filter 来达到效果, 使用 tree-filter 的命令如下:

```
$ git filter-branch --tree-filter 'rm 1984' master
```

使用上述命令之后, 我们发现命令执行的过程失败了. 这是因为 Git 会对 master 分支的每个提交建立该提交的上下文, 并且执行 rm 命令, 但是文件 1984 是在第三个提交引入的, 所以对第一个提交执行 rm 命令会失败. 修改之后的命令如下:

```
# 使用 -f 选项来强制删除并且忽略不存在的文件
$ git filter-branch --tree-filter 'rm -f 1984' master
```

Git 会输出当前重写的所有提交, 但是只有最后一个显示在屏幕上. 可以通过管道命令将 Git 的输出重定向到 less, 即可以看到所有重写的提交.

使用 index-filter 的命令如下:

```
$ git filter-branch --index-filter 'git rm --cached --ignore-unmatch 1984' master
```

因为 1984 这个文件是从第三个提交引入的, 所有 Git 会给从第三个提交开始的所有提交生成新的 SHA1 值, 在重写和过滤的过程中, Git 创建并维护新老提交的对应关系表, 并提供 map 函数来获取它.

**使用 git filter-branch 编辑提交信息**

在之前的示例中, 我们删除了 1984 文件, 但是一些提交信息中仍然提到了 1984. 例如:

![图 包含1984的提交信息](./images/image19-01.png)

我们可以使用 --msg-filter 过滤器来重写提交信息, 该过滤器命令从 stdin 接受老的提交信息并将修改后的文本你写入 stdout. 使用的命令如下:

```
$ git filter-branch --msg-filter '
sed -e "/1984/d" -e "s/few classics/classic/"' master
```

### filter-branch 的诱惑 ###

git filter-branch 也可以作用于多个分支和引用, 假设需要将操作作用于所有分支:

```
# 使用 --all 作用于所有分支
$ git filter-branch --index-filter \
"git rm --cached -f --ignore-unmatch '*.jpeg'" \
-- --all
```

如果你需要同时将所有标签从过滤前的旧提交指向新提交:

```
$ git filter-branch --index-filter \
"git rm --cached -f --ignore-unmatch '*.jpeg'" \
--tag-name-filter cat \
-- --all
```

可以使用如下的命令找到修改过名字的文件:

```
$ git log --name-only --follow --all - file
```

## 我如何学会喜欢上 git rev-list ##

### 基于日期的检出 ###

可以利用类似 git checkout master@{Jan 1, 2011} 的命令可以实现基于日期的检出, 该命令使用 reflog 来找到 master 分支上基于日期的引用. 但是这种方式有几个问题可能导致这种方式失效:

1. 版本库没有启用 reflog, 或者 reflog 过期
2. 它要求依据 reflog 依据你对 master 分支的操作记录来查找在给定时刻分支指向哪个提交, 而不是根据该分支上的提交时间线来查找. 这两者可能是没有关系的.
3. 可能造成死锁

所以应该使用 git rev-list 命令, 它提供了丰富的选项组合, 帮助用户对有很多分支的复杂历史记录排序, 挖掘潜在模糊的用户特征, 限制搜索空间, 最后在提交历史记录中定位特定的提交.

例如找出 master 分支上 2011 年的最后一个提交:

```
$ git clone git://github.com/gitster/git.git
$ cd git
$ git rev-list -n 1 --before="Jan 1, 2012 00:00:00" master
```

git rev-list 命令参考的是 CommitDate(提交日期) 字段, 而不是 AuthorDate(创作日期) 字段.

**基于日期的检出的注意事项**

Git 处理日期的部分是通过一个叫 approxidate() 函数实现的, Git 在解析你作为参数传入的日期时是近似的.

```
# 精确的时间
$ git rev-list -n 1 --before="Jan 1, 2012 00:00:00" master

# 假定为当前时间
$ git rev-list -n 1 --before="Jan 1, 2012" master
```

尽管你在按特定时间查询提交时, 可以得到一个有效的结果, 但是可能过几天再以同样的查询条件查询时会得到不同的结果(可能从其他分支合并了更符合条件的提交).

### 获取文件的旧版本 ###

可以保持当前工作目录的状态, 而只是将其中某个文件恢复到某个历史版本. 可以借助 rev-list 技术来找出包含所要文件的提交, 在查找时 Git 允许将搜索限定到特定的文件或一系列文件(称为路径限制 path limiting). 

```
$ git rev-list master --date.c
```

在找到提交之后有三种方法可以用来得到文件的那个版本:

1. 直接检出那个提交的文件并覆盖工作目录中的当前文件

```
$ git checkout ecee9d9 date.c
# 如果不知道提交ID但是知道提交日志包含的一些内容
$ git checkout :/"FIx PR-1705" main.c
```

2. 通过 show 命令写入文件

```
$ git show ecee9d9:date.c > date.c-oldest
```

3. 通过 cat-file 命令写入文件

```
$ git cat-file -p 89967:date.c > date.c-first-change
```

第二种和第三种方式有细微的差别, 第二种方式会利用任何可用的文本转换方法对输出内容进行过滤, 第三种不会进行过滤.

## 数据块的交互式暂存 ##

## 恢复遗失的提交 ##

### git fsck 命令 ###

### 重新连接遗失的提交 ###

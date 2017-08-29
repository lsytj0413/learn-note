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

### 获取文件的旧版本 ###

## 数据块的交互式暂存 ##

## 恢复遗失的提交 ##

### git fsck 命令 ###

### 重新连接遗失的提交 ###

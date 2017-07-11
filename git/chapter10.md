# 第十章: 更改提交 #

## 关于修改历史记录的注意事项 ##

作为一般原则, 如果一个分支已经公开, 并且可能存在于其他版本库中, 那就不应该重写, 修改或更改该分支的任何部分.

## 使用 git reset ##

git reset 调整 HEAD 引用指向给定的提交, 默认情况下还会更新索引以匹配该提交. git reset 命令也可以修改工作目录以呈现给定提交代表的项目修订版本.

git reset 命令的主要选项如下表:

| 选项 | 作用 |
|:--|:--|
| --soft | 将HEAD引用指向给定提交, 索引和工作目录保持不变. |
| --mixed | 将HEAD指向给定提交, 索引内容也修改为符合给定提交的树结构, 默认模式 |
| --hard | 将HEAD指向给定提交, 索引和工作目录也修改为符合给定提交的内容 |

git reset 命令把原始 HEAD 值保存在 ORIG_HEAD 中. 下面是一个意外暂存了 foo.c 文件, 需要恢复的例子:

```
# 意外暂存文件 foo.c
$ git add foo.c

# 显示暂存列表
$ git ls-files
foo.c
main.c

# 删除暂存的 foo.c
$ git reset HEAD foo.c

$ git ls-files
main.c
```

git reset 的另一个常见的用法是简单的重做或清除分支上的最近提交. 下面建立一个有两个分支的仓库作为例子:

```
# 初始化仓库, 并在 master 分支上建立两个提交
$ git init
$ echo foo >> master_file
$ git add master_file
$ git commit -m "Add master_file to master branch"
$ echo "more foo" >> master_file
$ git commit -m "Add more foo"
$ git show branch --more=5
```

然后撤销第二个提交, 但是保存工作目录文件内容:

```
$ git reset HEAD^
$ cat master_file
foo
more foo
```

然后修改文件并重新索引, 提交:

```
$ echo "even more foo" >> master_file
$ git commit -m "Updated foo" master_file
```

然后调整提交信息:

```
$ git reset --soft HEAD^
$ git commit -m ""
```

--soft 选项只是将 HEAD 调整位置, 但保持索引和工作目录不变, 这样就有机会通过重新提交来修改提交信息.

假设要完全取消第二次提交, 可以使用如下命令:

```
$ git reset --hard HEAD^
$ cat master_file
foo
```

为了演示对其他分支使用 git reset, 现在添加一个新分支 dev:

```
$ git checkout master
$ git checkout -b dev
$ echo bar >> dev_file
$ git add dev_file
$ git commit -m "Add dev_file o dev branch"
```

然后在 master 分支上使用 git reset 命令:

```
$ git checkout master
$ git reset --soft dev
```

此时会有一个非常特殊的状态, 即 HEAD 指向的提交有个 dev_file 文件, 但是这个文件不在 master 分支上, 然后在 master 分支上构建一个提交:

![图 在 master 分支上构建提交](./images/image10-01.png)

Git 正确的添加了新文件 new, 但是却显示删除了文件 dev_file. 这是因为该文件确实不存在于 master 分支, 因为它从来没有存在过. 为什么 Git 选择删除这个文件呢? 这是因为执行提交时 HEAD 的指向中有这个文件:

![图 提交的 HEAD](./images/image10-02.png)

可以看出, 最后一次提交是错误的, 应该删除. 但是此时不能使用 git reset --hard HEAD^, 但是这时 HEAD^ 是指向的 dev 分支的HEAD, 而不是 master 分支的 HEAD, 所以也是不正确的状态.
有几个办法可以确认 master 分支应该重置到哪个提交, 例如使用 git log 命令:

![图 git log 确认提交](./images/image10-03.png)

或者使用 reglog 来查看版本库中引用变化的历史记录:

![图 git reflog 确认提交](./images/image10-04.png)

通过以上方式可以确认, e719b1f 或者 HEAD@{2} 是可以恢复到正确状态的提交:

```
$ git rev-parse HEAD@{2}
$ git reset --hard HEAD@{2}
$ git show-branch
```

## 使用 git cherry-pick ##

## 使用 git revert ##

## reset, revert 和 checkout ##

## 修改最新提交 ##

## 变基提交 ##

### 使用 git rebase -i ###

### 变基和合并 ###

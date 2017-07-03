# 第九章: 合并 #

## 合并的例子 ##

可以使用如下的命令把 other_branch 分支合并到 branch 中:

```
$ git checkout branch
$ git merge other_branch branch
```

### 为合并做准备 ###

在正常合并结束的时候, Git 会创建新版本的文件并把它们放到工作目录中, 而且 Git 会使用索引来存储文件的中间版本.
如果已经修改了工作目录中的文件, 或者通过 git add 或 git rm 等修改了索引, 那么版本库中就是一个脏的工作目录或索引, 在这种状态下进行合并 Git 可能无法一次合并所有分支及工作目录或索引的修改.
所以从干净的工作目录和索引进行合并, 会使 Git 的合并更容易.

### 合并两个冲突 ###

下面以一个拥有两个分支的版本库为示例:

首先创建版本库, 并在 master 分支上添加两个提交:

```
$ git init
$ cat > file
Line 1 stuff
Line 2 stuff
Line 3 stuff
^D
$ git add file
$ git commit -m "Initial 3 line file"

# 添加第二个提交
$ cat > other_file
Here is stuff on another file!
^D
$ git add other_file
$ git commit -m "Another file"
```

创建新分支 alternate, 从 master^ 提交派生, 并修改 file 文件:

```
$ git checkout -b alternate master^
$ cat >> file
Line 4 alternate stuff
^D
$ git commit -a -m "Add alternate's line 4"
```

现在使用 git merge 命令进行合并, 在 git merge 命令中, 当前分支始终是目标分支, 会将一个或多个其他分支合并到当前分支.
使用以下命令将 alternate 分支合并到 master 分支:

```
$ git checkout master
$ git merge alternate
```

查看到 git log 的输出如下图:

![图 git log --graph](./images/image09-01.png)

从上图中可以看到, 两个分支在初始提交 8f4d2d5 处分开; 每个分支有一个提交; 两个分支在提交 1d51b93 处合并.

### 有冲突的合并 ###

以之前的实例为基础, 构造一个包含冲突的合并. 首先, 在 master 分支上修改文件并提交:

```
$ git checkout master
$ cat >> file
Line 5 stuff
Line 6 stuff
^D
$ git commit -a -m "Add line 5 and 6"
```

在 alternate 分支上修改同一个文件:

```
$ git checkout alternate
$ git show-branch
$ cat >> file
Line 5 alternate stuff
Line 6 alternate stuff
^D
$ git commit -a -m "Add alternate line 5 and 6"
```

尝试执行合并操作, 并得到一个冲突的提示:

```
$ git checkout master
$ git merge alternate
```

使用 git diff 查看文件在工作目录和索引之间的差异:

![图 git diff file](./images/image09-02.png)

从图上可以看到, 改变的内容显示在 <<<<<<<< 和 ======== 之间, 替代的内容在 ======== 和 >>>>>>>> 之间. 使用文本编辑器修改文件内容如下:

```
$ cat file
Line 1 stuff
Line 2 stuff
Line 3 stuff
Line 4 alternate stuff
Line 5 stuff
Line 6 alternate stuff
```

这时冲突已经解决, 提交文件:

```
$ git add file
$ git commit
```

此处使用 git commit 命令来进行提交, Git 会准备一条模板消息.

## 处理合并冲突 ##

### 定位冲突的文件 ###

### 检查冲突 ###

### Git 是如何追踪冲突的 ###

### 结束解决冲突 ###

### 中止或重新启动合并 ###

## 合并策略 ##

### 退化合并 ###

### 常规合并 ###

### 特殊提交 ###

### 应用合并策略 ###

### 合并驱动程序 ###

## Git 怎么看待合并 ##

### 合并和 Git 的对象模型 ###

### 压制合并 ###

### 为什么不一个接一个地合并每个变更 ###


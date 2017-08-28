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

### filter-branch 的诱惑 ###

## 我如何学会喜欢上 git rev-list ##

### 基于日期的检出 ###

### 获取文件的旧版本 ###

## 数据块的交互式暂存 ##

## 恢复遗失的提交 ##

### git fsck 命令 ###

### 重新连接遗失的提交 ###

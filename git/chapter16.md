# 第十六章: 合并项目 #

子模块不但构成了你自己的 Git 版本库的一部分, 而且它也独立的存在于它自己的源代码版本库中.

## 旧解决方案: 部分检出 ##

传统的版本控制系统有一种流行的功能, 部分检出. 通过部分检出可以选择只检出特定的子目录, 并只在其中工作. 但当前的 Git 架构不支持部分检出技术.

## 显而易见的解决方案: 将代码导入版本库 ##

通过直接导入的方式来使用子模块, 有两种方法: 一是手动复制文件, 二是导入历史记录.

### 手动复制导入子项目 ###

直接把需要的文件复制进来即可.

### 通过 git pull -s subtree 导入子项目 ###

也可以直接合并该子项目的所有历史记录. 首先创建一个项目仓库 myapp, 然后导入 git 项目:

```
$ cd /tmp
$ mkdir myapp
$ cd myapp
$ git init
$ echo hello > hello.txt
$ git add hello.txt
$ git commit -m "first commit"

# 导入 git
$ mkdir git && cd git
$ (cd ~/git.git && git archive v1.6.0) | tar -xf -
$ cd ..
$ git add git
$ git commit -m "imported git v1.6.0"
```

然后使用 git pull -s ours 策略来通知 Git 你已经在 myapp 项目中导入了 git 项目:

```
# 简单的指定 v1.6.0 是不正确的, 需要完整的名称
$ git pull -s ours ~/git.git refs/tagsv1.6.0
```

现在可以在 git 目录中进行一个提交:

```
$ cd git
$ echo "i am a git" > c.txt
$ git add c.txt
$ git commit -m "my first c.txt to git"
```

现在 Git 子项目版本为 v1.6.0, 而且拥有一个额外的补丁. 然后再尝试将 git 更新至 v1.6.0.1:

```
$ git pull -s subtree ~/git.git refs/tags/v1.6.0.1
```

现在检查文件是否已经正确更新, 因为在 1.6.0.1 中所有的文件都被移动到了 git 目录中, 需要在 git diff 中采用选择器语法:

```
$ git diff HEAD^2 HEAD:git
```

可以看到, 与 v1.6.0.1 的唯一区别就是我们的那个补丁提交.

### 将更改提交到上游 ###

可以通过使用 -s subtree 合并策略将你的项目历史记录合并回 git.git 中, 但这回将你项目的完整历史导入, 然后在合并时删除除 git 目录以外的所有文件.

## 自动化解决方案: 使用自定义脚本检出子项目 ##

## 原生解决方案: gitlink 和 git submodule ##

### gitlink ###

### git submodule 命令 ###

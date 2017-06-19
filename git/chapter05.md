# 第五章: 文件管理和索引 #

当使用 Git 时, 你会在工作目录下编辑, 在索引中积累修改, 然后把索引中积累的修改作为一次性的变更来进行提交.

## 关于索引的一切 ##

Git 的索引不包含任何文件内容, 仅仅是追踪你想要提交的那么内容. 当执行 git commit 命令的时候, Git 会通过检查索引而不是工作目录来找到提交的内容.

在任何时候都可以通过 git status 命令来查询索引的状态, 它会明确展示哪些文件在 Git 看来是暂存的.

可以使用 git diff 命令显示两组不同的差异: git diff 显示仍留在工作目录中且未暂存的变更; git diff --cached 显示已经暂存并且因此要有助于下次提交的变更.

## Git 中的文件分类 ##

Git 将所有文件分为以下 3 类:

- 已追踪的: 指已经在版本库中的文件, 或者是已暂存到索引中的文件
- 被忽略的: 在版本库中明确声明为不可见或被忽略的文件
- 未追踪的: 不在前两类中的文件

```
# 建立新版本库
$ cd /tmp/my_stuff
$ git status

# 添加文件
$ echo "New data" > data
# 显示一个未追踪文件
$ git status

# 忽略文件
$ touch main.o
$ git status
$ echo main.o > .gitignore
# 忽略 main.o, .gitignore显示为未追踪
$ git status
```

## 使用 git add ##

git add 命令将暂存一个文件, 如果一个文件是未追踪的, 那么该命令就会将文件的状态转化为已追踪的; 如果是一个目录, 那么该目录下的文件和子目录都会递归暂存.

```
git status
git add data .gitignore

# 查看暂存文件的 SHA1
git ls-files --stage

# 修改 data 文件并查看新版的 SHA1
echo "And some more data now" >> data
git hash-object data
# 暂存新版本
git add data
git ls-files --stage
```

在发出 git add 命令时每个文件的全部内容都将被复制到对象库中, 并且按照文件的 SHA1 名来索引. 相对于添加这个文件, git add 命令更合适看作添加这个内容.

需要注意的是, 工作目录中的文件版本和索引中暂存的文件版本可能是不同步的, 当提交的时候, Git 会使用索引中的版本.

## 使用 git commit 的一些注意事项 ##

### 使用 git commit --all ###

git commit 的 -a 或者 --all 选项会导致执行提交前自动暂存所有未暂存的和未追踪的文件变化, 包括从工作副本中删除的已追踪的文件. 但是对于一个全新的目录, 而且该目录下没有任何文件名或路径是已追踪的, 那么该选项也不会将其提交.

```
mkdir /tmp/commit-all-example
cd /tmp/commit-all-example
git init

# commit
echo something >> ready
echo something else >> notyet
git add ready notyet
git commit -m "Setup"

echo modify >> ready
git add ready
echo modify >> notyet
mkdir subdir
echo Nope >> subdir/new

git status

# 提交 ready 和 notyet
git commit -all -m "commit"
```

### 编辑提交日志 ###

如果你是在编辑器中编写提交日志, 并决定中止操作, 只需要不保存退出即可; 也可以删除已经编辑的日志消息, 重新保存即可. Git 不会处理空提交.

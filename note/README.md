# note #

## 单词 ##

[单词](./word.md) 记录了一些比较有趣与常用的单词.

## script ##

[script](./script.md) 记录了一些 shell 使用过程中的笔记.

## sudo ##

在执行 sudo 时可能会出现 **Command Not Found** 的错误(这是因为在 Ubuntu 上执行 sudo 命令时会重置 PATH), 这时在 ~/.bashrc 中加入以下内容即可:

```
alias sudo="sudo env PATH=$PATH"
```

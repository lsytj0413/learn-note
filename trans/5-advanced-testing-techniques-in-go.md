# Go语言中的5个高级测试技巧 #

Go 有一个强大的内置测试库. 如果你使用过 Go 语言, 那你应该已经知道了这一点. 在这篇文章中, 我们将讨论一些有效的技巧来帮助你在 Go 语言中进行更好的测试, 这些技巧是我们从我们的大型 Go 代码库中获得的经验, 这些技巧可以节省维护代码的时间和精力.

## 使用测试套件 ##

如果你只能从这篇文章中学到一件事, 那么就应该是: 使用测试套件. 对于那些不熟悉这种模式的人来说, 测试套件就是针对一个通用的接口开发一个测试过程, 这个测试过程可以用来对这个接口的多个实现进行测试. 下面的代码演示了如果针对不同 Thinger 的实现使用相同的测试:

```
type Thinger interface {
    DoThing(input string) (Result, error)
}

// Suite tests all the functionality that Thingers should implement
func Suite(t *testing.T, impl Thinger) {
    res, _ := impl.DoThing("thing")
    if res != expected {
        t.Fail("unexpected result")
    }
}

// TestOne tests the first implementation of Thinger
func TestOne(t *testing.T) {
    one := one.NewOne()
    Suite(t, one)
}

// TestOne tests another implementation of Thinger
func TestTwo(t *testing.T) {
    two := two.NewTwo()
    Suite(t, two)
}
```

有些读者也许已经在代码中使用了这种测试技术. 这种技巧在基于插件的系统中广泛使用, 通常是针对接口编写适用于该接口的所有实现的测试, 以确定实现是否满足行为要求.

使用这种技巧可以节省数小时, 数天甚至更多的时间. 而且, 这可以在交换两个底层系统时避免编写(很多)额外的测试, 也可以确保不会破坏应用程序的正确性. 这隐含的要求你提供一个方式来指定需要测试的实现, 使用依赖注入你可以将需要测试的实现传递给测试套件.

[这里](https://github.com/segmentio/testdemo) 提供了一个完整的例子. 虽然这个例子是故意设计的, 但是你可以想象其中的一个实现是远程数据库, 另一个实现是内存数据库.

在标准库中有一个很好的例子是 golang.org/x/net/nettest 包, 它提供了一个满足 net.Conn 的接口来进行测试验证.

## 空接口污染 ##

在 Go 语言中没有接口就没有测试.

接口在测试环境中非常重要, 因为它们是我们测试库中最强大的工具, 所以正确的使用接口是非常重要的. 包中经常导出接口提供给使用者使用, 这一般会出现两种情况: 使用者提供他们自己的实现或者该包提供自己的实现.

> The bigger the interface, the weaker the abstraction.
> -- Rob Pike, Go Proverbs

在导出之前, 应该仔细的考虑接口的定义. 开发者经常导出接口让使用者来实现他自己的行为. 相反的, 应该在文档中描述你的结构满足哪些接口, 这样你就不会在使用者和你自己的包之间创建一个强的依赖关系. errors 包就是一个很好的例子.

当我们的程序中有一个我们不想导出的接口时, 可以使用一个[内部包/子树](https://golang.org/doc/go1.4#internalpackages)来隐藏它们. 通过这种方式, 可以避免其他使用者依赖于这些接口, 因此可以灵活的改变这些接口来适应新的需求. 我们通常围绕外部依赖创建接口, 并使用依赖注入的方式来运行本地测试.

这允许使用者能够实现自己的小接口, 并且提供给自己测试. 有关这些概念的更多细节, 可以参考 [rakyll 的文章](https://rakyll.org/interface-pollution/).



# 资料 #

- 原文 [5 Advanced Testing Techniques in Go](https://segment.com/blog/5-advanced-testing-techniques-in-go/)

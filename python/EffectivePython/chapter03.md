# 第三章: 类与继承 #

## 第22条: 尽量用辅助类来维护程序的状态, 而不要用字典和元组 ##

### 介绍 ###

假设需要记录许多学生的成绩:

```
class SimpleGradeBook(object):
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = []
    def report_grade(self, name, score):
        self._grades[name].append(score)
    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)
```
由于字典用起来很方便, 所以有可能因为功能过分膨胀而导致代码出问题.
假设需要扩充以上的SimpleGradeBook类使它按照科目来保存成绩:

```
class BySubjectGradeBook(object):
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = {}
    def report_grade(self, name, subject, score):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(score)
    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count
```
可以看到实现上已经稍显复杂, 现在假设需求上还需要记录科目成绩占科目总成绩的权重, 实现方式之一是修改内部的字典, 改用一系列元组作为值, 每个元组都具备 (score, weight) 的形式.

新修改的类用起来已经比较麻烦, 此时我们就应该从字典和元组迁移到类体系.

用来保存程序状态的数据结构一旦变得过于复杂, 就应该将其拆解为类, 以便提供更为明确的接口, 并更好的封装数据. 这样做也能够在接口与具体实现之间创建抽象层.

1. 科目考试成绩的重构

由于分数和权重都不再变化, 而且信息也比较简单, 所以可以使用元组来记录科目的历次考试成绩.

```
grades = []
grades.append((95, 0.45))
```
问题在于普通的元组只是按照位置来排布其中的各项数值. 如果我们要给每次成绩附加老师的评语, 则需要修改原来使用二元组的代码. 元组的长度逐步扩张也意味着代码渐趋复杂. 元组里的数据一旦超过两项, 就应该考虑用其他办法来实现.

collections模块中的namedtuple(具名元组) 类型非常适合这种需求, 很容易就能定义出精简而又不可变的数据类.

```
import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))
```
构建具名元组时, 即可以按照位置访问, 也可以采用关键字指定.

namedtuple也有局限:

- 无法指定各参数的默认值
- 属性依然可以通过下标及迭代访问, 这可能导致其他人以不符合设计者意图的方式使用这些元组

2. 科目类重构

```
class Subject(object):
    def __init__(self):
        self._grades = []
    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))
    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight
```

3. 学生类重构

```
class Student(object):
    def __init__(self):
        self._subjects = {}
    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]
    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count
```

4. 容器类重构

```
class Gradebook(object):
    def __init__(self):
        self._students = {}
    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]
```

### 要点 ###

1. 不要使用包含其他字典的字典, 也不要使用过长的元组
2. 如果容器中包含简单而又不可变的数据, 那么可以先使用 namedtuple 来表示, 待稍后有需要时再修改为完整的类
3. 保存内部状态的字典如果变得比较复杂, 就应该把这些拆解为多个辅助类

## 第23条: 简单的接口应该接受函数, 而不是类的实例 ##

### 介绍 ###

Python有许多内置的API都允许调用者传入函数(Hook)以定制其行为. 例如list类型的sort方法接受可选的key参数, 用以指定每个索引位置间应该如何排序.

```
names = ['Socrates', 'Archimedes', 'POlato']
names.sort(key=lambda x: len(x))
```
用函数作为Hook是比较合适的, 因为它们很容易就能描述这个挂钩的功能, 而且比定义一个类要简单.

例如要定制defaultdict类的行为, 在字典里找不到待查询的键时打印一条信息, 并返回0, 以作为该键所对应的值:

```
def log_missing():
    print('Key added')
    return 0
    
current = {'green': 12}
result = defaultdict(log_missing, current)
```
提供log_missing这样的函数可以使API更容易构建, 也更易测试, 因为它能够把附带的效果与确定的行为分离开.

例如要统计字典中遇到多少个缺失的键:

```
def increment_with_report(current, increments):
    added_count = 0
    
    def missing():
        nonlocal added_count
        added_count += 1
        return 0
        
    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    return result, added_count
```
上面的代码使用了闭包函数来隐藏状态, 这样的缺点就是读起来要比无状态的函数难懂, 也可以定义一个小型的类来封装状态.

### 要点 ###

1. 对于连接各种Python组件的简单接口, 通常应该给其传入函数而不是某个类的实例
2. Python中的函数和方法都可以像一级类那样引用
3. 通过名为 \_\_call\_\_的特殊方法, 可以使类的实例像普通的Pyhton函数那样得到调用
4. 如果要用函数来保存状态, 就应该定义新的类并实现 \_\_call\_\_方法, 而不要定义带状态的闭包

## 第24条: 以 @classmethod形式的多态取通用地构建对象 ##

### 介绍 ###

### 要点 ###

## 第25条: 用super初始化父类 ##

### 介绍 ###

### 要点 ###

## 第26条: 只在使用Mix-in组件制作工具类时进行多重继承 ##

### 介绍 ###

### 要点 ###

## 第27条: 多用public属性, 少用private属性 ##

### 介绍 ###

### 要点 ###

## 第28条: 继承collections.abc 以实现自定义的容器类型 ##

### 介绍 ###

### 要点 ###


# 第四章: 元类及属性 #

## 第29条: 用纯属性取代get和set方法 ##

### 介绍 ###

setter和getter等工具方法, 有助于定义类的接口, 它也使得开发者能够更加方便的封装功能, 验证用法并限定取值范围.
但是对于Python来说, 基本上不需要手工实现setter和getter方法, 应该先从简单的public属性开始使用.

如果想在设置属性的时候实现特殊行为, 可以改用 @property 修改器和setter方法来做.

```
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
    @property
    def voltage(self):
        return self._voltage
    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms
```

我们也可以用 @property 来防止父类的属性遭到修改:

```
class RixedResistance(Resistor):
    @property
    def ohms(self):
        return slef._ohms
    @ohms.setter
    def onms(self, ohms):
        if hasattr(slef, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms
```

@property 属性最大的缺点在于: 和属性相关的方法, 只能在子类里面共享, 而与之无关的其他类无法复用同一份实现代码.

### 要点 ###

1. 编写新类时, 应该用简单的public属性来定义其接口, 而不要手工实现set和get方法
2. 如果访问对象的某个属性时, 需要表现出特殊的行为, 那就用 @property 来定义这种行为
3. @property 方法应该遵循最小惊讶原则, 而不应该产生奇怪的副作用
4. @property方法需要执行得迅速一些, 耗时或复杂的工作应该放在普通的方法里面

## 第30条: 考虑用 @property 来替代属性重构 ##

### 介绍 ###

Python内置的 @property 修饰器, 使调用者能够轻松的访问该类的实例属性. 它也可以把简单的数值属性迁移为实时计算的属性.

假设要用纯Python对象实现带有配额的漏桶(漏桶算法), 把当前剩余的配额以及重置配额的周期放在Bucket类里:

```
class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0
        
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed
        
    @quota.setter
    def quota(slef, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta
```

### 要点 ###

1. @property 可以为现有的实例属性添加新的功能
2. 可以用 @property 来逐步完善数据模型
3. 如果 @property 用的太过频繁, 那就应该考虑彻底重构该类并修改相关的调用代码

## 第31条: 用描述符来改写需要复用的 @property 方法 ##

### 介绍 ###

Python内置的 @property 修饰器有个明显的缺点: 就是不便于复用, 受它修饰的这些方法, 无法为同一个类中的其他属性所复用, 而且与之无关的类也无法复用这些方法.

```
class Homework(object):
    def __init__(self):
        self._grade = 0
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = grade
```

现在假设要把这套验证逻辑放在考试成绩上面, 而考试成绩又是多个科目的小成绩组成, 每一科都要单独计分:

```
class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0
    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
    @property
    def writing_grade(self):
        return self._writing_grade
    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value
    @property
    def math_grade(self):
        return self._math_grade
    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value
```
这种写法不够通用, 需要反复编写 @property 代码和 \_check\_grade方法.

还有一种方式能够更好的实现上述要求, 那就是采用Python的描述符. Python会通过描述符协议来对访问操作进行一定的转义.
描述符类可以提供 \_\_get\_\_ 和 \_\_set\_\_ 方法, 使得开发者无需再编写例行代码, 即可复用分数验证功能.

```
class Grade(object):
    def __get__(*args, **kwargs):
        #
    def __set__(*args, **kwargs):
        #
        
class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    
exam = Exam()
exam.writing_grade = 40
# 转义之后的代码
# Exam.__dict__['writing_grade'].__set__(exam, 40)
```

之所以会有这样的转义, 关键就在于object类的 \_\_getattribute\_\_ 方法. 简单来说, 如果Exam实例没有名为 writing_grade 的属性,
那么Python就会转向Exam类, 并在该类中寻找同名的属性, 而如果这个类属性实现了 \_\_get\_\_ 和 \_\_set\_\_ 方法的对象, 那么Python就会默认对象遵从描述符协议.

我们可以使用以下的 Grade类来实现Homework类的分数验证逻辑:

```
class Grade(object):
    def __init__(self):
        self._value = 0
    def __get__(self, instance, instance_type):
        return self._value
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value
```
不幸的是, 上面这种实现方式是错误的, 它会导致不符合预期的行为. 在多个Exam实例上面分别操作某一属性, 就会导致错误的结果. 因为对于 writing_grade 这个类属性来说, 它只会在程序的生命期中构建一次.

为解决这个问题, 我们需要把每个Exam实例所对应的值记录到 Grade中.

```
class Grade(object):
    def __init__(self):
        self._values = {}
    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)
    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value
```
上面这种方式简单而且正确, 但是它会泄漏内存. 因为 values字典会保存指向 Exam实例的引用, 从而导致该实例的引用计数不能降为0, 垃圾回收器无法将其回收.

使用WeakKeyDictionary的特殊字典来解决此问题, 如果运行期系统发现这种字典所持有的引用是整个程序里面的最后一个引用, 那么系统就会自动将该实例从字典的键中移除.

### 要点 ###

1. 如果想复用 @property 方法及其验证机制, 那么可以自己定义描述符类
2. WeakKeyDictionary 可以保证描述符类不会泄漏内存
3. 通过描述符协议来实现属性的获取和设置操作时, 不要纠结与 \_\_getattribute\_\_ 的方法具体运作细节.

## 第32条: 用 \_\_getattr\_\_, \_\_getattribute\_\_ 和 \_\_setattr\_\_ 实现按需生成的属性 ##

### 介绍 ###

如果某个类定义了 \_\_getattr\_\_ , 同时系统在该类对象的实例字典中又找不到待查询的属性, 那么系统就会调用这个方法.

```
class LazyDB(object):
    def __getattr__(self, name):
        value = 'Value for %s' % (name)
        setattr(self, name, value)
        return value
```

然后给LazyDB添加记录功能, 把程序对 \_\_getattr\_\_ 的调用行为记录下来:

```
class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % (name))
        return super().__getattr__(name)     # 避免递归调用
```

程序每次访问对象的属性时, Pyhton系统都会调用 \_\_getattribute\_\_ 方法, 即使属性字典里已经有了该属性.

```
class ValidatingDB(object):
    def __getattribute__(self, name):
         print('Called __getattribute__(%s)' % (name))
         try:
             return super().__getattribute__(name)
         except AttributeError:
             value = 'Value for %s' % (name)
             setattr(self, name, value)
             return value
```

我们经常会使用 hasattr函数来判断对象是否已经拥有了相关的属性, 并用内置 getattr 函数来获取属性值. 这些函数会先在实例字典中搜索待查询的属性, 然再调用 \_\_getattr\_\_ .

### 要点 ###

## 第33条: 用元类来验证子类 ##

### 介绍 ###

### 要点 ###

## 第34条: 用元类来注册子类 ##

### 介绍 ###

### 要点 ###

## 第35条: 用元类来注解类的属性 ##

### 介绍 ###

### 要点 ###

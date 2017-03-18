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

### 要点 ###

## 第32条: 用 \_\_getattr\_\_, \_\_getattribute\_\_ 和 \_\_setattr\_\_ 实现按需生成的属性 ##

### 介绍 ###

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

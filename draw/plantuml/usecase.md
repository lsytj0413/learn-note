# 用例图 #

## 简单例子 ##

用例是指使用小括号包围起来的文字, 也可以使用 usecase 关键字来定义用例, 使用 as 关键字来定义别名.

将以下内容保存为 [usecase01](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase01.pum):

```
@startuml

(First usecase)
(Another usecase) as (UC2)
usecase UC3
usecase (Last\nusecase) as UC4

@enduml
```

生成的效果图如下:

![usecase01.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase/usecase01.png)

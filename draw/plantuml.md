# plantuml #

## 简介 ##

### 什么是plantuml ###

[plantuml](http://plantuml.com/) 是一个快速创建 UML 图形的组件, 通过简单直观的语言来定义图形, 可以生成PNG, SVG和二进制图片.
plantuml 支持的图形有:

- 序列图 (sequence diagram)
- 用例图 (use case diagram)
- 类图 (class diagram)
- 活动图 (activity diagram)
- 组件图 (component diagram)
- 状态图 (state diagram)
- 对象图 (object diagram)
- 线框图 (wireframe graphical interface)

[User Guide](https://github.com/lsytj0413/learn-note/blob/master/draw/PlantUML_Guide.pdf)

### 一个例子 ###

将以下内容保存为 [plantuml01](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/plantuml01.pum):

```
@startuml
Alice -> Bob: synchronous call
Alice ->> Bob: asynchronous call
@enduml
```

生成的效果图如下:

![plantuml01.png](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/plantuml01.png)

## 序列图 ##

[教程](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/sequence.md)

## 用例图 ##

[教程](https://github.com/lsytj0413/learn-note/blob/master/draw/plantuml/usecase.md)

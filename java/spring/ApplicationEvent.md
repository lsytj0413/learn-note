# Spring事件机制 #

Spring的事件为Bean与Bean之间的消息通信提供了支持.
当一个Bean处理完一个任务之后, 希望另一个Bean知道并能做出相应的处理, 这时就需要让另一个Bean监听当前Bean所发送的事件.
该方法实现了观察者模式, 解除了消息发送者与具体接收者之间的耦合.

Spring的事件需要遵循以下流程:

1. 自定义事件, 继承ApplicationEvent
2. 定义事件监听器, 实现ApplicationListener
3. 使用容器发布事件

## 一个简单的实例 ##

### 自定义事件 ###

首先自定义一个字符串消息事件.

```
package com.tuya;

import org.springframework.context.ApplicationEvent;

public class DemoEvent extends ApplicationEvent{
	private static final long serialVersionUID = 1L;
	private String msg;
	
	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}

	public DemoEvent(Object source, String msg) {
		super(source);
		this.msg = msg;
	}
}
```

### 定义事件监听器 ###

然后定义一个事件监听器, 以便处理事件:

```
package com.tuya;

import org.springframework.context.ApplicationListener;
import org.springframework.stereotype.Component;

@Component
public class DemoListener implements ApplicationListener<DemoEvent> {
	public void onApplicationEvent(DemoEvent event) {
		String msg = event.getMsg();
		
		System.out.println("DemoListener-DemoEvent消息: " + msg);
	}
}
```

### 实现事件发布Bean ###

```
package com.tuya;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Component;

@Component
public class DemoPublisher {
	@Autowired
	ApplicationContext applicationContext;
	
	public void publish(String msg) {
		applicationContext.publishEvent(new DemoEvent(this, msg));
	}
}
```

### 实现配置类 ###

```
package com.tuya;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("com.tuya")
public class ServerConfig {

}
```

### 发布事件 ###

在main函数中发布事件, 观察监听器的输出:

```
package com.tuya;

// import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

@SpringBootApplication
public class HeiPaServerApplication {

	public static void main(String[] args) {
//		SpringApplication.run(HeiPaServerApplication.class, args);
		AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(ServerConfig.class);
		
		DemoPublisher demoPublisher = context.getBean(DemoPublisher.class);
		demoPublisher.publish("hello application event");
		
		context.close();
	}
}
```

### 结果 ###

以上代码正确的输出了监听器中的print, 可见该监听器已经正确的接收到消息并进行了相应的处理.
在代码中我们并不需要知道该消息会被哪些class接收并处理, 实现了消息发送者与接收者之间的解耦.


## 多个消息的处理 ##

在上个例子中, 我们实现了对一个消息使用事件机制的实例, 并能够正常工作.
但是在实际的使用中, 我们经常遇到需要发布多种消息, 以及一个具体的接收者需要能处理多种消息的情况. 接下来的实例演示了这种情况的处理.

### 添加一种消息 ###

```
package com.tuya;

import org.springframework.context.ApplicationEvent;

public class DemoEvent2 extends ApplicationEvent{
	private static final long serialVersionUID = 1L;
	private long id;
	
	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public DemoEvent2(Object source, long id) {
		super(source);
		this.id = id;
	}
}
```

### 修改事件发布Bean ###

在事件发布Bean上添加一个方法:

```
package com.tuya;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Component;

@Component
public class DemoPublisher {
	@Autowired
	ApplicationContext applicationContext;
	
	public void publish(String msg) {
		applicationContext.publishEvent(new DemoEvent(this, msg));
	}
	
	public void publish(int id) {
		applicationContext.publishEvent(new DemoEvent2(this, id));
	}
}
```

### 实现消息接收者 ###

因为在java中不能同时 implements 两次 ApplicationListener接口, 所以需要迂回的处理这个问题, 主要采用以下两种方式:

#### 采用两个内部类接收 ####

这种方式采用两个内部类implements消息接收者, 然后转移给外部类统一处理:

```
package com.tuya;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationListener;
import org.springframework.stereotype.Component;

@Component
public class DemoListener2 {

	void onEvent(DemoEvent event) {
		System.out.println("DemoListener2-DemoEvent消息: " + event.getMsg());
	}
	
	void onEvent(DemoEvent2 event) {
		System.out.println("DemoListener2-DemoEvent2消息: " + event.getId());
	}
	
	@Component
	static class EventListener2 implements ApplicationListener<DemoEvent> {
		@Autowired
		DemoListener2 listener2;
		
		public void onApplicationEvent(DemoEvent event) {
			listener2.onEvent(event);
		}
	}
	
	@Component
	static class Event2Listener2 implements ApplicationListener<DemoEvent2> {
		@Autowired
		DemoListener2 listener2;
		
		public void onApplicationEvent(DemoEvent2 event) {
			listener2.onEvent(event);
		}
	}
}
```

#### EventListener注解 ####

Spring4.2提供了EventListener注解来支持这种用法:

```
package com.tuya;

import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

@Component
public class DemoListener3 {

	@EventListener
	public void onEvent(DemoEvent event) {
		System.out.println("DemoListener3-DemoEvent消息: " + event.getMsg());
	}
	
	@EventListener
	public void onEvent(DemoEvent2 event) {
		System.out.println("DemoListener3-DemoEvent2消息: " + event.getId());
	}
}
```

## 发布消息 ##

在main函数中依次发布事件:

```
package com.tuya;

//import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

@SpringBootApplication
public class HeiPaServerApplication {

	public static void main(String[] args) {
//		SpringApplication.run(HeiPaServerApplication.class, args);
		AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(ServerConfig.class);
		
		DemoPublisher demoPublisher = context.getBean(DemoPublisher.class);
		demoPublisher.publish("hello application event");
		
		demoPublisher.publish(10);
		
		context.close();
	}
}
```

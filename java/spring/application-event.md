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
		
		demoPublisher.publish(10);
		
		context.close();
	}
}
```

### 结果 ###

以上代码正确的输出了监听器中的print, 可见该监听器已经正确的接收到消息并进行了相应的处理.
在代码中我们并不需要知道该消息会被哪些class接收并处理, 实现了消息发送者与接收者之间的解耦.

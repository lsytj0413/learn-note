# Spring多线程 #

Spring通过任务执行器(TaskExecutor)来实现多线程和并发编程, 使用ThreadPoolTaskExecutor可实现一个基于线程池的TaskExecutor.

## 配置类 ##

在配置类中开启异步任务支持并重写相关方法:

```
package com.tuya;

import java.util.concurrent.Executor;

import org.springframework.aop.interceptor.AsyncUncaughtExceptionHandler;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.AsyncConfigurer;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

@Configuration
@ComponentScan("com.tuya")
@EnableAsync
public class TaskExecutorConfig implements AsyncConfigurer {
	@Override
	public Executor getAsyncExecutor() {
		ThreadPoolTaskExecutor taskExecutor = new ThreadPoolTaskExecutor();
		taskExecutor.setCorePoolSize(5);
		taskExecutor.setMaxPoolSize(10);
		taskExecutor.setQueueCapacity(25);
		taskExecutor.initialize();
		return taskExecutor;
	}
	
	@Override
	public AsyncUncaughtExceptionHandler getAsyncUncaughtExceptionHandler() {
		return null;
	}
}
```

## 任务执行类 ##

通过Async注解表明方法/类是异步方法:

```
package com.tuya;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
public class AsyncTaskService {

	@Async
	public void executeAsyncTask(Integer i) {
		System.out.println("执行异步任务:" + i);
	}
	
	@Async
	public void executeAsyncTaskPlus(Integer i) {
		System.out.println("执行异步任务+1:" + (i + 1));
	}
}
```

## 执行任务 ##

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
		
		AsyncTaskService asyncTaskService = context.getBean(AsyncTaskService.class);
		for (int i = 0;  i < 10; ++i) {
			asyncTaskService.executeAsyncTask(i);
			asyncTaskService.executeAsyncTaskPlus(i);
		}
		
		context.close();
	}
}
```

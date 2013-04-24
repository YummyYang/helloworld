package yummy.spring.hello;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class HelloWorldSpringDI {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// Initialize Spring Application Context
		ApplicationContext ctx = new ClassPathXmlApplicationContext("META-INF/spring/app-context.xml");
		IMessageRenderer mr = ctx.getBean("renderer", IMessageRenderer.class);
		mr.render();
	}

}

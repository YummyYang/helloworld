package yummy.test;
public class HelloWorldDecoupled{
	public static void main(String[] args){
		IMessageRenderer mr = new StandardOutMessageRenderer();
		IMessageProvider mp = new HelloWorldMessageProvider();
		mr.setMessageProvider(mp);
		mr.render();
	}
}

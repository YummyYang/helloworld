package yummy.spring.hello;

public interface IMessageRenderer {
	public void render();
	public void setMessageProvider(IMessageProvider provider);
	public IMessageProvider getMessageProvider();
}

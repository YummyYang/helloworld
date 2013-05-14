package yummy.test;

public interface IMessageRenderer{
	public void render();
	public void setMessageProvider(IMessageProvider provider);
	public IMessageProvider getMessageProvider();
}

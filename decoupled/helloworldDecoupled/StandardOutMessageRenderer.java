package yummy.test;

public class StandardOutMessageRenderer implements IMessageRenderer{
	private IMessageProvider messageProvider = null;
	public void setMessageProvider(IMessageProvider provider){
		this.messageProvider = provider;
	}
	public IMessageProvider getMessageProvider(){
		return this.messageProvider;
	}
	public void render(){
		if(messageProvider == null){
			throw new RuntimeException(
				"You must set the Property messageProvider of class:"
				+ StandardOutMessageRenderer.class.getName());
		}
		System.out.println(messageProvider.getMessage());
	}
}

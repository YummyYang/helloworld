package yummy.test;

public class StandardOutMessageRenderer implements MessageRenderer{
	private MessageProvider messageProvider = null;
	public void setMessageProvider(MessageProvider provider){
		this.messageProvider = provider;
	}
	public MessageProvider getMessageProvider(){
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

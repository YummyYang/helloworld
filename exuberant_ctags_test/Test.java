package yummy.test;

import java.util.*;
public class Test{

	public static void main(String[] args){
		if(args.length > 0 && args.length < 2){
			System.out.println("Okey , length:" + args.length + " ,args[0]:" + args[0]);
		}else if(args.length >=2){
			System.err.println("Error: args.length >=2");
		}else{
			System.out.println("Well , javacomplete/compile/run looks ok~");
		}
	}
	void test(){
		//calculate GC time
		System.currentTimeMillis();
		System.gc();
		System.currentTimeMillis();
		System.getenv();
	}
	void ok(){

	}
	void faint(){

	}
	void again(){

	}
	void very_strange(){

	}
}

class C1 extends Test{

}


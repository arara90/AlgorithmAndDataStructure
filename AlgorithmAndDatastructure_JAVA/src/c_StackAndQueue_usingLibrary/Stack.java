package c_StackAndQueue_usingLibrary;
import java.util.*;

public class Stack {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		java.util.Stack<Integer> s = new java.util.Stack<Integer>();
		System.out.println("A stack is created");

		// insert(push)
		for(int i=0; i<10; i++) 
			s.push(new Integer(i));
		
		// delete(pop)
		for(int i=0; i<s.size(); i++) 
			System.out.println(s.pop());
	}

}

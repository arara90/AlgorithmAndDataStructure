package c_StackAndQueue_usingLibrary;
import java.util.*;



public class Queue {

	// 자바의 연결리스트는 자료구조의 연결리스트가 아닌 큐를 구현한 것. 즉 자바의 LinkedList = Queue
	//offer 와 poll 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList <String> ls = new LinkedList<String>();
		
		ls.offer("A");
		ls.offer("B");
		ls.offer("C");
		ls.offer("D");
		
		System.out.println("Size = " + ls.size() );
		
//		while(!ls.isEmpty()) { System.out.println(ls.poll()); }
		while(ls.peek() != null) //읽을 값이 있는지 확인
		{
			 System.out.println(ls.poll());
		}
		
		System.out.println("Size = " + ls.size() );

	}

}

package c_StackAndQueue_usingLibrary;
import java.util.*;



public class Queue {

	// �ڹ��� ���Ḯ��Ʈ�� �ڷᱸ���� ���Ḯ��Ʈ�� �ƴ� ť�� ������ ��. �� �ڹ��� LinkedList = Queue
	//offer �� poll 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList <String> ls = new LinkedList<String>();
		
		ls.offer("A");
		ls.offer("B");
		ls.offer("C");
		ls.offer("D");
		
		System.out.println("Size = " + ls.size() );
		
//		while(!ls.isEmpty()) { System.out.println(ls.poll()); }
		while(ls.peek() != null) //���� ���� �ִ��� Ȯ��
		{
			 System.out.println(ls.poll());
		}
		
		System.out.println("Size = " + ls.size() );

	}

}
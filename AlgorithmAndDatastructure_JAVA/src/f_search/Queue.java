//  https://youtu.be/W3jNbNGyjMs
//  따라해보기 (Queue 구현)
package f_search;
import java.util.NoSuchElementException;

public class Queue<T> {
	class Node<T>{
		private T data;
		private Node<T> next;
		
		public Node(T data) {
			this.data = data;
		}
	} //Node
	
	private Node<T> first; 
	private Node<T> last;
	
	
	// 1. 추가
	public void enqueue(T item) {
		Node<T> t = new Node<T>(item);
		if (last != null) {
			last.next = t;
		}
		last = t;
		
		if(first == null) {
			first = last;
		}
	}
	
	// 2. 제거
	public T dequeue(){
		
		//빈 큐일 경우 예외처리
		if(first == null) {
			throw new NoSuchElementException();
		}
		
		T data = first.data;
		first = first.next;
		if(first == null) {
			last = null;
		}
		
		return data;
	}
	
	public T peek() {
		if(first == null) {
			throw new NoSuchElementException();
		}
		return first.data;	
	}
	
	public boolean isEmpty() {
		return first == null;
	}
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Queue<Integer> q = new Queue<Integer>();
		q.enqueue(1);
		q.enqueue(2);
		q.enqueue(3);
		q.enqueue(4);
		
		System.out.print(q.dequeue());	//1
		System.out.print(q.dequeue());	//2
		System.out.print(q.peek()); 	//3
		System.out.print(q.dequeue());	//2
		System.out.print(q.isEmpty());	//false
		System.out.print(q.dequeue());	//4
		System.out.print(q.isEmpty());	//true
		
	}

}

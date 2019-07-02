package b_stack_linkedList;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LinkedList list = new LinkedList();
		
		list.insert(1, 100);
		list.insert(2, 200);
		list.insert(3, 300);
		list.insert(4, 400);
		list.insert(5, 500);
		
		list.print();
		
		while(!list.isEmpty()) {
			Link deletedLink = list.delete();
			System.out.print("deleted: ");
			deletedLink.print();
			System.out.println("");
		}
		
		list.print();
	
	}

}

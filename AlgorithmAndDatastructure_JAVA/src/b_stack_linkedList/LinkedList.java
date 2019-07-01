package b_stack_linkedList;


public class LinkedList {
	
	private Link first;
	
	// ������
	public LinkedList() {
		// ó�� ���Ḯ��Ʈ�� �ƹ��� ���ھ��� �����ϸ� �� ����Ʈ�� �����ȴ�.
		first = null;
	}
	
	// isEmpty
	public boolean isEmpty(){ return first == null; }
	
	// ����
	public void insert(int d1, double d2){
		Link link = new Link(d1, d2);
		link.nextLink = first;
		first = link;
	}
	
	// ���� : ù��° ���� ����
	public Link delete() {
		// ���� ����
		Link tmp = first;
		first = first.nextLink;
		// ���̽���� ���� : Garbage Collector. ���̽�/C/C++�� overflow ������ ���� delete�� �� �޸� ���� �۾��� ���� ���־�� ������ �ڹٴ� �˾Ƽ�.
		// System.gc(); �ǹ����� ����ϸ� �ȵȴ�. �����带 �� ���δٰ� ��. https://yaboong.github.io/java/2018/06/09/java-garbage-collection/)
		return tmp;
	}

	// ���
	public void print() {
		Link current = first;
		System.out.print("List: " );
		while ( current != null) {
			current.print();
			current = current.nextLink;
		}
		System.out.println("" );
		
	}

}
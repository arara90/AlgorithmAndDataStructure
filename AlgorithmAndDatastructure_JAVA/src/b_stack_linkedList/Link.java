package b_stack_linkedList;

public class Link {
	public int data1;
	public double data2;
	public Link nextLink;
	
	// 생성자
	public Link (int d1, double d2) {
		data1 = d1;
		data2 = d2;
	}
	
	// node 데이터 출력
	public void print() {
		System.out.printf( "{" + data1 + "," + data2 + "}" );
	}

	
}

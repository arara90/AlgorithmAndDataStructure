package d_binarytree;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Tree Tm = new Tree();
		Tm.add(10, "CHO");
		Tm.add(20, "KIM");
		Tm.add(30, "minho");
		Tm.add(40, "JYeon");
		
		System.out.println("Data Search and Get");
		Object Temp = Tm.get(20);
		System.out.println(Temp);
		
		System.out.println("Data Search and Get");
		Object Temp2 = Tm.get(40);
		System.out.println(Temp2);
		

	}

}

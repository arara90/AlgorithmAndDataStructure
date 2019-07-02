package e_vector;
import java.util.Vector;

public class VectorTest {

	public static void main(String[] args) {
		// 정수 값만 다루는 제네릭 벡터 생성
		Vector<Integer> vector = new Vector<Integer>();
		
		vector.add(5);
		vector.add(4);
		vector.add(-1);
		
		//벡터 중간에 삽입
		vector.add(2,100); // 4와 -1사이에 100삽입  (1)  -1 (2) 4 (3) 5
		
		System.out.println("벡터 안의 요소 객체 수 : " + vector.size());
		System.out.println("벡터의 현재 용량 : " + vector.capacity());
		
		//모든 정수 요소 출력
		for (int i =0 ; i<vector.size();i++) {
			int n = vector.get(i);
			System.out.println(n);
		}
		
		int sum = 0;
		//모든 정보 더하기
		for (int i =0 ; i<vector.size();i++) {
			int n = vector.elementAt(i);
			sum += n;
		}
		
		System.out.println(sum);
		System.out.println("벡터에 있는 정수의 합 : " + sum);
		

	}

}

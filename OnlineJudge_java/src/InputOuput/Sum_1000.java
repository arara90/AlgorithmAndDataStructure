package InputOuput;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sum_1000 {

	public static void main(String[] args) throws IOException {

	/////////// 오답노트  ///////////
	////////////next()는 space가 먹지 않아! space를 종료키로 인식
	//		Scanner sc = new Scanner(System.in);
	//		String str = sc.next();
	//		sc.close();
	//		
	//		String[] inputs = str.split(" ");
	//	 	int res = Integer.parseInt(inputs[0]) + Integer.parseInt(inputs[1]);  	// index에러 1이 없음
	//		System.out.print(inputs.length);										//1 즉, 스페이스에서 종료됨

	BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
	String input = in.readLine();
	String[] inputs = input.split(" ");
	System.out.print( Integer.parseInt(inputs[0]) + Integer.parseInt(inputs[1]) );


		
	}
	
}



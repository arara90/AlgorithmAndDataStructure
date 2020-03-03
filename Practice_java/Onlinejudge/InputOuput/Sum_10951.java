package InputOuput;
import java.io.*;
import java.util.ArrayList;

// https://wanna-b.tistory.com/59
//12992KB	84ms
public class Sum_10951 {
	public static void main(String[] args) throws IOException {
		String input = "";
		String[] tmp = new String[2];
		ArrayList array = new ArrayList();

		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while ( (input = br.readLine()) !=null) {
			tmp = input.split(" ");
			array.add(  Integer.parseInt( tmp[0] ) + Integer.parseInt( tmp[1] ) );
		}
		
		for(int i=0; i<array.size(); i++) {
			System.out.println(array.get(i));
		}
		
		
	}

}



////2. OutputStreamWriter쓰기 : 속도 더 빠르고, 자원 더먹는다.
// 13060KB	80ms
//import java.io.BufferedReader;
//import java.io.InputStreamReader;
//import java.io.IOException;
//import java.io.BufferedWriter;
//import java.io.OutputStreamWriter;
//class Main{
//    public static void main(String[] args) throws IOException{
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        String str = br.readLine();
//        while(str != null){
//            String[] strs = str.split(" ");
//            bw.write(Integer.parseInt(strs[0]) + Integer.parseInt(strs[1]) + "\n");
//            str = br.readLine();
//        }
//        bw.flush();
//        br.close();
//        bw.close();
//    }
//}



////3. Scanner 쓰기
////    Scanner를 사용할 경우는 sc.hasNextInt()와 같은 함수를 사용한다
//
//import java.util.Scanner;
//public class Main{
//	public static void main(String[] args) {
//		Scanner s = new Scanner(System.in);
//		while(s.hasNextInt()) {
//			int a = s.nextInt();
//			int b = s.nextInt();
//			
//			System.out.println(a+b);
//		}
//	}
//	
//}

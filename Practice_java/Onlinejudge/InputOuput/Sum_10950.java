package InputOuput;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sum_10950 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
		int[] arr = new int[num];
		String[] tmp = new String[2];
		
		for(int i=0; i<num; i++) {
			tmp = br.readLine().split(" ");
			arr[i] =  Integer.parseInt( tmp[0] ) + Integer.parseInt( tmp[1] );
		}
		
		for(int i=0; i<num; i++) {
			System.out.println(arr[i]);
		}
	}

}

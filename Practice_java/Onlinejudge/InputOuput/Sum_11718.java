package InputOuput;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Sum_11718 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String input;
		

		while( (input=br.readLine()) != null  ) {
			bw.write(input + "\n");

		}
		br.close();
		bw.flush();
		bw.close();
		
//		 Scanner scan = new Scanner(System.in);
//	     String str = "";
//	     while(scan.hasNext()){
//	     	str = scan.nextLine();
//	     System.out.println(str);
//		
	}
	
	
	
}

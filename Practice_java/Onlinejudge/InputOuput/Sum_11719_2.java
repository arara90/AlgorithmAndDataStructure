package InputOuput;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

//https://plplim.tistory.com/7
public class Sum_11719_2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder builder = new StringBuilder();
		
		
		while(true){
		    String str = br.readLine();
		    if (str == null || str.isEmpty()) {
		        break;
		    }
		    
		    builder.append(str).append("\n");
		}
		br.close();
		
		System.out.println(builder);
	
	}
	
}

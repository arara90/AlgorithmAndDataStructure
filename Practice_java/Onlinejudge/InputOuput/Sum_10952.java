package InputOuput;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Sum_10952 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList array = new ArrayList();
		String input = "";
		int a,b;
		
		while( (input = br.readLine()) != null) {
			String[] tmp = input.split(" ");
			a = Integer.parseInt(tmp[0]); 
			b = Integer.parseInt(tmp[1]);
			if(a==0 && b==0) break;
			else array.add( Integer.parseInt(tmp[0]) + Integer.parseInt(tmp[1]));
		}
		br.close();
		
		for(int i=0; i<array.size(); i++) {
			System.out.println(array.get(i));
		}
		
	}

}

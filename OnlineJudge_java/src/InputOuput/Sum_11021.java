package InputOuput;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Sum_11021 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList array = new ArrayList();

		int num = Integer.parseInt( br.readLine() );
		
		while( num > 0 ) {
			String[] tmp = br.readLine().split(" ");
			array.add( Integer.parseInt(tmp[0]) + Integer.parseInt(tmp[1]));
			num--;
		}
		br.close();
		
		for(int i=0; i<array.size(); i++) {
			System.out.println("Case #" + (i+1) + ": " +  array.get(i));
		}
		
	}

}

package InputOuput;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Sum_11022 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
//		ArrayList array = new ArrayList();
		int num = Integer.parseInt( br.readLine() );
		
		int res;
		String str = "";
		int i = 0;
		while( i < num ) {
			String[] tmp = br.readLine().split(" ");
			int a = Integer.parseInt(tmp[0]);
			int b = Integer.parseInt(tmp[1]);
			res = a + b;
			str = "Case #" + (i+1) + ": " + a + " + " + b + " = " + res + "\n";
			bw.write(str);
			i++;
		}
		br.close();
		bw.flush();
		bw.close();
		
	}

}

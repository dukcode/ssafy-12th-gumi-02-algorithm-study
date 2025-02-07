import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class B2228 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		BigInteger a = new BigInteger(br.readLine());
		BigInteger b = new BigInteger(br.readLine());

		bw.write(a.add(b) + "\n");
		bw.write(a.subtract(b) + "\n");
		bw.write(String.valueOf(a.multiply(b)));

		br.close();
		bw.close();
	}
}

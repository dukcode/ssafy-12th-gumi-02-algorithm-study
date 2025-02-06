import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B17263 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());
		int maximum = 0;
		for (int i = 0; i < n; i++) {
			int cur_num = Integer.parseInt(st.nextToken());
			maximum = Math.max(maximum, cur_num);
		}

		bw.write(String.valueOf(maximum));
		br.close();
		bw.close();
	}
}

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class B2845 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int humanNumber = Integer.parseInt(st.nextToken());
		int area = Integer.parseInt(st.nextToken());

		int total = humanNumber * area;

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 5; i++) {
			int target = Integer.parseInt(st.nextToken());
			int answer = target - total;
			bw.write(answer +" ");
		}

		bw.close();
		br.close();
	}
}

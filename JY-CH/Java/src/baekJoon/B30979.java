import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B30979 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int totalTime = Integer.parseInt(br.readLine());
		int totalCandy = Integer.parseInt(br.readLine());
		int candySum = 0;

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < totalCandy; i++) {
			int candyTime = Integer.parseInt(st.nextToken());
			candySum += candyTime;
		}

		if (candySum >= totalTime) {
			bw.write("Padaeng_i Happy");
		} else {
			bw.write("Padaeng_i Cry");
		}

		br.close();
		bw.close();
	}
}

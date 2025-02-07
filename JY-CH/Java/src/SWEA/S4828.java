package SWEA;

import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class S4828 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int tc = Integer.parseInt(br.readLine());

		for (int i = 0; i < tc; i++) {
			int n = Integer.parseInt(br.readLine());
			int maximum = Integer.MIN_VALUE;
			int minimum = Integer.MAX_VALUE;
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				int cur_num = Integer.parseInt(st.nextToken());
				if (cur_num > maximum) {
					maximum = cur_num;
				}
				if (cur_num < minimum) {
					minimum = cur_num;
				}
			}


			bw.write("#" + (i+1) + " " + (maximum - minimum) + "\n");
		}
		br.close();
		bw.close();
	}
}

package SWEA;

import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class S12471 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int tc = Integer.parseInt(br.readLine());

		for (int i = 0; i < tc; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int length = Integer.parseInt(st.nextToken());
			int sumRange= Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			int[] arr = new int[length];
			for (int j = 0; j < length; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
			}

			int min = 0;
			int max = 0;
			for (int o = 0; o < sumRange; o++) {
				min += arr[o];
				max += arr[length - 1 - o];
			}
			bw.write("#" + (i+1) + " " + (max - min) + "\n");

		}
		br.close();
		bw.close();

	}
}


package SWEA;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class S4828_1 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int tc = Integer.parseInt(br.readLine());

		for (int i = 0; i < tc; i++) {
			int n = Integer.parseInt(br.readLine());
			int[] arr = new int[n];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				int cur_num = Integer.parseInt(st.nextToken());
				arr[j] = cur_num;
				}
			for (int j = 0; j < arr.length; j++) {
				for (int k = j + 1; k < arr.length; k++) {
					if (arr[j] > arr[k]) {
						int tmp = arr[k];
						arr[k] = arr[j];
						arr[j] = tmp;
					}
				}
			}
			int answer = arr[n-1] - arr[0];




			bw.write("#" + (i+1) + " " + answer + "\n");
		}
		br.close();
		bw.close();
	}
}

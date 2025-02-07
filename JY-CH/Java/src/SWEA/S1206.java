package SWEA;

import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.StringTokenizer;

public class S1206 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int tc = 10;

		for (int i = 0; i < tc; i++) {
			int length = Integer.parseInt(br.readLine());
			int[] arr = new int[length];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int arrIndex = 0; arrIndex < length; arrIndex++) {
				arr[arrIndex] = Integer.parseInt(st.nextToken());
			}
			// 조망권 체크 합시다.
			int goodViewHome = 0;
			for (int viewRange = 2; viewRange < length - 2; viewRange++) {
				if (Math.max(arr[viewRange - 2], arr[viewRange - 1]) < arr[viewRange] & Math.max(arr[viewRange + 1], arr[viewRange + 2]) < arr[viewRange]) {
					goodViewHome += (arr[viewRange] - Math.max(Math.max(arr[viewRange - 2], arr[viewRange - 1]), Math.max(arr[viewRange + 1], arr[viewRange + 2])));
				}
			}

			bw.write("#" + (i+1) + " " + goodViewHome + "\n");
		}

		bw.close();
		br.close();

	}
}

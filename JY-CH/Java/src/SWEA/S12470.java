package SWEA;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class S12470 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int tc = Integer.parseInt(br.readLine());
		for (int i = 0; i < tc; i++) {
			int cardNumber = Integer.parseInt(br.readLine());
			String[] arr = String.valueOf(br.readLine()).split("");
			// 카운팅 해야지
			int[] result = new int[10];
			int answerNumber = 0;
			int answerCount = 0;
			for (int j = 0; j < arr.length; j++) {
				result[Integer.parseInt(arr[j])]++;
				if (answerCount <= result[Integer.parseInt(arr[j])]) {
					if (answerNumber < Integer.parseInt(arr[j]))
						answerNumber = Integer.parseInt(arr[j]);
						answerCount = result[Integer.parseInt(arr[j])];
				}
			}
			bw.write("#" + (i+1) + " " + answerNumber + " " + answerCount);
			bw.newLine();




		}
		br.close();
		bw.close();
	}
}

package SWEA;

import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class S12471 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int tc = Integer.parseInt(br.readLine());

		for (int i = 0; i < tc; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int length = Integer.parseInt(st.nextToken());
			int sumRange = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			int[] arr = new int[length];
			for (int j = 0; j < length; j++) {
				arr[j] = Integer.parseInt(st.nextToken());
			}

			int maxPartialSum = Integer.MIN_VALUE;
			int minPartialSum = Integer.MAX_VALUE;
			int partialSum = 0;
			Queue<Integer> queue = new LinkedList<>();
			Stack<Integer> stk = new Stack<>();
			for (int num : arr) {
				partialSum += num;
				queue.offer(num);
				if (!queue.isEmpty() && queue.size() > sumRange) {
					partialSum -= queue.poll();
				}

				if (queue.size() == sumRange) {
					maxPartialSum = Math.max(maxPartialSum, partialSum);
					minPartialSum = Math.min(minPartialSum, partialSum);
				}
			}

			bw.write(String.valueOf(maxPartialSum - minPartialSum));
			bw.newLine();
		}

		bw.close();
		br.close();

	}

}
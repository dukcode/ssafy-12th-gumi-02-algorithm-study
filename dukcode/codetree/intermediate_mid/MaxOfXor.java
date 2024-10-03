package com.dukcode.codetree.intermediate_low.backtracking;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MaxOfXor {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    bw.write(String.valueOf(solve(-1, 0, 0)));

    bw.close();
    br.close();
  }

  private static int solve(int lastIdx, int cnt, int val) {
    if (cnt == m) {
      return val;
    }

    int ret = 0;
    for (int nextIdx = lastIdx + 1; nextIdx < n; nextIdx++) {
      ret = Math.max(ret, solve(nextIdx, cnt + 1, val ^ arr[nextIdx]));
    }

    return ret;
  }

}

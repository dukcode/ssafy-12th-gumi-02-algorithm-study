package com.dukcode.solvedac.class_01;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B2457 {

  private static final int N = 5;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int[] nums = new int[N];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < N; i++) {
      nums[i] = Integer.parseInt(st.nextToken());
    }

    int ans = 0;
    for (int num : nums) {
      ans += num * num;
      ans %= 10;
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();

  }


}

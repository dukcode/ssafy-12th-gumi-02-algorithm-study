package com.dukcode.solvedac.class_02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B11050 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());

    cache = new int[n + 1][n + 1];
    for (int i = 0; i <= n; ++i) {
      Arrays.fill(cache[i], -1);
    }

    bw.write(String.valueOf(comb(n, k)));

    br.close();
    bw.close();

  }

  private static int comb(int n, int k) {
    if (k == 0 || k == n) {
      return 1;
    }

    if (cache[n][k] != -1) {
      return cache[n][k];
    }

    return cache[n][k] = comb(n - 1, k) + comb(n - 1, k - 1);
  }

}

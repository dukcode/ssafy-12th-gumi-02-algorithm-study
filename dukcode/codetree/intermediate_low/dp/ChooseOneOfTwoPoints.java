package com.dukcode.codetree.intermediate_low.dp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class ChooseOneOfTwoPoints {

  private static final int MN = -987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] red;
  private static int[] blue;

  private static int[][][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    red = new int[2 * n];
    blue = new int[2 * n];
    for (int i = 0; i < 2 * n; i++) {
      st = new StringTokenizer(br.readLine());
      red[i] = Integer.parseInt(st.nextToken());
      blue[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[2 * n][n + 1][n + 1];
    for (int z = 0; z < 2 * n; z++) {
      for (int y = 0; y <= n; y++) {
        Arrays.fill(cache[z][y], -1);
      }
    }

    bw.write(String.valueOf(solve(2 * n - 1, n, n)));

    br.close();
    bw.close();
  }

  private static int solve(int i, int rCnt, int bCnt) {
    if (i == -1 && rCnt == 0 && bCnt == 0) {
      return 0;
    }

    if (rCnt < 0 || bCnt < 0) {
      return MN;
    }

    if (cache[i][rCnt][bCnt] != -1) {
      return cache[i][rCnt][bCnt];
    }

    return cache[i][rCnt][bCnt] = Math.max(
        red[i] + solve(i - 1, rCnt - 1, bCnt),
        blue[i] + solve(i - 1, rCnt, bCnt - 1));
  }


}

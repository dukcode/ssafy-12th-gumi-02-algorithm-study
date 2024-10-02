package com.dukcode.codetree.intermediate_low.simulation;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BestPlaceOf33 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = 0;
    for (int y = 0; y < n - 2; ++y) {
      for (int x = 0; x < n - 2; ++x) {
        ret = Math.max(ret, cntCoins(y, x));
      }
    }

    return ret;
  }

  private static int cntCoins(int sy, int sx) {
    int ret = 0;
    for (int y = sy; y < sy + 3; ++y) {
      for (int x = sx; x < sx + 3; ++x) {
        ret += board[y][x];
      }
    }

    return ret;
  }


}

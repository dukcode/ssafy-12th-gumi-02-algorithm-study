package com.dukcode.swea.a;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 활주로 건설
public class S4014 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int x;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      x = Integer.parseInt(st.nextToken());

      board = new int[n][n];
      for (int y = 0; y < n; ++y) {
        st = new StringTokenizer(br.readLine());
        for (int x = 0; x < n; ++x) {
          board[y][x] = Integer.parseInt(st.nextToken());
        }
      }

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = 0;
    for (int i = 0; i < n; i++) {
      int[] col = new int[n];
      for (int y = 0; y < n; y++) {
        col[y] = board[y][i];
      }

      if (canBuild(col, x)) {
        ret++;
      }

      if (canBuild(board[i], x)) {
        ret++;
      }
    }

    return ret;
  }

  public static boolean canBuild(int[] line, int x) {
    int h = line[0];
    int cnt = 1;
    for (int i = 1; i < line.length; i++) {
      if (h == line[i]) {
        cnt++;
        continue;
      }

      if (Math.abs(h - line[i]) > 1) {
        return false;
      }

      boolean up = line[i] - h > 0;
      if (up) {
        if (cnt < x) {
          return false;
        }
        h = line[i];
        cnt = 1;
        continue;
      }

      if (cnt < 0) {
        return false;
      }

      h = line[i];
      cnt = 1 - x;
    }

    return cnt >= 0;
  }


}

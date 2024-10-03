package com.dukcode.codetree.intermediate_low.dfs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class PuyoPuyo {

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  private static boolean[][] vis;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    board = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    int[] ans = solve();
    bw.write(String.valueOf(ans[0]));
    bw.write(' ');
    bw.write(String.valueOf(ans[1]));

    br.close();
    bw.close();

  }

  private static int[] solve() {
    vis = new boolean[n][n];
    int cntBoom = 0;
    int maxBlocks = 0;
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (vis[y][x]) {
          continue;
        }

        int cnt = dfs(y, x);
        maxBlocks = Math.max(maxBlocks, cnt);
        if (cnt < 4) {
          continue;
        }

        cntBoom++;
      }
    }

    return new int[]{cntBoom, maxBlocks};
  }

  private static int dfs(int y, int x) {
    vis[y][x] = true;

    int cnt = 1;
    for (int dir = 0; dir < 4; dir++) {
      int ny = y + DY[dir];
      int nx = x + DX[dir];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      if (vis[ny][nx] || board[y][x] != board[ny][nx]) {
        continue;
      }

      cnt += dfs(ny, nx);
    }

    return cnt;
  }

}

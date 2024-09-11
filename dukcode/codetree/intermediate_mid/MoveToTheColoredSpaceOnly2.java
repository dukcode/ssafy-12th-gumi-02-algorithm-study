package com.dukcode.codetree.intermediate_mid.parametric_search.parametric_search;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class MoveToTheColoredSpaceOnly2 {

  private static final int BLANK = 0;
  private static final int COLORED = 1;

  private static final int MX_D = 1_000_000_000;

  private static final int[] DELTA_Y = {-1, 1, 0, 0};
  private static final int[] DELTA_X = {0, 0, -1, 1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static int[][] board;
  private static List<Point> colors;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());

    board = new int[h][w];
    for (int y = 0; y < h; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    colors = new ArrayList<>();
    for (int y = 0; y < h; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; ++x) {
        int color = Integer.parseInt(st.nextToken());
        if (color == COLORED) {
          colors.add(new Point(y, x));
        }
      }
    }

    cntColor(21);
    cntColor(20);

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int minD = 0;
    int maxD = MX_D;

    while (minD <= maxD) {
      int halfD = (maxD + minD) / 2;
      if (cntColor(halfD) < colors.size()) {
        minD = halfD + 1;
      } else {
        maxD = halfD - 1;
      }
    }

    return minD;
  }

  private static void dfs(int y, int x, int d, boolean[][] vis) {
    vis[y][x] = true;

    for (int dir = 0; dir < 4; ++dir) {
      int ny = y + DELTA_Y[dir];
      int nx = x + DELTA_X[dir];

      if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
        continue;
      }

      if (vis[ny][nx]) {
        continue;
      }

      if (Math.abs(board[y][x] - board[ny][nx]) > d) {
        continue;
      }

      dfs(ny, nx, d, vis);
    }
  }

  private static int cntColor(int d) {
    boolean[][] vis = new boolean[h][w];

    Point first = colors.get(0);
    dfs(first.y, first.x, d, vis);

    int ret = 0;
    for (Point p : colors) {
      if (vis[p.y][p.x]) {
        ret++;
      }
    }

    return ret;
  }

  private static class Point {

    int y;
    int x;

    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }


}

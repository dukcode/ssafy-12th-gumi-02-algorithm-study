package com.dukcode.codetree.intermediate_low.simulation;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MaxAreaOfPositiveRectangle {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static int[][] board;

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

    bw.write(String.valueOf(getMaxPositiveArea()));

    br.close();
    bw.close();
  }

  private static int getMaxPositiveArea() {
    int maxArea = -1;
    for (int y = 0; y < h; ++y) {
      for (int x = 0; x < w; ++x) {
        maxArea = Math.max(maxArea, getMaxPositiveArea(y, x));
      }
    }
    return maxArea;
  }

  private static int getMaxPositiveArea(int sy, int sx) {
    int ret = -1;
    for (int ey = sy; ey < h; ++ey) {
      for (int ex = sx; ex < w; ++ex) {
        ret = Math.max(ret, getPositiveArea(sy, sx, ey, ex));
      }
    }
    return ret;
  }

  private static int getPositiveArea(int sy, int sx, int ey, int ex) {
    for (int y = sy; y <= ey; ++y) {
      for (int x = sx; x <= ex; ++x) {
        if (board[y][x] <= 0) {
          return -1;
        }
      }
    }

    return (ey - sy + 1) * (ex - sx + 1);
  }


}

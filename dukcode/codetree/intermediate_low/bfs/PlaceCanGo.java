package com.dukcode.codetree.intermediate_low.bfs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class PlaceCanGo {

  private static final int[] DY = {1, 0, -1, 0};
  private static final int[] DX = {0, 1, 0, -1};

  private static final int WALL = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int[][] board;

  private static boolean[][] discovered;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    discovered = new boolean[n][n];

    int cnt = 0;
    for (int i = 0; i < k; ++i) {
      st = new StringTokenizer(br.readLine());
      int r = Integer.parseInt(st.nextToken()) - 1;
      int c = Integer.parseInt(st.nextToken()) - 1;

      if (discovered[r][c]) {
        continue;
      }

      cnt += bfs(r, c);
    }

    bw.write(String.valueOf(cnt));

    br.close();
    bw.close();

  }

  private static int bfs(int r, int c) {
    Queue<Point> q = new LinkedList<>();

    q.offer(new Point(r, c));
    discovered[r][c] = true;

    int cnt = 0;

    while (!q.isEmpty()) {
      Point cur = q.poll();
      cnt++;
      for (int dir = 0; dir < 4; ++dir) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (discovered[ny][nx] || board[ny][nx] == WALL) {
          continue;
        }

        q.offer(new Point(ny, nx));
        discovered[ny][nx] = true;
      }
    }

    return cnt;
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

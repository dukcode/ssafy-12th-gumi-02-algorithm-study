package com.dukcode.baekjoon.simulation;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class B17822 {

  private static final int[] DY = {-1, 1, 0, 0};
  private static final int[] DX = {0, 0, -1, 1};

  private static final int CW = 0;
  private static final int CCW = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static int t;
  private static LinkedList<Integer>[] board;
  private static int x;
  private static int d;
  private static int k;

  private static int sum;
  private static int cnt;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());
    t = Integer.parseInt(st.nextToken());

    board = new LinkedList[h];
    for (int y = 0; y < h; ++y) {
      board[y] = new LinkedList<>();
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; ++x) {
        int num = Integer.parseInt(st.nextToken());
        board[y].add(num);
        sum += num;
        cnt++;
      }
    }

    for (int i = 0; i < t; ++i) {
      st = new StringTokenizer(br.readLine());
      x = Integer.parseInt(st.nextToken());
      d = Integer.parseInt(st.nextToken());
      k = Integer.parseInt(st.nextToken());

      move();
    }

    bw.write(String.valueOf(sum));

    br.close();
    bw.close();
  }

  private static void move() {
    rotate();
    if (remove()) {
      return;
    }
    moveToAvg();

  }

  private static void moveToAvg() {
    int toAdd = 0;
    for (int y = 0; y < h; ++y) {
      for (int x = 0; x < w; ++x) {
        int num = board[y].get(x);
        if (num == 0) {
          continue;
        }
        int diff = num * cnt - sum;
        if (diff > 0) {
          toAdd -= 1;
          board[y].set(x, num - 1);
        } else if (diff < 0) {
          toAdd += 1;
          board[y].set(x, num + 1);
        }
      }
    }

    sum += toAdd;
  }


  private static boolean remove() {
    boolean remove = false;
    boolean[][] toRemove = new boolean[h][w];
    for (int y = 0; y < h; ++y) {
      for (int x = 0; x < w; ++x) {
        int pivot = board[y].get(x);
        if (pivot == 0) {
          continue;
        }
        for (int dir = 0; dir < 4; ++dir) {
          int ny = y + DY[dir];
          int nx = x + DX[dir];

          if (ny < 0 || ny >= h) {
            continue;
          }

          if (nx < 0) {
            nx = w - 1;
          } else if (nx >= w) {
            nx = 0;
          }

          if (board[ny].get(nx) != pivot) {
            continue;
          }

          remove = true;
          toRemove[y][x] = true;
          toRemove[ny][nx] = true;
        }
      }
    }

    if (!remove) {
      return false;
    }

    int cntNow = 0;
    int sumNow = 0;
    for (int y = 0; y < h; ++y) {
      for (int x = 0; x < w; ++x) {
        int num = board[y].get(x);
        if (num != 0 && !toRemove[y][x]) {
          cntNow++;
          sumNow += num;
          continue;
        }
        board[y].set(x, 0);
      }
    }

    cnt = cntNow;
    sum = sumNow;

    return true;
  }

  private static void rotate() {
    for (int idx = 0; idx < h; ++idx) {
      if ((idx + 1) % x != 0) {
        continue;
      }

      rotate(idx, d, k);
    }
  }

  private static void rotate(int h, int dir, int k) {
    if (dir == CW) {
      for (int i = 0; i < k; ++i) {
        board[h].offerFirst(board[h].pollLast());
      }
      return;
    }

    for (int i = 0; i < k; ++i) {
      board[h].offerLast(board[h].pollFirst());
    }
  }

}

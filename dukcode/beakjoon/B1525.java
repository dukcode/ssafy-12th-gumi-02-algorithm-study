package com.dukcode.baekjoon.bfs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Queue;
import java.util.StringTokenizer;

public class B1525 {

  private static final int[] dy = {-1, 0, 0, 1};
  private static final int[] dx = {0, -1, 1, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static State start;
  private static State end;

  private static int n = 3;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int[][] startBoard = new int[n][n];
    int zeroY = -1;
    int zeroX = -1;
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        startBoard[y][x] = Integer.parseInt(st.nextToken());
        if (startBoard[y][x] == 0) {
          zeroY = y;
          zeroX = x;
        }
      }
    }
    start = new State(startBoard, zeroY, zeroX);

    int[][] endBoard = new int[n][n];
    int num = 1;
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (y == n - 1 && x == n - 1) {
          continue;
        }
        endBoard[y][x] = num++;
      }
    }
    end = new State(endBoard, n - 1, n - 1);

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    Map<State, Integer> dist = new HashMap<>();
    Queue<State> q = new ArrayDeque<>();

    q.offer(start);
    dist.put(start, 1);
    q.offer(end);
    dist.put(end, -1);

    while (!q.isEmpty()) {
      State cur = q.poll();
      int curDist = dist.get(cur);
      for (State next : cur.nextAdj()) {

        Integer d = dist.get(next);
        if (d == null) {
          dist.put(next, increase(curDist));
          q.offer(next);
          continue;
        }

        if (sign(d) != sign(curDist)) {
          return Math.abs(d) + Math.abs(curDist) - 1;
        }
      }
    }

    return -1;
  }

  private static int sign(int dist) {
    if (dist < 0) {
      return -1;
    }

    return 1;
  }

  private static int increase(int dist) {
    if (dist < 0) {
      return dist - 1;
    }

    return dist + 1;
  }

  private static class State {

    private int[][] board;
    private int zeroY;
    private int zeroX;

    public State(int[][] board, int zeroY, int zeroX) {
      this.board = board;
      this.zeroY = zeroY;
      this.zeroX = zeroX;
    }

    private List<State> nextAdj() {
      List<State> adj = new ArrayList<>();

      for (int dir = 0; dir < 4; dir++) {
        int ny = zeroY + dy[dir];
        int nx = zeroX + dx[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        int[][] next = new int[n][n];
        for (int y = 0; y < n; y++) {
          System.arraycopy(board[y], 0, next[y], 0, n);
        }
        next[zeroY][zeroX] = next[ny][nx];
        next[ny][nx] = 0;
        adj.add(new State(next, ny, nx));
      }
      return adj;
    }

    @Override
    public boolean equals(Object o) {
      if (this == o) {
        return true;
      }
      if (o == null || getClass() != o.getClass()) {
        return false;
      }
      State state = (State) o;
      return Objects.deepEquals(board, state.board);
    }

    @Override
    public int hashCode() {
      return Arrays.deepHashCode(board);
    }
  }

}


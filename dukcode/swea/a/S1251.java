package com.dukcode.swea.a;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 하나로
public class S1251 {


  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int[][] islands;

  private static double e;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      n = Integer.parseInt(br.readLine());

      islands = new int[n][2];

      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; i++) {
        islands[i][0] = Integer.parseInt(st.nextToken());
      }

      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < n; i++) {
        islands[i][1] = Integer.parseInt(st.nextToken());
      }

      e = Double.parseDouble(br.readLine());

      bw.write("#" + tc + " ");
      bw.write(String.format("%.0f", solve()));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static double solve() {
    double ret = 0;
    boolean[] vis = new boolean[n];
    PriorityQueue<VisInfo> pq = new PriorityQueue<>(
        (v1, v2) -> Double.compare(v1.costBefore, v2.costBefore));

    pq.offer(new VisInfo(0, 0));

    while (!pq.isEmpty()) {
      VisInfo cur = pq.poll();
      int curIdx = cur.idx;

      if (vis[curIdx]) {
        continue;
      }

      vis[curIdx] = true;
      ret += cur.costBefore;

      for (int nextIdx = 0; nextIdx < n; nextIdx++) {
        if (nextIdx == curIdx) {
          continue;
        }

        if (vis[nextIdx]) {
          continue;
        }

        pq.offer(new VisInfo(nextIdx, getCost(curIdx, nextIdx)));
      }
    }

    return ret;
  }

  private static double getCost(int fr, int to) {
    int dx = Math.abs(islands[to][0] - islands[fr][0]);
    int dy = Math.abs(islands[to][1] - islands[fr][1]);
    return e * ((long) dx * dx + (long) dy * dy);
  }

  private static class VisInfo {

    int idx;
    double costBefore;

    public VisInfo(int idx, double costBefore) {
      this.idx = idx;
      this.costBefore = costBefore;
    }
  }

}

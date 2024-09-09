package com.dukcode.codetree.intermediate_mid.parametric_search.parametric_search;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaximizeDistOfNearestPoints {

  private static final int MX_DIST = 1_000_000_000;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static Line[] lines;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    lines = new Line[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int start = Integer.parseInt(st.nextToken());
      int end = Integer.parseInt(st.nextToken());

      lines[i] = new Line(start, end);
    }

    Arrays.sort(lines, (l1, l2) -> l1.start == l2.start ? l1.end - l2.end : l1.start - l2.start);

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int minDist = 1;
    int maxDist = MX_DIST;

    while (minDist <= maxDist) {
      int halfDist = (minDist + maxDist) / 2;
      if (countMaxPoints(halfDist) >= n) {
        minDist = halfDist + 1;
      } else {
        maxDist = halfDist - 1;
      }
    }

    return minDist - 1;
  }

  private static int countMaxPoints(int minDist) {
    int cnt = 0;
    int lastPos = -MX_DIST;
    for (Line line : lines) {
      int nextLastPos = Math.max(lastPos + minDist, line.start);
      if (nextLastPos > line.end) {
        continue;
      }

      cnt++;
      lastPos = nextLastPos;
    }

    return cnt;
  }

  private static class Line {

    int start;
    int end;

    public Line(int start, int end) {
      this.start = start;
      this.end = end;
    }
  }


}

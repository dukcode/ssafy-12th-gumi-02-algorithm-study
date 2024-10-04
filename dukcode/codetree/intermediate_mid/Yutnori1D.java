package com.dukcode.codetree.intermediate_low.backtracking;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Yutnori1D {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int k;

  private static int[] moves;

  private static int[] pieces;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken()) - 1;
    k = Integer.parseInt(st.nextToken());

    moves = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      moves[i] = Integer.parseInt(st.nextToken());
    }

    pieces = new int[k];

    bw.write(String.valueOf(solve(0)));

    br.close();
    bw.close();

  }

  private static int solve(int idx) {
    if (idx == n) {
      int score = 0;
      for (int pos : pieces) {
        score += pos >= m ? 1 : 0;
      }

      return score;
    }

    int ret = 0;
    int cntEnd = 0;
    for (int piece = 0; piece < k; piece++) {
      if (pieces[piece] >= m) {
        cntEnd++;
        continue;
      }
      pieces[piece] += moves[idx];
      ret = Math.max(ret, solve(idx + 1));
      pieces[piece] -= moves[idx];
    }

    ret = Math.max(ret, cntEnd);

    return ret;
  }

}

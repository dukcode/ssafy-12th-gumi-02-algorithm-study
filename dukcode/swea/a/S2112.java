package com.dukcode.swea.a;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

// 보호 필름
public class S2112 {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int h;
  private static int w;
  private static int k;

  private static int[][] film;

  private static int[] a;
  private static int[] b;

  private static int ans;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      st = new StringTokenizer(br.readLine());
      h = Integer.parseInt(st.nextToken());
      w = Integer.parseInt(st.nextToken());
      k = Integer.parseInt(st.nextToken());

      film = new int[h][w];
      for (int y = 0; y < h; ++y) {
        st = new StringTokenizer(br.readLine());
        for (int x = 0; x < w; ++x) {
          film[y][x] = Integer.parseInt(st.nextToken());
        }
      }

      a = new int[w];
      b = new int[w];
      Arrays.fill(b, 1);

      ans = MX;
      solve(0, 0);

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(ans));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static void solve(int toChange, int cnt) {
    if (toChange == h) {
      if (isOk()) {
        ans = Math.min(ans, cnt);
      }

      return;
    }

    if (cnt >= ans) {
      return;
    }

    solve(toChange + 1, cnt);

    int[] tmp = film[toChange];

    film[toChange] = a;
    solve(toChange + 1, cnt + 1);

    film[toChange] = b;
    solve(toChange + 1, cnt + 1);

    film[toChange] = tmp;
  }

  private static boolean isOk() {
    for (int x = 0; x < w; ++x) {
      if (!isColOk(x)) {
        return false;
      }
    }

    return true;
  }

  private static boolean isColOk(int x) {
    int cnt = 1;
    for (int y = 1; y < h; ++y) {
      if (film[y - 1][x] == film[y][x]) {
        cnt++;
        continue;
      }

      if (cnt >= k) {
        return true;
      }

      cnt = 1;
    }

    return cnt >= k;
  }


}

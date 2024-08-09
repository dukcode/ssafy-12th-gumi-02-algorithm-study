package com.dukcode.algospot.chap06_brute_force;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Picnic {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static boolean[][] areFriends;
  private static boolean[] taken;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      m = Integer.parseInt(st.nextToken());

      areFriends = new boolean[n][n];
      st = new StringTokenizer(br.readLine());
      for (int i = 0; i < m; i++) {
        int first = Integer.parseInt(st.nextToken());
        int second = Integer.parseInt(st.nextToken());

        areFriends[first][second] = true;
        areFriends[second][first] = true;
      }

      taken = new boolean[n];

      bw.write(String.valueOf(countPairings()));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static int countPairings() {
    int firstFree = -1;
    for (int i = 0; i < n; ++i) {
      if (!taken[i]) {
        firstFree = i;
        break;
      }
    }

    if (firstFree == -1) {
      return 1;
    }


    int ret = 0;
    for (int pairWith = firstFree + 1; pairWith < n; pairWith++) {
      if (!areFriends[firstFree][pairWith] || taken[pairWith]) {
        continue;
      }

      taken[firstFree] = true;
      taken[pairWith] = true;
      ret += countPairings();
      taken[firstFree] = false;
      taken[pairWith] = false;
    }

    return ret;
  }

}

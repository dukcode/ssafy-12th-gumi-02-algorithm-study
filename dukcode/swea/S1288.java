package com.dukcode.swea;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 * 새로운 불면증 치료법
 */
public class S1288 {


  private static BufferedReader br;
  private static BufferedWriter bw;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      int n = Integer.parseInt(br.readLine());
      bw.write(String.format("#%d %d\n", tc, solve(n)));
    }

    br.close();
    bw.close();
  }

  private static int solve(int base) {
    boolean[] appeared = new boolean[10];

    int num = base;
    int cnt = 0;
    do {
      cnt++;
      checkAppeared(appeared, num);
      num += base;
    } while (!isOver(appeared));

    return cnt * base;
  }

  private static void checkAppeared(boolean[] appeared, int num) {
    while (num > 0) {
      appeared[num % 10] = true;
      num /= 10;
    }
  }

  private static boolean isOver(boolean[] appeared) {
    for (boolean isAppeared : appeared) {
      if (!isAppeared) {
        return false;
      }
    }

    return true;
  }

}

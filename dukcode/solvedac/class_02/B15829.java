package com.dukcode.solvedac.class_02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B15829 {

  private static final long R = 31;
  private static final long MOD = 1_234_567_891;

  private static BufferedReader br;
  private static BufferedWriter bw;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int len = Integer.parseInt(br.readLine());
    String str = br.readLine();

    bw.write(String.valueOf(toHash(str)));

    br.close();
    bw.close();

  }

  private static long toHash(String str) {
    long ret = 0;

    for (int idx = str.length() - 1; idx >= 0; idx--) {
      char c = str.charAt(idx);
      ret *= R;
      ret += c - 'a' + 1;
      ret %= MOD;
    }

    return ret;
  }

}

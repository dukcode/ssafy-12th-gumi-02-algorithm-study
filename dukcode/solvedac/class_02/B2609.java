package com.dukcode.solvedac.class_02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B2609 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;


  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    int a = Integer.parseInt(st.nextToken());
    int b = Integer.parseInt(st.nextToken());

    bw.write(String.valueOf(gcd(a, b)));
    bw.newLine();
    bw.write(String.valueOf(lcm(a, b)));

    br.close();
    bw.close();

  }

  private static int lcm(int a, int b) {
    return a * b / gcd(a, b);
  }

  private static int gcd(int a, int b) {
    if (b == 0) {
      return a;
    }

    if (a < b) {
      return gcd(b, a);
    }

    return gcd(b, a % b);

  }

}

package com.dukcode.codetree.novice_mid.radix;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class TransformationOfNumberSystem {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int fromBase;
  private static int toBase;
  private static String n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    fromBase = Integer.parseInt(st.nextToken());
    toBase = Integer.parseInt(st.nextToken());

    n = br.readLine();

    String ans = changeBase(n, fromBase, toBase);
    bw.write(ans);
    br.close();
    bw.close();

  }

  private static String changeBase(String n, int from, int to) {
    int decimal = 0;
    for (char digit : n.toCharArray()) {
      decimal *= from;
      decimal += digit - '0';
    }

    StringBuilder sb = new StringBuilder();
    while (decimal > 0) {
      sb.append(decimal % to);
      decimal /= to;
    }

    sb.reverse();
    return sb.toString();
  }

}

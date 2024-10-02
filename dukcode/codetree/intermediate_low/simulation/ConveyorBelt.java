package com.dukcode.codetree.intermediate_low.simulation;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class ConveyorBelt {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int t;
  private static int[] beltA;
  private static int[] beltB;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    t = Integer.parseInt(st.nextToken());

    beltA = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      beltA[i] = Integer.parseInt(st.nextToken());
    }

    beltB = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      beltB[i] = Integer.parseInt(st.nextToken());
    }

    move(t);

    for (int i = 0; i < n; i++) {
      bw.write(String.valueOf(beltA[i]));
      bw.write(" ");
    }
    bw.newLine();

    for (int i = 0; i < n; i++) {
      bw.write(String.valueOf(beltB[i]));
      bw.write(" ");
    }
    bw.newLine();

    br.close();
    bw.close();
  }

  private static void move(int t) {
    for (int time = 0; time < t; time++) {
      int tmp = beltA[n - 1];
      for (int i = n - 1; i >= 1; --i) {
        beltA[i] = beltA[i - 1];
      }
      beltA[0] = beltB[n - 1];

      for (int i = n - 1; i >= 1; --i) {
        beltB[i] = beltB[i - 1];
      }
      beltB[0] = tmp;
    }
  }


}

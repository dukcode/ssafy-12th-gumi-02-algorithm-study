package com.dukcode.solvedac.class_02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B30802 {

  private static final int NUM_SIZE = 6;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;


  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());

    int[] numPeople = new int[NUM_SIZE];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < NUM_SIZE; i++) {
      numPeople[i] = Integer.parseInt(st.nextToken());
    }

    st = new StringTokenizer(br.readLine());
    int t = Integer.parseInt(st.nextToken());
    int p = Integer.parseInt(st.nextToken());

    int cnt = 0;
    for (int i = 0; i < NUM_SIZE; i++) {
      cnt += (numPeople[i] + t - 1) / t;
    }

    bw.write(String.valueOf(cnt));
    bw.newLine();
    bw.write(String.valueOf(n / p));
    bw.write(' ');
    bw.write(String.valueOf(n % p));

    br.close();
    bw.close();

  }

}

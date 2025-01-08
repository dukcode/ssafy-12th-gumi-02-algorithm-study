package com.dukcode.solvedac.class_01;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class B31403 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int a = Integer.parseInt(br.readLine());
    int b = Integer.parseInt(br.readLine());
    int c = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(a + b - c));
    bw.newLine();
    bw.write(String.valueOf(Integer.parseInt(String.valueOf(a) + String.valueOf(b)) - c));
    bw.newLine();

    br.close();
    bw.close();

  }

}

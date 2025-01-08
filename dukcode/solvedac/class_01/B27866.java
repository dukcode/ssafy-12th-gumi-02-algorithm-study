package com.dukcode.solvedac.class_01;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B27866 {

  private static BufferedReader br;
  private static BufferedWriter bw;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    String word = br.readLine();
    int idx = Integer.parseInt(br.readLine()) - 1;

    bw.write(word.charAt(idx));

    br.close();
    bw.close();

  }

}

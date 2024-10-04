package com.dukcode.codetree.intermediate_low.simulation;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class ShortestRunLengthEncoding {

  private static final int MX = 100;

  private static BufferedReader br;
  private static BufferedWriter bw;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    char[] word = br.readLine().toCharArray();

    int minLength = MX;
    for (int shift = 0; shift < word.length; shift++) {
      shift(word);
      minLength = Math.min(minLength, getEncodedLength(word));
    }

    bw.write(String.valueOf(minLength));

    br.close();
    bw.close();
  }

  private static int getEncodedLength(char[] word) {
    char pivot = word[0];

    StringBuilder sb = new StringBuilder();
    int num = 0;
    for (char c : word) {
      if (c == pivot) {
        num++;
        continue;
      }

      sb.append(pivot);
      sb.append(num);

      pivot = c;
      num = 1;
    }

    sb.append(pivot);
    sb.append(num);

    return sb.length();
  }

  private static void shift(char[] word) {
    char tmp = word[word.length - 1];
    for (int i = word.length - 1; i > 0; i--) {
      word[i] = word[i - 1];
    }

    word[0] = tmp;
  }


}

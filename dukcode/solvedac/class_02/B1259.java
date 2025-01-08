package com.dukcode.solvedac.class_02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B1259 {

  private static BufferedReader br;
  private static BufferedWriter bw;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    while (true) {
      String number = br.readLine();

      if (number.equals(String.valueOf(0))) {
        break;
      }

      bw.write(isPalindrome(number) ? "yes" : "no");
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static boolean isPalindrome(String number) {
    int n = number.length();

    int st = 0;
    int en = n - 1;
    while (st < en) {
      if (number.charAt(st) != number.charAt(en)) {
        return false;
      }

      st++;
      en--;
    }

    return true;
  }

}

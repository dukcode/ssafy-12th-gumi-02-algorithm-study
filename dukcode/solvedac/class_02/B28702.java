package com.dukcode.solvedac.class_02;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class B28702 {

  private static BufferedReader br;
  private static BufferedWriter bw;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    bw.write(getAns(getNumber()));

    br.close();
    bw.close();

  }

  private static int getNumber() throws IOException {
    for (int i = 0; i < 3; ++i) {
      String str = br.readLine();
      if (isNumber(str)) {
        return Integer.parseInt(str) + (3 - i);
      }
    }

    return -1;
  }

  private static boolean isNumber(String s) {
    return !s.endsWith("z");
  }

  private static String getAns(int num) {
    if (num % 3 == 0 && num % 5 == 0) {
      return "FizzBuzz";
    }

    if (num % 3 == 0) {
      return "Fizz";
    }

    if (num % 5 == 0) {
      return "Buzz";
    }

    return String.valueOf(num);
  }

}

package com.dukcode.codetree.intermediate_mid.datastructure.hashmap;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class MostFrequentData {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static HashMap<String, Integer> map;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    int ans = -1;
    map = new HashMap<>();
    for (int i = 0; i < n; i++) {
      String word = br.readLine();
      int newCount = map.getOrDefault(word, 0) + 1;
      map.put(word, newCount);
      ans = Math.max(ans, newCount);
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }


}

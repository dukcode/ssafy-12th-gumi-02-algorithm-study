package com.dukcode.codetree.intermediate_high.topology_sort.topology_sort;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class SizeComparison3 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static List<Integer>[] adj;
  private static int[] inDegrees;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    adj = new List[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
    }

    inDegrees = new int[n];
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      adj[a].add(b);
      inDegrees[b]++;
    }

    PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int i = 0; i < n; ++i) {
      if (inDegrees[i] == 0) {
        pq.add(i);
      }
    }

    List<Integer> order = new ArrayList<>();
    while (!pq.isEmpty()) {
      int here = pq.poll();
      order.add(here);
      for (int there : adj[here]) {
        inDegrees[there]--;

        if (inDegrees[there] != 0) {
          continue;
        }

        pq.offer(there);
      }
    }

    for (Integer i : order) {
      bw.write(String.valueOf(i + 1));
      bw.write(' ');
    }

    br.close();
    bw.close();
  }


}

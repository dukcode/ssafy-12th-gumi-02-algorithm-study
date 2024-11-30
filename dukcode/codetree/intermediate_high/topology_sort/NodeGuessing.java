package com.dukcode.codetree.intermediate_high.topology_sort.topology_sort;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.StringTokenizer;

public class NodeGuessing {

  private static final int NUM_ALPHABET = 26;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static String[] nodes;
  private static Map<String, Integer> strToNode;

  private static int m;

  private static List<Integer>[] adj;
  private static List<Integer>[] children;
  private static List<Integer> roots;

  private static int[] inDegrees;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    nodes = new String[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      nodes[i] = st.nextToken();
    }

    Arrays.sort(nodes);

    strToNode = new HashMap<>();
    for (int i = 0; i < n; i++) {
      strToNode.put(nodes[i], i);
    }

    adj = new List[n];
    children = new List[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
      children[i] = new ArrayList<>();
    }

    m = Integer.parseInt(br.readLine());

    inDegrees = new int[n];
    roots = new ArrayList<>();
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      String child = st.nextToken();
      String parent = st.nextToken();

      int childIdx = strToNode.get(child);
      int parentIdx = strToNode.get(parent);

      adj[parentIdx].add(childIdx);
      inDegrees[childIdx]++;
    }

    Queue<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < n; i++) {
      if (inDegrees[i] == 0) {
        q.offer(i);
        roots.add(i);
      }
    }

    while (!q.isEmpty()) {
      int here = q.poll();
      for (int there : adj[here]) {
        inDegrees[there]--;
        if (inDegrees[there] == 0) {
          q.offer(there);
          children[here].add(there);
        }
      }
    }

    for (List<Integer> child : children) {
      Collections.sort(child);
    }

    bw.write(String.valueOf(roots.size()));
    bw.newLine();
    for (int root : roots) {
      bw.write(String.valueOf(nodes[root]));
      bw.write(' ');
    }
    bw.newLine();

    for (int i = 0; i < n; i++) {
      bw.write(nodes[i]);
      bw.write(' ');
      bw.write(String.valueOf(children[i].size()));
      bw.write(' ');
      for (int child : children[i]) {
        bw.write(nodes[child]);
        bw.write(' ');
      }
      bw.newLine();
    }

    br.close();
    bw.close();
  }


}

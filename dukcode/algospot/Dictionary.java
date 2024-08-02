import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Dictionary {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static String[] words;

  private static boolean[][] adj;
  private static boolean[] vis;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());

      words = new String[n];
      for (int i = 0; i < n; ++i) {
        words[i] = br.readLine();
      }

      createGraph();

      List<Integer> order = dfsAll();

      if (order.isEmpty()) {
        bw.write("INVALID HYPOTHESIS\n");
        continue;
      }

      for (int ch : order) {
        bw.write((char) (ch + 'a'));
      }
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static void dfs(int here, List<Integer> order) {
    vis[here] = true;

    for (int there = 0; there < 26; ++there) {
      if (vis[there] || !adj[here][there]) {
        continue;
      }

      dfs(there, order);
    }

    order.add(here);
  }

  private static List<Integer> dfsAll() {
    vis = new boolean[26];

    List<Integer> order = new ArrayList<>();
    for (int i = 25; i >= 0; --i) {
      if (vis[i]) {
        continue;
      }

      dfs(i, order);
    }

    Collections.reverse(order);

    for (int i = 0; i < order.size(); ++i) {
      int from = order.get(i);
      for (int j = i + 1; j < order.size(); ++j) {
        int to = order.get(j);

        if (adj[to][from]) {
          return Collections.emptyList();
        }
      }
    }

    return order;

  }

  private static void createGraph() {
    adj = new boolean[26][26];

    for (int i = 1; i < n; ++i) {
      String before = words[i - 1];
      String after = words[i];

      int len = Math.min(before.length(), after.length());

      for (int idx = 0; idx < len; ++idx) {
        if (before.charAt(idx) != after.charAt(idx)) {
          adj[before.charAt(idx) - 'a'][after.charAt(idx) - 'a'] = true;
          break;
        }
      }
    }
  }


}

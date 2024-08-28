import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B4803 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static boolean[][] adj;

  private static int[] parent;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int t = 0;
    while (input()) {
      t++;

      init();

      int countTree = solve();

      StringBuilder sb = new StringBuilder();
      sb.append("Case ").append(t).append(": ");
      if (countTree > 1) {
        sb.append("A forest of ").append(countTree).append(" trees.");
      } else if (countTree == 1) {
        sb.append("There is one tree.");
      } else {
        sb.append("No trees.");
      }

      bw.write(sb.toString());
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static void init() {
    parent = new int[n];
    Arrays.fill(parent, -1);
  }

  private static boolean input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    if (n == 0 && m == 0) {
      return false;
    }

    adj = new boolean[n][n];
    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int first = Integer.parseInt(st.nextToken()) - 1;
      int second = Integer.parseInt(st.nextToken()) - 1;

      adj[first][second] = true;
      adj[second][first] = true;
    }

    return true;
  }

  private static boolean dfs(int here) {
    boolean ret = true;
    for (int there = 0; there < n; ++there) {
      if (there == here || !adj[here][there]) {
        continue;
      }

      if (parent[there] != -1) {
        if (there != parent[here]) {
          ret = false;
        }
        continue;
      }

      parent[there] = here;
      if (!dfs(there)) {
        ret = false;
      }

    }

    return ret;
  }

  private static int solve() {
    int countTree = 0;
    for (int start = 0; start < n; ++start) {
      if (parent[start] != -1) {
        continue;
      }

      parent[start] = start;
      if (dfs(start)) {
        countTree++;
      }
    }

    return countTree;
  }


}
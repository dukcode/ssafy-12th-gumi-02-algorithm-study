import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class GraphTraversal {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static List<Integer>[] adj;

  private static boolean[] vis;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    adj = new List[n];
    for (int i = 0; i < n; ++i) {
      adj[i] = new ArrayList<>();
    }

    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;
      adj[fr].add(to);
      adj[to].add(fr);
    }

    vis = new boolean[n];
    bw.write(String.valueOf(dfs(0) - 1));

    br.close();
    bw.close();

  }

  private static int dfs(int here) {
    vis[here] = true;

    int cnt = 1;
    for (int there : adj[here]) {
      if (vis[there]) {
        continue;
      }

      cnt += dfs(there);
    }

    return cnt;
  }

}

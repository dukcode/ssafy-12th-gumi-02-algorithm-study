import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class HeightOfFriends {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static List<Integer>[] adj;

  private static List<Integer> order;
  private static boolean[] vis;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    adj = new List[n + 1];
    for (int i = 1; i <= n; ++i) {
      adj[i] = new ArrayList<>();
    }

    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int before = Integer.parseInt(st.nextToken());
      int after = Integer.parseInt(st.nextToken());

      // 거꾸로 삽입 답이 1개임을 보장하기 때문에 가능
      adj[after].add(before);
    }

    dfsAll();

    for (int num : order) {
      bw.write(String.valueOf(num));
      bw.write(' ');
    }

    br.close();
    bw.close();

  }

  private static void dfsAll() {
    order = new ArrayList<>();
    vis = new boolean[n + 1];
    for (int here = 1; here <= n; ++here) {
      if (vis[here]) {
        continue;
      }

      dfs(here);
    }

  }

  private static void dfs(int here) {
    vis[here] = true;

    for (int there : adj[here]) {
      if (vis[there]) {
        continue;
      }

      dfs(there);
    }

    order.add(here);
  }

}

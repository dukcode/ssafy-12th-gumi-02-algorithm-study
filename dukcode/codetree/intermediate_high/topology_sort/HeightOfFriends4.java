import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class HeightOfFriends4 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static List<Integer>[] adj;

  private static int[] inDegrees;

  private static Edge[] edges;

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

    edges = new Edge[m];
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;

      edges[i] = new Edge(fr, to);
    }

    int idx = solve();

    bw.write(idx == m ? "Consistent" : String.valueOf(idx + 1));

    br.close();
    bw.close();
  }

  private static int solve() {
    int st = 0;
    int en = m;

    while (st < en) {
      int half = (st + en) / 2;
      if (!hasCycle(half)) {
        st = half + 1;
      } else {
        en = half;
      }
    }

    return st;
  }

  private static boolean hasCycle(int idx) {
    for (int i = 0; i < n; ++i) {
      adj[i] = new ArrayList<>();
    }

    inDegrees = new int[n];
    for (int i = 0; i <= idx; ++i) {
      int fr = edges[i].fr;
      int to = edges[i].to;

      adj[fr].add(to);
      inDegrees[to]++;
    }

    Queue<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < n; ++i) {
      if (inDegrees[i] == 0) {
        q.offer(i);
      }
    }

    boolean[] visited = new boolean[n];
    int visCount = 0;
    Loop:
    while (!q.isEmpty()) {
      int here = q.poll();
      visited[here] = true;
      visCount++;
      for (int there : adj[here]) {
        if (visited[there]) {
          break Loop;
        }

        inDegrees[there]--;

        if (inDegrees[there] != 0) {
          continue;
        }

        q.offer(there);
      }
    }

    return visCount != n;
  }

  private static class Edge {

    int fr;
    int to;

    public Edge(int fr, int to) {
      this.fr = fr;
      this.to = to;
    }
  }

}

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

public class DetectCycle {

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
    for (int i = 0; i < n; ++i) {
      adj[i] = new ArrayList<>();
    }

    inDegrees = new int[n];
    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;
      adj[fr].add(to);
      inDegrees[to]++;
    }

    Queue<Integer> q = new ArrayDeque<>();
    boolean[] vis = new boolean[n];
    for (int i = 0; i < n; ++i) {
      if (inDegrees[i] == 0) {
        q.offer(i);
        vis[i] = true;
      }
    }

    boolean hasCycle = false;
    Loop:
    while (!q.isEmpty()) {
      int here = q.poll();
      for (int there : adj[here]) {
        if (vis[there]) {
          hasCycle = true;
          break Loop;
        }

        inDegrees[there]--;
        if (inDegrees[there] != 0) {
          continue;
        }

        q.offer(there);
        vis[there] = true;
      }
    }

    for (int i = 0; i < n; ++i) {
      if (!vis[i]) {
        hasCycle = true;
        break;
      }
    }

    bw.write(hasCycle ? "Exists" : "Not Exists");

    br.close();
    bw.close();
  }


}

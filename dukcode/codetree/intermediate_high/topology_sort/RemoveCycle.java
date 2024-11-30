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

public class RemoveCycle {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m1;
  private static int m2;

  private static List<Integer>[] adj;

  private static int[] inDegrees;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m1 = Integer.parseInt(st.nextToken());
    m2 = Integer.parseInt(st.nextToken());

    adj = new List[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
    }

    inDegrees = new int[n];
    for (int i = 0; i < m1; ++i) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;

      adj[fr].add(to);
      inDegrees[to]++;
    }

    for (int i = 0; i < m2; ++i) {
      st = new StringTokenizer(br.readLine());
    }

    Queue<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < n; ++i) {
      if (inDegrees[i] == 0) {
        q.offer(i);
      }
    }

    boolean[] visited = new boolean[n];
    int cntVis = 0;
    Loop:
    while (!q.isEmpty()) {
      int here = q.poll();
      visited[here] = true;
      cntVis++;

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

    bw.write(cntVis == n ? "Yes" : "No");

    br.close();
    bw.close();
  }


}

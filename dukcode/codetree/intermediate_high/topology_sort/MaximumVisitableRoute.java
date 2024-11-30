import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class MaximumVisitableRoute {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static List<Integer>[] adj;
  private static int[] inDegrees;

  private static int[] dist;
  private static int[] before;

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

      adj[to].add(fr);
      inDegrees[fr]++;
    }

    dist = new int[n];
    Arrays.fill(dist, -1);
    dist[n - 1] = 0;
    before = new int[n];
    Arrays.fill(before, -1);

    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; ++i) {
      if (inDegrees[i] == 0) {
        q.offer(i);
      }
    }

    while (!q.isEmpty()) {
      int here = q.poll();
      for (int there : adj[here]) {
        if (dist[here] != -1) {
          if (dist[here] + 1 > dist[there]) {
            dist[there] = dist[here] + 1;
            before[there] = here;
          } else if (dist[here] + 1 == dist[there] && before[there] > here) {
            before[there] = here;
          }
        }

        inDegrees[there]--;
        if (inDegrees[there] == 0) {
          q.offer(there);
        }
      }
    }

    if (dist[0] == -1) {
      bw.write("-1");
    } else {
      List<Integer> order = new ArrayList<>();
      int cur = 0;
      order.add(cur);
      while (cur != n - 1) {
        cur = before[cur];
        order.add(cur);
      }

      bw.write(String.valueOf(order.size()));
      bw.newLine();
      for (Integer i : order) {
        bw.write(String.valueOf(i + 1));
        bw.write(' ');
      }

    }

    br.close();
    bw.close();
  }


}

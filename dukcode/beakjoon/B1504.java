import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.AbstractMap.SimpleEntry;
import java.util.Arrays;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class B1504 {

  // INF 값이 최대 3번까지 더해질 수 있음 따라서 21억 / 3보다 작은 값으로 잡음
  private static final int INF = 600_000_000;
  private static final int MX = 200_000_000;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int e;

  private static int[][] adj;

  private static int v1;
  private static int v2;


  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    int ans = solve();
    output(ans);

    br.close();
    bw.close();
  }

  private static void output(int ans) throws IOException {
    bw.write(String.valueOf(ans));
  }

  private static int[] dijkstra(int start) {
    int[] dist = new int[n];
    Arrays.fill(dist, INF);

    PriorityQueue<Entry<Integer, Integer>> pq = new PriorityQueue<>(
        (a, b) -> a.getKey() == b.getKey() ? a.getValue() - b.getValue() : a.getKey() - b.getKey());

    pq.offer(new SimpleEntry<>(0, start));
    dist[start] = 0;

    while (!pq.isEmpty()) {
      Entry<Integer, Integer> cur = pq.poll();
      int here = cur.getValue();
      int hereDist = cur.getKey();

      if (dist[here] > hereDist) {
        continue;
      }

      for (int there = 0; there < n; ++there) {
        if (adj[here][there] == -1) {
          continue;
        }

        int thereDist = hereDist + adj[here][there];

        if (dist[there] <= thereDist) {
          continue;
        }

        pq.offer(new SimpleEntry<>(thereDist, there));
        dist[there] = thereDist;
      }
    }

    return dist;
  }

  private static int solve() {
    int[] dist0 = dijkstra(0);
    int[] distV1 = dijkstra(v1);
    int[] distV2 = dijkstra(v2);

    int ret = Math.min(dist0[v1] + distV1[v2] + distV2[n - 1],
        dist0[v2] + distV2[v1] + distV1[n - 1]);
    return ret > MX ? -1 : ret;
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    e = Integer.parseInt(st.nextToken());

    adj = new int[n][n];
    for (int i = 0; i < n; i++) {
      Arrays.fill(adj[i], -1);
    }

    for (int i = 0; i < e; ++i) {
      st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;
      int d = Integer.parseInt(st.nextToken());
      adj[from][to] = d;
      adj[to][from] = d;
    }

    st = new StringTokenizer(br.readLine());
    v1 = Integer.parseInt(st.nextToken()) - 1;
    v2 = Integer.parseInt(st.nextToken()) - 1;
  }


}

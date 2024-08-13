import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class B11779 {
  private static final long MX = Long.MAX_VALUE / 2;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static List<Entry<Integer, Integer>>[] adj;

  private static int s;
  private static int e;

  private static long[] dist;
  private static int[] parent;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    init();
    solve();
    output();

    br.close();
    bw.close();
  }

  private static void output() throws IOException {
    bw.write(String.valueOf(dist[e]));
    bw.newLine();

    int i = e;
    List<Integer> order = new ArrayList<>();
    while (parent[i] != i) {
      order.add(i);
      i = parent[i];
    }
    order.add(i);

    Collections.reverse(order);

    bw.write(String.valueOf(order.size()));
    bw.newLine();

    for (int v : order) {
      bw.write(String.valueOf(v + 1));
      bw.write(' ');
    }

    bw.newLine();
  }

  private static void solve() {
    // dist, v
    PriorityQueue<Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> {
      if (a.getKey() == b.getKey()) {
        return a.getValue() - b.getValue();
      }

      return a.getKey() - b.getKey();
    });

    pq.offer(new SimpleEntry<>(0, s));
    dist[s] = 0;
    parent[s] = s;

    while (!pq.isEmpty()) {
      Entry<Integer, Integer> cur = pq.poll();
      int here = cur.getValue();
      int hereDist = cur.getKey();

      if (hereDist > dist[here]) {
        continue;
      }

      for (Entry<Integer, Integer> next : adj[here]) {
        int there = next.getValue();
        int thereDist = next.getKey() + hereDist;

        if (thereDist >= dist[there]) {
          continue;
        }

        pq.offer(new SimpleEntry<>(thereDist, there));
        dist[there] = thereDist;
        parent[there] = here;
      }
    }
  }

  private static void init() {
    dist = new long[n];
    Arrays.fill(dist, MX);

    parent = new int[n];
    Arrays.fill(parent, -1);
  }

  private static void input() throws IOException {
    n = Integer.parseInt(br.readLine());
    m = Integer.parseInt(br.readLine());

    adj = new ArrayList[n];
    for (int i = 0; i < n; i++) {
      adj[i] = new ArrayList<>();
    }

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());

      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;
      int cost = Integer.parseInt(st.nextToken());

      adj[fr].add(new SimpleEntry<>(cost, to));
    }

    st = new StringTokenizer(br.readLine());
    s = Integer.parseInt(st.nextToken()) - 1;
    e = Integer.parseInt(st.nextToken()) - 1;
  }


}

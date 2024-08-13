import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class B1753 {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int v;
  private static int e;
  private static int k;

  private static List<Map.Entry<Integer, Integer>>[] adj; // (cost, v)
  private static int[] dist;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    v = Integer.parseInt(st.nextToken());
    e = Integer.parseInt(st.nextToken());

    adj = new ArrayList[v];
    for (int i = 0; i < v; ++i) {
      adj[i] = new ArrayList<>();
    }

    k = Integer.parseInt(br.readLine()) - 1;

    for (int i = 0; i < e; ++i) {
      st = new StringTokenizer(br.readLine());
      int u = Integer.parseInt(st.nextToken()) - 1;
      int v = Integer.parseInt(st.nextToken()) - 1;
      int w = Integer.parseInt(st.nextToken());

      adj[u].add(new SimpleEntry<>(w, v));
    }

    dist = new int[v];
    Arrays.fill(dist, MX);

    PriorityQueue<Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> {
      if (a.getKey() == b.getKey()) {
        return a.getValue() - b.getValue();
      }

      return a.getKey() - b.getKey();
    });

    pq.offer(new SimpleEntry<>(0, k)); // (dist, v)
    dist[k] = 0;

    while (!pq.isEmpty()) {
      Entry<Integer, Integer> cur = pq.poll();
      int cost = cur.getKey();
      int here = cur.getValue();

      if (dist[here] < cost) {
        continue;
      }

      for (Entry<Integer, Integer> next : adj[here]) {
        int nextDist = next.getKey() + cost;
        int there = next.getValue();

        if (dist[there] < nextDist) {
          continue;
        }

        dist[there] = nextDist;
        pq.offer(new SimpleEntry<>(nextDist, there));
      }
    }

    for (int i = 0; i < v; ++i) {
      int d = dist[i];
      bw.write(d == MX ? "INF" : String.valueOf(d));
      bw.newLine();
    }

    br.close();
    bw.close();
  }


}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Routing {

  private static final double MX = Double.MAX_VALUE / 2.0;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static List<Entry<Double, Integer>>[] adj;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      m = Integer.parseInt(st.nextToken());

      adj = new List[n];
      for (int i = 0; i < n; ++i) {
        adj[i] = new ArrayList<>();
      }

      for (int i = 0; i < m; ++i) {
        st = new StringTokenizer(br.readLine());
        int fr = Integer.parseInt(st.nextToken());
        int to = Integer.parseInt(st.nextToken());
        double cost = Double.parseDouble(st.nextToken());

        adj[fr].add(new SimpleEntry<>(Math.log(cost), to));
      }

      double[] dist = dijkstra(0);
      double ans = Math.exp(dist[n - 1]);

      bw.write(String.format("%.10f", ans));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static double[] dijkstra(int src) {
    double[] dist = new double[n];
    Arrays.fill(dist, MX);

    PriorityQueue<Entry<Double, Integer>> pq = new PriorityQueue<>(
        (a, b) -> a.getKey().equals(b.getKey()) ?
            Integer.compare(a.getValue(), b.getValue()) :
            Double.compare(a.getKey(), b.getKey()));

    dist[src] = 0.0;
    pq.add(new SimpleEntry<>(0.0, src));

    while (!pq.isEmpty()) {
      Entry<Double, Integer> cur = pq.poll();
      double costHere = cur.getKey();
      int here = cur.getValue();

      for (Entry<Double, Integer> next : adj[here]) {
        double costNext = next.getKey() + costHere;
        int there = next.getValue();
        if (dist[there] < costNext) {
          continue;
        }

        dist[there] = costNext;
        pq.add(new SimpleEntry<>(costNext, there));
      }
    }

    return dist;
  }

}
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

public class FireTrucks {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int v;
  private static int e;
  private static int n;
  private static int m;

  private static List<Entry<Integer, Integer>>[] adj;

  private static int[] fireLocations;
  private static int[] fireStations;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {

      st = new StringTokenizer(br.readLine());
      v = Integer.parseInt(st.nextToken());
      e = Integer.parseInt(st.nextToken());
      n = Integer.parseInt(st.nextToken());
      m = Integer.parseInt(st.nextToken());

      adj = new List[v];
      for (int i = 0; i < v; ++i) {
        adj[i] = new ArrayList<>();
      }

      for (int i = 0; i < e; ++i) {
        st = new StringTokenizer(br.readLine());
        int fr = Integer.parseInt(st.nextToken()) - 1;
        int to = Integer.parseInt(st.nextToken()) - 1;
        int cost = Integer.parseInt(st.nextToken());

        adj[fr].add(new SimpleEntry<>(cost, to));
        adj[to].add(new SimpleEntry<>(cost, fr));
      }

      st = new StringTokenizer(br.readLine());
      fireLocations = new int[n];
      for (int i = 0; i < n; ++i) {
        fireLocations[i] = Integer.parseInt(st.nextToken()) - 1;
      }

      st = new StringTokenizer(br.readLine());
      fireStations = new int[m];
      for (int i = 0; i < m; ++i) {
        fireStations[i] = Integer.parseInt(st.nextToken()) - 1;
      }

      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int solve() {

    int[] dist = new int[v];
    Arrays.fill(dist, MX);

    PriorityQueue<Entry<Integer, Integer>> pq = new PriorityQueue<>(
        (a, b) -> a.getKey().equals(b.getKey()) ?
            a.getValue() - b.getValue() :
            a.getKey() - b.getKey()
    );

    for (int i = 0; i < m; ++i) {
      pq.offer(new SimpleEntry<>(0, fireStations[i]));
      dist[fireStations[i]] = 0;
    }

    while (!pq.isEmpty()) {
      Entry<Integer, Integer> cur = pq.poll();
      int distHere = cur.getKey();
      int here = cur.getValue();

      for (Entry<Integer, Integer> next : adj[here]) {
        int distThere = distHere + next.getKey();
        int there = next.getValue();

        if (dist[there] <= distThere) {
          continue;
        }

        dist[there] = distThere;
        pq.offer(new SimpleEntry<>(distThere, there));
      }
    }

    int ret = 0;
    for (int i = 0; i < n; ++i) {
      ret += dist[fireLocations[i]];
    }

    return ret;
  }

}
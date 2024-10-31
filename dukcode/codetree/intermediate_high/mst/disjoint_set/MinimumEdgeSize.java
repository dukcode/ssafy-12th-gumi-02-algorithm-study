import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class MinimumEdgeSize {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int a;
  private static int b;

  private static Edge[] edges;

  private static int[] parent;
  private static int[] height;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    a = Integer.parseInt(st.nextToken()) - 1;
    b = Integer.parseInt(st.nextToken()) - 1;

    edges = new Edge[m];

    parent = IntStream.range(0, n).toArray();
    height = new int[n];

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;
      int dist = Integer.parseInt(st.nextToken());

      edges[i] = new Edge(fr, to, dist);
    }

    Arrays.sort(edges, (e1, e2) -> Integer.compare(e2.dist, e1.dist));

    int ans = -1;
    for (int i = 0; i < m; i++) {
      Edge e = edges[i];
      union(e.fr, e.to);

      if (findRoot(a) == findRoot(b)) {
        ans = e.dist;
        break;
      }
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static void union(int a, int b) {
    int rootA = findRoot(a);
    int rootB = findRoot(b);

    if (rootA == rootB) {
      return;
    }

    if (height[rootA] > height[rootB]) {
      parent[rootB] = rootA;
      return;
    } else if (height[rootA] < height[rootB]) {
      parent[rootA] = rootB;
      return;
    }

    parent[rootA] = rootB;
    height[rootB]++;
  }

  private static int findRoot(int x) {
    if (parent[x] == x) {
      return x;
    }

    return parent[x] = findRoot(parent[x]);
  }

  private static class Edge {

    int fr;
    int to;
    int dist;

    public Edge(int fr, int to, int dist) {
      this.fr = fr;
      this.to = to;
      this.dist = dist;
    }
  }
}

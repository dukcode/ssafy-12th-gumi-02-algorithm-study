import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class ConnectWithTheMostVertices {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int k;

  private static int[] minCosts;

  private static int[] parents;
  private static int[] heights;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    minCosts = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      minCosts[i] = Integer.parseInt(st.nextToken());
    }

    parents = IntStream.range(0, n).toArray();
    heights = new int[n];
    Arrays.fill(heights, 1);

    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int fr = Integer.parseInt(st.nextToken()) - 1;
      int to = Integer.parseInt(st.nextToken()) - 1;

      union(fr, to);
    }

    List<Integer> groupCosts = new ArrayList<>();
    boolean[] vis = new boolean[n];
    for (int i = 0; i < n; ++i) {
      int root = findRoot(i);

      if (vis[root]) {
        continue;
      }

      groupCosts.add(minCosts[root]);
      vis[root] = true;
    }

    groupCosts.sort(Comparator.naturalOrder());
    int ans = 0;
    for (int i = 1; i < groupCosts.size(); ++i) {
      ans += groupCosts.get(0) + groupCosts.get(i);
    }

    bw.write(ans > k ? "NO" : String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static int findRoot(int x) {
    if (parents[x] == x) {
      return x;
    }

    return parents[x] = findRoot(parents[x]);
  }

  private static void union(int a, int b) {
    int rootA = findRoot(a);
    int rootB = findRoot(b);

    if (rootA == rootB) {
      return;
    }

    int minCost = Math.min(minCosts[rootA], minCosts[rootB]);

    if (heights[rootA] > heights[rootB]) {
      parents[rootB] = rootA;
      minCosts[rootA] = minCost;
      return;
    } else if (heights[rootA] < heights[rootB]) {
      parents[rootA] = rootB;
      minCosts[rootB] = minCost;
      return;
    }

    parents[rootA] = rootB;
    minCosts[rootB] = minCost;
    heights[rootB]++;
  }

}

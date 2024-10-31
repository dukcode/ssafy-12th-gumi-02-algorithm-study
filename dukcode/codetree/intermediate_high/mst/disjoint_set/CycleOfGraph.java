import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class CycleOfGraph {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] parent;
  private static int[] rank;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    parent = IntStream.range(0, n).toArray();
    rank = new int[n];

    int ans = -1;
    for (int i = 1; i <= m; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      int rootA = findRoot(a);
      int rootB = findRoot(b);
      if (rootA == rootB) {
        ans = i;
        break;
      }

      union(rootA, rootB);
    }

    bw.write(ans == -1 ? "happy" : String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static void union(int a, int b) {
    if (rank[a] > rank[b]) {
      parent[b] = a;
      return;
    } else if (rank[a] < rank[b]) {
      parent[a] = b;
      return;
    }

    parent[a] = b;
    rank[b]++;
  }

  private static int findRoot(int x) {
    if (parent[x] == x) {
      return x;
    }

    return parent[x] = findRoot(parent[x]);
  }

}

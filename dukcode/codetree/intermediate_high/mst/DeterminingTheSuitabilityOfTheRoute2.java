import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class DeterminingTheSuitabilityOfTheRoute2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int k;

  private static int[] parent;
  private static int[] height;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    parent = IntStream.range(0, n).toArray();
    height = new int[n];
    Arrays.fill(height, 1);

    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      union(a, b);
    }

    boolean ok = true;
    st = new StringTokenizer(br.readLine());
    int before = Integer.parseInt(st.nextToken()) - 1;
    for (int i = 1; i < k; ++i) {
      int now = Integer.parseInt(st.nextToken()) - 1;
      if (findRoot(before) != findRoot(now)) {
        ok = false;
        break;
      }
      before = now;
    }

    bw.write(String.valueOf(ok ? 1 : 0));

    br.close();
    bw.close();

  }

  private static void union(int a, int b) {
    int rootA = findRoot(a);
    int rootB = findRoot(b);

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

    int rootX = findRoot(parent[x]);
    parent[x] = rootX;
    return rootX;
  }
}

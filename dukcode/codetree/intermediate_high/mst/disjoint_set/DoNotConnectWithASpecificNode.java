import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class DoNotConnectWithASpecificNode {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int a;
  private static int b;
  private static int k;

  private static int[] parent;
  private static int[] height;
  private static int[] size;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    parent = IntStream.range(0, n).toArray();
    height = new int[n];
    Arrays.fill(height, 1);
    size = new int[n];
    Arrays.fill(size, 1);

    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      union(a, b);
    }

    st = new StringTokenizer(br.readLine());
    a = Integer.parseInt(st.nextToken()) - 1;
    b = Integer.parseInt(st.nextToken()) - 1;
    k = Integer.parseInt(st.nextToken());

    int rootA = findRoot(a);
    int rootB = findRoot(b);

    List<Integer> sizes = new ArrayList<>();
    boolean[] vis = new boolean[n];
    for (int i = 0; i < n; ++i) {
      int rootI = findRoot(i);

      if (rootI == rootA || rootI == rootB) {
        continue;
      }

      if (vis[rootI]) {
        continue;
      }

      sizes.add(size[rootI]);
      vis[rootI] = true;
    }

    sizes.sort(Collections.reverseOrder());
    int ans = size[rootA];
    for (int i = 0; i < Math.min(k, sizes.size()); ++i) {
      ans += sizes.get(i);
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
      size[rootA] += size[rootB];
      return;
    } else if (height[rootA] < height[rootB]) {
      parent[rootA] = rootB;
      size[rootB] += size[rootA];
      return;
    }

    parent[rootA] = rootB;
    size[rootB] += size[rootA];
    height[rootB]++;
  }

  private static int findRoot(int x) {
    if (parent[x] == x) {
      return x;
    }

    return parent[x] = findRoot(parent[x]);
  }

  private static class Size {

    int idx;
    int size;

    public Size(int idx, int size) {
      this.idx = idx;
      this.size = size;
    }
  }
}

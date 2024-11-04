import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class RedTeamAndWhiteTeam {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] parent;
  private static int[] height;
  private static int[] against;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    parent = IntStream.range(0, n).toArray();
    height = new int[n];
    Arrays.fill(height, 1);
    against = new int[n];
    Arrays.fill(against, -1);

    boolean ans = true;
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      if (!beta(a, b)) {
        ans = false;
        break;
      }
    }

    bw.write(String.valueOf(ans ? 1 : 0));

    br.close();
    bw.close();

  }

  private static boolean beta(int a, int b) {
    int rootA = findRoot(a);
    int rootB = findRoot(b);

    if (rootA == rootB) {
      return false;
    }

    if (against[rootA] != -1) {
      union(against[rootA], rootB);
    }

    if (against[rootB] != -1) {
      union(against[rootB], rootA);
    }

    rootA = findRoot(rootA);
    rootB = findRoot(rootB);

    against[rootA] = rootB;
    against[rootB] = rootA;

    return true;
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

    parent[rootB] = rootA;
    height[rootA] += 1;
  }

  private static int findRoot(int x) {
    if (parent[x] == x) {
      return x;
    }

    return parent[x] = findRoot(parent[x]);
  }


}

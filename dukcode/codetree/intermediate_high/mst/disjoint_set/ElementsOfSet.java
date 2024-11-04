import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class ElementsOfASet {

  private static final int UNION = 0;
  private static final int IN_SAME_SET = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] parent;
  private static int[] height;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    parent = IntStream.range(0, n).toArray();
    height = new int[n];
    Arrays.fill(height, 1);

    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      int command = Integer.parseInt(st.nextToken());
      int a = Integer.parseInt(st.nextToken()) - 1;
      int b = Integer.parseInt(st.nextToken()) - 1;

      if (command == UNION) {
        union(a, b);
        continue;
      } else {
        bw.write(String.valueOf(areInSameSet(a, b) ? 1 : 0));
        bw.newLine();
      }


    }

    br.close();
    bw.close();

  }

  private static void union(int a, int b) {
    int rootA = findRoot(a);
    int rootB = findRoot(b);

    if (rootA == rootB) {
      return;
    }

    if (height[rootA] < height[rootB]) {
      parent[rootA] = rootB;
      return;
    } else if (height[rootA] > height[rootB]) {
      parent[rootB] = rootA;
      return;
    }

    parent[rootA] = rootB;
    height[rootB]++;
  }

  private static int findRoot(int x) {
    if (parent[x] == x) {
      return x;
    }

    int root = findRoot(parent[x]);
    parent[x] = root;

    return root;
  }

  private static boolean areInSameSet(int a, int b) {
    return findRoot(a) == findRoot(b);
  }

}

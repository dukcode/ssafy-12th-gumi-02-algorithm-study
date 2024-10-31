import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class ConnectedVertex {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

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

    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < m; i++) {
      st = new StringTokenizer(br.readLine());
      String command = st.nextToken();

      switch (command) {
        case "x":
          int a = Integer.parseInt(st.nextToken()) - 1;
          int b = Integer.parseInt(st.nextToken()) - 1;
          union(a, b);
          break;
        case "y":
          int x = Integer.parseInt(st.nextToken()) - 1;
          sb.append(size[findRoot(x)]);
          sb.append("\n");
        default:
          break;
      }
    }

    bw.write(sb.toString());

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

}

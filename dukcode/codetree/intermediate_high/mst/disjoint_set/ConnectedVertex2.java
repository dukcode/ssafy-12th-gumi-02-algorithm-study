import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class ConnectedVertex2 {

  private static final int MX = 100_000;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static int[] parent;
  private static int[] rank;
  private static int[] size;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    parent = IntStream.rangeClosed(0, MX).toArray();
    size = new int[MX + 1];
    Arrays.fill(size, 1);

    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      int rootA = findRoot(a);
      int rootB = findRoot(b);

      if (rootA != rootB) {
        parent[rootA] = rootB;
        size[rootB] += size[rootA];
      }

      bw.write(String.valueOf(size[rootB]));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int findRoot(int x) {
    if (parent[x] == x) {
      return x;
    }

    return parent[x] = findRoot(parent[x]);
  }


}

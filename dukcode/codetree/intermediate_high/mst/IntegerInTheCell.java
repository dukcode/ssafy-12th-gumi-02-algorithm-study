import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class IntegerInTheCell {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] parent;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    m = Integer.parseInt(br.readLine());

    parent = IntStream.rangeClosed(0, n).toArray();

    int ans = m;
    for (int i = 1; i <= m; i++) {
      int x = Integer.parseInt(br.readLine());

      int root = findRoot(x);

      if (root == 0) {
        ans = i - 1;
        break;
      }

      int beforeEmpty = findRoot(root - 1);
      parent[root] = beforeEmpty;
    }

    bw.write(String.valueOf(ans));

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

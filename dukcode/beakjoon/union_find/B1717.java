import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class B1717 {

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

    parent = IntStream.rangeClosed(0, n).toArray();

    height = new int[n + 1];
    Arrays.fill(height, 1);

    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int command = Integer.parseInt(st.nextToken());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      if (command == 1) {
        bw.write(find(a) == find(b) ? "YES" : "NO");
        bw.newLine();
        continue;
      }

      union(a, b);
    }

    br.close();
    bw.close();

  }

  private static void union(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) {
      return;
    }

    if (height[a] < height[b]) {
      parent[a] = b;
    } else if (height[a] > height[b]) {
      parent[b] = a;
    } else {
      parent[a] = b;
      height[b]++;
    }
  }

  private static int find(int e) {
    if (parent[e] == e) {
      return e;
    }

    return parent[e] = find(parent[e]);
  }

}

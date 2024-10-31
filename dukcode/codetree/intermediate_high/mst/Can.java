import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Can {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] parent;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    parent = IntStream.rangeClosed(0, n).toArray();
    int cnt = n;
    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());

      while (true) {
        a = findRoot(a);

        if (a >= b) {
          break;
        }

        parent[a] = a + 1;
        a++;
        cnt--;
      }

      bw.write(String.valueOf(cnt));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int findRoot(int x) {
    if (parent[x] == x) {
      return x;
    }

    return parent[x] = findRoot(x);
  }


}

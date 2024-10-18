import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Knapsack2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static Jewel[] jewels;

  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    jewels = new Jewel[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int w = Integer.parseInt(st.nextToken());
      int v = Integer.parseInt(st.nextToken());
      jewels[i] = new Jewel(w, v);
    }

    cache = new int[m + 1];
    Arrays.fill(cache, -1);

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = 0;
    for (int i = 0; i <= m; i++) {
      ret = Math.max(ret, solve(i));
    }

    return ret;
  }

  private static int solve(int w) {
    if (w == 0) {
      return 0;
    }

    if (cache[w] != -1) {
      return cache[w];
    }

    for (Jewel jewel : jewels) {
      if (w - jewel.w < 0) {
        continue;
      }
      cache[w] = Math.max(cache[w], solve(w - jewel.w) + jewel.v);
    }

    return cache[w];
  }

  private static class Jewel {

    int w;
    int v;

    public Jewel(int w, int v) {
      this.w = w;
      this.v = v;
    }
  }


}

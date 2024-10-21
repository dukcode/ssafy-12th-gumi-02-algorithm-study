import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

// 메모리 초과
public class GainExpQuickly_2 {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[] e;
  private static int[] t;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    e = new int[n];
    t = new int[n];
    for (int i = 0; i < n; ++i) {
      st = new StringTokenizer(br.readLine());
      e[i] = Integer.parseInt(st.nextToken());
      t[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[n][m + 1];
    for (int y = 0; y < n; ++y) {
      Arrays.fill(cache[y], -1);
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = solve(0, 0);
    return ret >= MX ? -1 : ret;
  }

  private static int solve(int idx, int exp) {
    if (exp >= m) {
      return 0;
    }

    if (idx == n) {
      return MX;
    }

    if (cache[idx][exp] != -1) {
      return cache[idx][exp];
    }

    return cache[idx][exp] = Math.min(solve(idx + 1, exp),
        solve(idx + 1, exp + e[idx]) + t[idx]);
  }

}

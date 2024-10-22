import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class NumberWar {

  private static final int MN = -987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] a;
  private static int[] b;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    a = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      a[i] = Integer.parseInt(st.nextToken());
    }

    b = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      b[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[n][n];
    for (int y = 0; y < n; y++) {
      Arrays.fill(cache[y], -1);
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    solve(0, 0);
    int ret = -1;
    for (int i = 0; i < n; i++) {
      ret = Math.max(ret, cache[i][0] == -1 ? ret : cache[i][0]);
      ret = Math.max(ret, cache[0][i] == -1 ? ret : cache[0][i]);
    }

    return ret;
  }

  private static int solve(int aIdx, int bIdx) {
    if (aIdx >= n || bIdx >= n) {
      return 0;
    }

    if (cache[aIdx][bIdx] != -1) {
      return cache[aIdx][bIdx];
    }

    int ret = solve(aIdx + 1, bIdx + 1);

    if (a[aIdx] < b[bIdx]) {
      ret = Math.max(ret, solve(aIdx + 1, bIdx));
    } else if (a[aIdx] > b[bIdx]) {
      ret = Math.max(ret, solve(aIdx, bIdx + 1) + b[bIdx]);
    }

    return cache[aIdx][bIdx] = ret;
  }


}

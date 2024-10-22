import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SecretOfAncientTreasure {

  private static final int UNUSED = Integer.MAX_VALUE;
  private static final int MN = -987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;

  private static int[] arr;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[n][k + 1];
    for (int i = 0; i < n; i++) {
      Arrays.fill(cache[i], UNUSED);
    }
    solve(0, -1);
    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = MN;
    for (int i = 0; i < n; i++) {
      for (int cntNegative = 0; cntNegative <= k; cntNegative++) {
        ret = Math.max(ret, solve(i, cntNegative));
      }
    }
    return ret;
  }

  private static int solve(int i, int cntNegative) {
    if (i == -1) {
      return k == 0 ? 0 : MN;
    }

    if (cntNegative < 0) {
      return MN;
    }

    if (cache[i][cntNegative] != UNUSED) {
      return cache[i][cntNegative];
    }

    return cache[i][cntNegative] =
        arr[i] + Math.max(0, solve(i - 1, cntNegative - (arr[i] < 0 ? 1 : 0)));
  }


}

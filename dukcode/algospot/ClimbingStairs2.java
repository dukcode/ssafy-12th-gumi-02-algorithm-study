import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class ClimbingStairs2 {

  private static final int MN = -987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] coins;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    coins = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      coins[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[n][4];
    for (int y = 0; y < n; ++y) {
      Arrays.fill(cache[y], -1);
    }

    int ans = solve(n - 1, 3);
    bw.write(String.valueOf(ans < 0 ? -1 : ans));

    br.close();
    bw.close();
  }

  private static int solve(int idx, int remain) {
    if (remain < 0) {
      return MN;
    }

    if (idx == -1) {
      return 0;
    }

    if (idx < -1) {
      return MN;
    }

    if (cache[idx][remain] != -1) {
      return cache[idx][remain];
    }

    int ret = MN;
    ret = Math.max(ret, solve(idx - 1, remain - 1) + coins[idx]);
    ret = Math.max(ret, solve(idx - 2, remain) + coins[idx]);

    return cache[idx][remain] = ret;
  }

}

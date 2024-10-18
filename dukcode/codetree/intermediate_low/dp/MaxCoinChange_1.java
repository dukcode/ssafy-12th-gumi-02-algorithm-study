import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaxCoinChange_1 {

  private static final int UNUSED = -1;
  private static final int IMPOSSIBLE = -2;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[] coins;

  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    coins = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      coins[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[m + 1];
    Arrays.fill(cache, UNUSED);
    cache[0] = 0;

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = solve(m);
    return ret == IMPOSSIBLE ? -1 : ret;
  }

  private static int solve(int sum) {
    if (sum == 0) {
      return 0;
    }

    if (cache[sum] != UNUSED) {
      return cache[sum];
    }

    int ret = IMPOSSIBLE;
    for (int coin : coins) {
      if (sum - coin < 0) {
        continue;
      }

      int before = solve(sum - coin);

      if (before == IMPOSSIBLE) {
        continue;
      }

      ret = Math.max(ret, before + 1);

    }

    return cache[sum] = ret;
  }


}

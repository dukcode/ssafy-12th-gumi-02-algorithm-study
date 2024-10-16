import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaxCoinChange {

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
    Arrays.fill(cache, -1);
    cache[0] = 0;

    for (int sum = 1; sum <= m; sum++) {
      for (int coin : coins) {
        if (sum - coin < 0) {
          continue;
        }

        if (cache[sum - coin] == -1) {
          continue;
        }
        cache[sum] = Math.max(cache[sum], cache[sum - coin] + 1);
      }
    }

    bw.write(String.valueOf(cache[m]));

    br.close();
    bw.close();
  }


}

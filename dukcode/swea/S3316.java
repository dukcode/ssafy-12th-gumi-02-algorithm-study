import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 동아리실 관리하기
public class S3316 {

  private static final int MOD = 1_000_000_007;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;
  private static char[] admins;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; ++tc) {
      admins = br.readLine().toCharArray();

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int solve() {
    int n = admins.length;
    int[][] dp = new int[n + 1][16];
    dp[0][1] = 1;

    for (int i = 1; i <= n; ++i) {

      int admin = (1 << (admins[i - 1] - 'A'));

      for (int before = 1; before < (1 << 4); ++before) {
        for (int now = 1; now < (1 << 4); ++now) {

          if ((now & admin) == 0 || (before & now) == 0) {
            continue;
          }

          dp[i][now] += dp[i - 1][before];
          dp[i][now] %= MOD;
        }
      }

    }

    int ret = 0;
    for (int perm = 1; perm < (1 << 4); perm++) {
      ret += dp[n][perm];
      ret %= MOD;
    }

    return ret;
  }

}

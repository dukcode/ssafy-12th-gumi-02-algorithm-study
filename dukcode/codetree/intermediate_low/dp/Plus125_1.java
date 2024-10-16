import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Plus125_1 {

  private static final int MOD = 10007;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    cache = new int[n + 1];
    Arrays.fill(cache, -1);

    bw.write(String.valueOf(solve(n)));

    br.close();
    bw.close();
  }

  private static int solve(int n) {
    if (n < 0) {
      return 0;
    }

    if (n == 0) {
      return 1;
    }

    if (cache[n] != -1) {
      return cache[n];
    }

    int ret = 0;
    for (int add : new int[]{1, 2, 5}) {
      ret = (ret + solve(n - add)) % MOD;
    }

    return cache[n] = ret;
  }


}

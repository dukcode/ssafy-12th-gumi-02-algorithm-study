import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class ClimbingStairs {

  private static final int MOD = 10_007;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(cntWays(n)));

    br.close();
    bw.close();

  }

  private static int cntWays(int stair, int[] cache) {
    if (stair <= 1) {
      return 0;
    }

    if (stair <= 3) {
      return 1;
    }

    if (cache[stair] != -1) {
      return cache[stair];
    }

    return cache[stair] = (cntWays(stair - 2, cache) + cntWays(stair - 3, cache)) % MOD;
  }

  private static int cntWays(int stair) {
    int[] cache = new int[stair + 1];
    Arrays.fill(cache, -1);
    return cntWays(stair, cache);
  }

}

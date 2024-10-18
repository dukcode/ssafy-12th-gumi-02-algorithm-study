import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class RodCutting {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] rods;

  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    rods = new int[n + 1];
    st = new StringTokenizer(br.readLine());
    for (int i = 1; i <= n; i++) {
      rods[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[n + 1];
    Arrays.fill(cache, -1);

    bw.write(String.valueOf(solve(n)));

    br.close();
    bw.close();
  }

  private static int solve(int n) {
    if (n == 0) {
      return 0;
    }

    if (cache[n] != -1) {
      return cache[n];
    }

    int ret = 0;
    for (int len = 1; len <= n; len++) {
      if (n - len < 0) {
        continue;
      }

      ret = Math.max(ret, solve(n - len) + rods[len]);
    }

    return cache[n] = ret;
  }


}

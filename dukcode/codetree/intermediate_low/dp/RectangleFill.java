import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class RectangleFill {

  private static final int MOD = 10_007;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(solve(n)));

    br.close();
    bw.close();

  }

  private static int solve(int width) {
    int[] cache = new int[width + 1];
    Arrays.fill(cache, -1);
    return solve(width, cache);
  }

  private static int solve(int width, int[] cache) {
    if (width <= 1) {
      return 1;
    }

    if (cache[width] != -1) {
      return cache[width];
    }

    return cache[width] = (solve(width - 1, cache) + solve(width - 2, cache)) % MOD;
  }

}

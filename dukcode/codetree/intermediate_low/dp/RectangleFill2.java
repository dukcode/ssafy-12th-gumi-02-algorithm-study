import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class RectangleFill2 {

  private static final int MOD = 10_007;

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;

  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    cache = new int[n + 1];
    return cnt(n);
  }

  private static int cnt(int width) {
    if (width <= 1) {
      return 1;
    }

    if (cache[width] != 0) {
      return cache[width];
    }

    return cache[width] = (cnt(width - 1) + 2 * cnt(width - 2)) % MOD;
  }

}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class AsymTiling {

  private static final int MOD = 1_000_000_007;

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int[] cache;
  private static int[] asymCache;

  private static int n;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());
      bw.write(String.valueOf(countAsym()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int countAsym() {
    cache = new int[n + 1];
    asymCache = new int[n + 1];
    return countAsym2(n);
  }

  private static int countAsym(int width) {
    if (width <= 2) {
      return 0;
    }

    if (asymCache[width] != 0) {
      return asymCache[width];
    }

    int ret = 0;
    ret = (ret + countAsym(width - 2)) % MOD;
    ret = (ret + countAsym(width - 4)) % MOD;
    ret = (ret + countTiling(width - 3)) % MOD;
    ret = (ret + countTiling(width - 3)) % MOD;

    return asymCache[width] = ret;
  }

  private static int countTiling(int width) {
    if (width <= 2) {
      return width;
    }

    if (cache[width] != 0) {
      return cache[width];
    }

    return cache[width] = (countTiling(width - 1) + countTiling(width - 2)) % MOD;
  }

  private static int countAsym2(int width) {
    if (width <= 2) {
      return 0;
    }

    if (width % 2 == 1) {
      return (countTiling(width) - countTiling(width - 1) + MOD) % MOD;
    }

    int ret = countTiling(width);
    // ㅁ=ㅁ짝수
    ret = (ret - countTiling(width / 2 - 1) + MOD) % MOD;
    // ㅁ짝수
    ret = (ret - countTiling(width / 2) + MOD) % MOD;

    return ret;
  }

}

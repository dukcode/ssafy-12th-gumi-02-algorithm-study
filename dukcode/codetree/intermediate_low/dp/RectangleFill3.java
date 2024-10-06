import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class RectangleFill3 {

  private static final long MOD = 1_000_000_007L;

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;

  private static long[] cntCache;
  private static long[] halfCache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(solve(n)));

    br.close();
    bw.close();

  }

  private static long solve(int width) {
    cntCache = new long[width + 1];
    halfCache = new long[width + 1];
    Arrays.fill(cntCache, -1L);
    Arrays.fill(halfCache, -1);
    return getCnt(width);
  }

  private static long getCnt(int width) {
    if (width <= 1) {
      return width + 1;
    }

    if (cntCache[width] != -1) {
      return cntCache[width];
    }

    return cntCache[width] =
        (2 * getCnt(width - 1) +
            getCnt(width - 2) +
            getHalfCnt(width - 1)
        ) % MOD;
  }

  private static long getHalfCnt(int width) {
    if (width == 1) {
      return 2;
    }
    if (halfCache[width] != -1) {
      return halfCache[width];
    }

    return halfCache[width] = (2 * getCnt(width - 1) % MOD +
        getHalfCnt(width - 1) % MOD
    ) % MOD;
  }

}

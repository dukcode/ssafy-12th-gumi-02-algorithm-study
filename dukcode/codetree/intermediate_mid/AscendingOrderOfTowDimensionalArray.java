import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class AscendingOrderOfTowDimensionalArray {

  private static final int MX = 1_000_000_000;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static int n;
  private static int k;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    k = Integer.parseInt(br.readLine());

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    int st = 1;
    int en = (int) Math.min(MX, (long) n * n);

    while (st <= en) {
      int half = (st + en) / 2;

      int cntLower = cntLower(half);
      if (cntLower < k) {
        st = half + 1;
      } else {
        en = half - 1;
      }
    }

    return st;
  }

  private static int cntLower(int value) {
    int ret = 0;
    for (int i = 1; i <= n; ++i) {
      ret += Math.min(n, value / i);
    }

    return ret;
  }

}

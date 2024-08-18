import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class Poly {

  private static final int MOD = 10_000_000;

  private static BufferedReader br;
  private static BufferedWriter bw;

  private static int n;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      n = Integer.parseInt(br.readLine());

      cache = new int[n + 1][n + 1];
      for (int y = 0; y <= n; y++) {
        Arrays.fill(cache[y], -1);
      }

      bw.write(String.valueOf(poly()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int poly() {
    int ret = 0;
    for (int head = 1; head <= n; head++) {
      ret = (ret + poly(n, head)) % MOD;
    }

    return ret;
  }

  private static int poly(int num, int head) {
    if (num == head) {
      return 1;
    }

    if (cache[num][head] != -1) {
      return cache[num][head];
    }

    int ret = 0;
    for (int next = 1; head + next <= num; ++next) {
      int toAdd = head + next - 1;
      toAdd *= poly(num - head, next);
      toAdd %= MOD;
      ret += toAdd;
      ret %= MOD;
    }

    return cache[num][head] = ret;
  }


}

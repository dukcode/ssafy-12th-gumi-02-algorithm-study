import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Plus125 {

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

    cache[0] = 1;
    for (int num = 1; num <= n; num++) {
      cache[num] = 0;
      for (int add : new int[]{1, 2, 5}) {
        if (num - add < 0) {
          continue;
        }

        cache[num] = (cache[num] + cache[num - add]) % MOD;
      }
    }

    bw.write(String.valueOf(cache[n]));

    br.close();
    bw.close();
  }


}

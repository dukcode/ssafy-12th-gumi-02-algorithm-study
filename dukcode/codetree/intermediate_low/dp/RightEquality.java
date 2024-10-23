import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class RightEquality {

  private static final int OFFSET = 20;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;

  private static int[] arr;

  private static long[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    cache = new long[n][2 * 20 + 1];
    for (int i = 0; i < n; i++) {
      Arrays.fill(cache[i], -1);
    }

    bw.write(String.valueOf(solve(n - 1, m)));
    br.close();
    bw.close();
  }

  private static long solve(int idx, int res) {
    if (res < -20 || res > 20) {
      return 0;
    }

    if (idx == 0) {
      if (Math.abs(res) == arr[idx]) {
        return arr[idx] == 0 ? 2 : 1;
      }

      return 0;
    }

    if (cache[idx][res + OFFSET] != -1) {
      return cache[idx][res + OFFSET];
    }

    return cache[idx][res + OFFSET] =
        solve(idx - 1, res - arr[idx]) + solve(idx - 1, res + arr[idx]);
  }


}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MinimumDiffPartition {

  private static final int MX = 987_564_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;
  private static int total;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
      total += arr[i];
    }

    cache = new int[n][total + 1];
    for (int y = 0; y < n; y++) {
      Arrays.fill(cache[y], MX);
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    return solve(0, 0);
  }

  private static int solve(int idx, int sum) {
    if (idx == n) {
      return Math.abs(total - 2 * sum);
    }

    if (cache[idx][sum] != MX) {
      return cache[idx][sum];
    }

    return cache[idx][sum] = Math.min(solve(idx + 1, sum), solve(idx + 1, sum + arr[idx]));
  }


}

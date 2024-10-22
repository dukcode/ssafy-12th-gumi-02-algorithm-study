import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class EqualPartition {

  private static final int NONE = -1;
  private static final int FALSE = 0;
  private static final int TRUE = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;

  private static int[][] cache;
  private static int total;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new int[n];
    total = 0;
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
      total += arr[i];
    }

    cache = new int[n][total / 2 + 1];
    for (int i = 0; i < n; i++) {
      Arrays.fill(cache[i], NONE);
    }

    bw.write(solve());

    br.close();
    bw.close();
  }

  private static String solve() {
    if (total % 2 == 1) {
      return "No";
    }

    return solve(0, 0) == 1 ? "Yes" : "No";
  }

  private static int solve(int idx, int sum) {
    if (sum == total / 2) {
      return TRUE;
    }

    if (sum > total / 2) {
      return FALSE;
    }

    if (idx == n) {
      return FALSE;
    }

    if (cache[idx][sum] != NONE) {
      return cache[idx][sum];
    }

    return cache[idx][sum] = solve(idx + 1, sum) | solve(idx + 1, sum + arr[idx]);
  }


}

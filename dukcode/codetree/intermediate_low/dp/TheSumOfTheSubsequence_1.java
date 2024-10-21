import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TheSumOfTheSubsequence_1 {

  private static final int INITIAL = -1;
  private static final int FALSE = 0;
  private static final int TRUE = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[] arr;

  private static int[][] cache;

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

    cache = new int[m + 1][n];
    for (int y = 0; y <= m; y++) {
      Arrays.fill(cache[y], INITIAL);
    }

    bw.write(solve());

    br.close();
    bw.close();
  }

  private static String solve() {
    return solve(m, 0) == TRUE ? "Yes" : "No";
  }

  private static int solve(int sum, int idx) {
    if (sum == 0) {
      return TRUE;
    }

    if (sum < 0 || idx >= n) {
      return FALSE;
    }

    if (cache[sum][idx] != INITIAL) {
      return cache[sum][idx];
    }

    int used = solve(sum - arr[idx], idx + 1);
    int notUsed = solve(sum, idx + 1);

    return cache[sum][idx] = used | notUsed;
  }

}
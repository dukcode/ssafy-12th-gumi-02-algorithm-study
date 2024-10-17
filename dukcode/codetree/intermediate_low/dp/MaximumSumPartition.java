import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaximumSumPartition {

  private static final int UNUSED = -1;
  private static final int IMPOSSIBLE = -2;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;

  private static int total;

  private static int[][][] cache;


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

    cache = new int[total + 1][total + 1][n];
    for (int a = 0; a <= total; a++) {
      for (int b = 0; b <= total; b++) {
        Arrays.fill(cache[a][b], UNUSED);
      }

    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    return solve(0, 0, 0);
  }

  private static int solve(int idx, int sumA, int sumB) {
    if (idx == n) {
      return sumA == sumB ? sumA : IMPOSSIBLE;
    }

    if (cache[sumA][sumB][idx] != UNUSED) {
      return cache[sumA][sumB][idx];
    }

    int ret = solve(idx + 1, sumA, sumB);
    ret = Math.max(ret, solve(idx + 1, sumA + arr[idx], sumB));
    ret = Math.max(ret, solve(idx + 1, sumA, sumB + arr[idx]));

    return cache[sumA][sumB][idx] = ret;
  }

}

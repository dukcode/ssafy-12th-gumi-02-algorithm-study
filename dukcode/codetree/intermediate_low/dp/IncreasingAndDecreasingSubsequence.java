import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class IncreasingAndDecreasingSubsequence {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;
  private static int[] incCache;
  private static int[] decCache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    incCache = new int[n];
    decCache = new int[n];

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = -1;
    for (int i = 0; i < n; i++) {
      ret = Math.max(ret, solveInc(i) + solveDec(i) - 1);
    }

    return ret;
  }

  private static int solveDec(int idx) {
    if (idx == n - 1) {
      return 1;
    }

    if (decCache[idx] != 0) {
      return decCache[idx];
    }

    int ret = 1;
    for (int i = idx + 1; i < n; i++) {
      if (arr[idx] <= arr[i]) {
        continue;
      }

      ret = Math.max(ret, solveDec(i) + 1);
    }

    return decCache[idx] = ret;
  }

  private static int solveInc(int idx) {
    if (idx == 0) {
      return 1;
    }

    if (incCache[idx] != 0) {
      return incCache[idx];
    }

    int ret = 1;
    for (int i = 0; i < idx; i++) {
      if (arr[i] >= arr[idx]) {
        continue;
      }

      ret = Math.max(ret, solveInc(i) + 1);
    }

    return incCache[idx] = ret;
  }

}

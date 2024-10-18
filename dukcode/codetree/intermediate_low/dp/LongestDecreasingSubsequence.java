import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class LongestDecreasingSubsequence {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());
    int[] arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    int[] cache = new int[n + 1];
    bw.write(String.valueOf(solve(-1, n, arr, cache) - 1));

    br.close();
    bw.close();

  }

  private static int solve(int idx, int n, int[] arr, int[] cache) {
    if (idx == n - 1) {
      return cache[idx] = 1;
    }

    if (cache[idx + 1] != 0) {
      return cache[idx + 1];
    }

    int ret = 1;
    for (int i = idx + 1; i < n; i++) {
      if (idx != -1 && arr[idx] <= arr[i]) {
        continue;
      }

      ret = Math.max(ret, solve(i, n, arr, cache) + 1);
    }

    return cache[idx + 1] = ret;
  }

}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class LongestIncreasingSubsequence {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[] arr;
  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; i++) {
      arr[i] = Integer.parseInt(st.nextToken());
    }

    cache = new int[n + 1];
    Arrays.fill(cache, -1);

    bw.write(String.valueOf(lis()));

    br.close();
    bw.close();
  }

  private static int lis() {
    return lis(n) - 1;
  }

  private static int lis(int idx) {
    if (idx == 0) {
      return 1;
    }

    if (cache[idx] != -1) {
      return cache[idx];
    }

    int ret = 1;
    for (int i = 0; i < idx; i++) {
      if (idx != n && arr[i] >= arr[idx]) {
        continue;
      }

      ret = Math.max(ret, lis(i) + 1);
    }

    return cache[idx] = ret;
  }


}

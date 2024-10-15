import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaximumNumberOfJumps {

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

    cache = new int[n];
    Arrays.fill(cache, -1);

    bw.write(String.valueOf(cntMaxJumps(0)));

    br.close();
    bw.close();
  }

  private static int cntMaxJumps(int idx) {
    if (idx == n - 1) {
      return 0;
    }

    if (cache[idx] != -1) {
      return cache[idx];
    }

    int ret = 0;
    for (int i = 1; i <= arr[idx]; i++) {
      if (i + idx < n) {
        ret = Math.max(ret, cntMaxJumps(idx + i) + 1);
      }
    }

    return cache[idx] = ret;
  }


}

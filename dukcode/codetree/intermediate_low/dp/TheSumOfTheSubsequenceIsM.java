import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TheSumOfTheSubsequenceIsM {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[] arr;

  private static int[] cache;

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

    cache = new int[m + 1];
    Arrays.fill(cache, MX);

    cache[0] = 0;
    for (int i = 0; i < n; ++i) {
      for (int sum = m; sum >= 0; --sum) {
        if (sum - arr[i] < 0) {
          continue;
        }

        cache[sum] = Math.min(cache[sum], cache[sum - arr[i]] + 1);
      }
    }

    bw.write(String.valueOf(cache[m] == MX ? -1 : cache[m]));

    br.close();
    bw.close();
  }


}

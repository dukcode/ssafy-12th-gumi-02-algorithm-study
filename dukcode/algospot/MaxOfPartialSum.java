import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MaxOfPartialSum {

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
    cache[0] = arr[0];

    int ans = arr[0];
    for (int i = 1; i < n; i++) {
      cache[i] = Math.max(cache[i - 1] + arr[i], arr[i]);
      ans = Math.max(ans, cache[i]);
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }


}

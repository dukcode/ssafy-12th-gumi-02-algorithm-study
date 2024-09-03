import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/**
 * SumCloseToParticularNumber
 */
public class SumCloseToParticularNumber {

  private static int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int s;
  private static int[] arr;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    s = Integer.parseInt(st.nextToken());

    int total = 0;
    arr = new int[n];
    st = new StringTokenizer(br.readLine());
    for (int i = 0; i < n; ++i) {
      arr[i] = Integer.parseInt(st.nextToken());
      total += arr[i];
    }

    int ans = MX;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        int diff = Math.abs(total - arr[i] - arr[j] - s);
        ans = Math.min(ans, diff);
      }
    }

    bw.write(String.valueOf(ans));

    bw.close();
    br.close();

  }
}
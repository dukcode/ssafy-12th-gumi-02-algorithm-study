import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class GainExpQuickly {

  private static final int MN = -987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[] e;
  private static int[] t;
  private static int totalTime;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    e = new int[n + 1];
    t = new int[n + 1];
    totalTime = 0;
    for (int i = 1; i <= n; ++i) {
      st = new StringTokenizer(br.readLine());
      e[i] = Integer.parseInt(st.nextToken());
      t[i] = Integer.parseInt(st.nextToken());
      totalTime += t[i];
    }

    cache = new int[n + 1][totalTime + 1];
    for (int y = 0; y <= n; ++y) {
      Arrays.fill(cache[y], MN);
    }
    cache[0][0] = 0;

    for (int idx = 1; idx <= n; ++idx) {
      for (int time = 0; time <= totalTime; ++time) {
        if (time - t[idx] >= 0) {
          cache[idx][time] = Math.max(cache[idx][time], cache[idx - 1][time - t[idx]] + e[idx]);
        }

        cache[idx][time] = Math.max(cache[idx][time], cache[idx - 1][time]);
      }
    }

    int ans = -1;
    for (int t = 0; t <= totalTime; ++t) {
      if (cache[n][t] >= m) {
        ans = t;
        break;
      }
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }

}

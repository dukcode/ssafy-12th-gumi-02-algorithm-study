import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaximumTransitTime {

  private static final long MX = 100_000_000_000_000L;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static long[] times;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    init();
    long ans = solve();

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static long solve() {
    long minTime = 1;
    long maxTime = MX;

    while (minTime <= maxTime) {
      long halfTime = (minTime + maxTime) / 2;

      if (getNum(halfTime) < n) {
        minTime = halfTime + 1;
      } else {
        maxTime = halfTime - 1;
      }
    }

    return minTime;
  }

  // 증가 함수
  private static long getNum(long time) {
    long cnt = 0;
    for (int i = 0; i < m; ++i) {
      cnt += time / times[i];
    }
    return cnt;
  }

  private static void init() {
    Arrays.sort(times);
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    times = new long[m];
    for (int i = 0; i < m; i++) {
      times[i] = Long.parseLong(br.readLine());
    }
  }


}

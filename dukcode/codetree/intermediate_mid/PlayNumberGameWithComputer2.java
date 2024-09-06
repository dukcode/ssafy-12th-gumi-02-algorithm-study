import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class PlayNumberGameWithComputer2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static long m;
  private static long a;
  private static long b;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    m = Long.parseLong(br.readLine());

    st = new StringTokenizer(br.readLine());
    a = Long.parseLong(st.nextToken());
    b = Long.parseLong(st.nextToken());

    int minCnt = Integer.MAX_VALUE;
    int maxCnt = 0;

    for (long num = a; num <= b; ++num) {
      int cnt = 0;
      long l = 1;
      long r = m;

      while (l <= r) {
        cnt++;
        long half = (l + r) / 2;

        if (half == num) {
          break;
        }

        if (half < num) {
          l = half + 1;
        } else {
          r = half - 1;
        }
      }

      minCnt = Math.min(minCnt, cnt);
      maxCnt = Math.max(maxCnt, cnt);
    }

    bw.write(String.valueOf(minCnt));
    bw.write(' ');
    bw.write(String.valueOf(maxCnt));

    br.close();
    bw.close();
  }

}

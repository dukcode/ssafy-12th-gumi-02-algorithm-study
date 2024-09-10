import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class TwoPointsOfTheLineThatDontOverlap {

  private static final long MX = 1_000_000_000_000_000_000L;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static long n;
  private static int m;
  private static Line[] lines;

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

  private static void init() {
    Arrays.sort(lines, (l1, l2) -> l1.start == l2.start ?
        Long.compare(l1.end, l2.end) :
        Long.compare(l1.start, l2.start));
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Long.parseLong(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    lines = new Line[m];
    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      long s = Long.parseLong(st.nextToken());
      long e = Long.parseLong(st.nextToken());

      lines[i] = new Line(s, e);
    }

  }

  private static long solve() {
    long minDist = 1;
    long maxDist = MX;

    while (minDist <= maxDist) {
      long halfDist = (minDist + maxDist) / 2;

      if (getMaxCnt(halfDist) >= n) {
        minDist = halfDist + 1;
      } else {
        maxDist = halfDist - 1;
      }
    }

    return minDist - 1;
  }

  private static long getMaxCnt(long minDist) {
    long lastPos = -MX;
    int cnt = 0;
    for (Line line : lines) {
      while (lastPos + minDist <= line.end) {
        cnt++;
        lastPos = Math.max(line.start, lastPos + minDist);

        if (cnt == n) {
          return cnt;
        }
      }
    }

    return cnt;
  }


  private static class Line {

    long start;
    long end;

    public Line(long start, long end) {
      this.start = start;
      this.end = end;
    }
  }

}

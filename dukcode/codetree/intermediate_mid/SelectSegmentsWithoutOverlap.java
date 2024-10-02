import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SelectSegmentsWithoutOverlap {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static Line[] lines;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    lines = new Line[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int s = Integer.parseInt(st.nextToken());
      int e = Integer.parseInt(st.nextToken());
      lines[i] = new Line(s, e);
    }

    Arrays.sort(lines, (l1, l2) -> l1.s == l2.s ?
        Integer.compare(l1.e, l2.e) :
        Integer.compare(l1.s, l2.s));

    bw.write(String.valueOf(solve(0, 0, -1)));

    br.close();
    bw.close();

  }

  private static int solve(int here, int cnt, int last) {
    if (here == n) {
      return cnt;
    }

    int ret = solve(here + 1, cnt, last);

    if (lines[here].s > last) {
      ret = Math.max(ret, solve(here + 1, cnt + 1, lines[here].e));
    }

    return ret;
  }

  private static class Line {

    int s;
    int e;

    public Line(int s, int e) {
      this.s = s;
      this.e = e;
    }
  }

}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class SelectSegmentsWithoutOverlap2 {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static Segment[] segments;
  private static int[] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    segments = new Segment[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int s = Integer.parseInt(st.nextToken());
      int e = Integer.parseInt(st.nextToken());
      segments[i] = new Segment(s, e);
    }

    cache = new int[n + 1];
    Arrays.fill(cache, -1);

    Arrays.sort(segments);

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    return solve(n) - 1;
  }

  private static int solve(int nowIdx) {

    if (cache[nowIdx] != -1) {
      return cache[nowIdx];
    }

    int ret = 1;
    for (int beforeIdx = 0; beforeIdx < nowIdx; ++beforeIdx) {
      if (nowIdx != n && segments[beforeIdx].e >= segments[nowIdx].s) {
        continue;
      }
      ret = Math.max(ret, solve(beforeIdx) + 1);
    }

    return cache[nowIdx] = ret;
  }


  private static class Segment implements Comparable<Segment> {

    int s;
    int e;

    public Segment(int s, int e) {
      this.s = s;
      this.e = e;
    }

    @Override
    public int compareTo(Segment o) {
      return Integer.compare(e, o.e);
    }
  }
}

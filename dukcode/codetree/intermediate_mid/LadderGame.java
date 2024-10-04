import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class LadderGame {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static List<Line> ladder;

  private static int[] result;
  private static int ans;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    ladder = new ArrayList<>();
    for (int i = 0; i < m; ++i) {
      st = new StringTokenizer(br.readLine());
      int l = Integer.parseInt(st.nextToken()) - 1;
      int h = Integer.parseInt(st.nextToken()) - 1;
      ladder.add(new Line(h, l));
    }

    ladder.sort((l1, l2) -> l1.height == l2.height ? l1.left - l2.left : l1.height - l2.height);

    result = getResult(ladder);

    ans = MX;
    List<Line> cands = new ArrayList<>();
    solve(0, 0, cands);
    bw.write(String.valueOf(ans == MX ? -1 : ans));

    br.close();
    bw.close();

  }

  private static void solve(int idx, int cnt, List<Line> cands) {
    if (idx == m) {
      int[] candidate = getResult(cands);
      for (int i = 0; i < n; ++i) {
        if (candidate[i] != result[i]) {
          return;
        }
      }

      ans = Math.min(ans, cnt);
      return;
    }

    if (cnt > ans) {
      return;
    }

    solve(idx + 1, cnt, cands);

    cands.add(ladder.get(idx));
    solve(idx + 1, cnt + 1, cands);
    cands.remove(cands.size() - 1);
  }

  private static int[] getResult(List<Line> ladder) {
    int[] ret = IntStream.range(0, n).toArray();
    for (Line line : ladder) {
      int tmp = ret[line.left];
      ret[line.left] = ret[line.left + 1];
      ret[line.left + 1] = tmp;
    }

    return ret;
  }

  private static class Line {

    int height;
    int left;

    public Line(int height, int left) {
      this.height = height;
      this.left = left;
    }
  }


}

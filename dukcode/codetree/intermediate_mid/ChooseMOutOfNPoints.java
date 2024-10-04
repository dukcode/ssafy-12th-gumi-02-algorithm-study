import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class ChooseMOutOfNPoints {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static Point[] points;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    points = new Point[n];
    for (int i = 0; i < n; i++) {
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int y = Integer.parseInt(st.nextToken());
      points[i] = new Point(x, y);
    }

    List<Point> picked = new ArrayList<>();
    bw.write(String.valueOf(solve(-1, picked)));
    br.close();
    bw.close();

  }

  private static int solve(int lastIdx, List<Point> picked) {
    if (picked.size() == m) {
      return getMaxDist(picked);
    }

    int ret = MX;
    for (int nextIdx = lastIdx + 1; nextIdx < n; nextIdx++) {
      picked.add(points[nextIdx]);
      ret = Math.min(ret, solve(nextIdx, picked));
      picked.remove(picked.size() - 1);
    }

    return ret;
  }

  private static int getMaxDist(List<Point> picked) {
    int n = picked.size();

    int ret = 0;
    for (int i = 0; i < n; i++) {
      Point a = picked.get(i);
      for (int j = i + 1; j < n; j++) {
        ret = Math.max(ret, a.getDist(picked.get(j)));
      }
    }

    return ret;
  }


  private static class Point {

    int x;
    int y;

    public Point(int x, int y) {
      this.x = x;
      this.y = y;
    }

    public int getDist(Point p) {
      int dx = x - p.x;
      int dy = y - p.y;
      return dx * dx + dy * dy;
    }
  }

}

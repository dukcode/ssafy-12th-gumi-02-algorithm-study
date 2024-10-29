import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class CollectCoinsEasy {

  private static final int MX = 987_654_321;

  private static final int START = 0;
  private static final int END = 10;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;

  private static Point[] coins;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();

    int ans = solve(0, 0, 0);
    bw.write(String.valueOf(ans == MX ? -1 : ans));

    br.close();
    bw.close();

  }

  private static int solve(int last, int cnt, int dist) {
    if (cnt == 3) {
      return dist + getDistBetween(coins[last], coins[END]);
    }

    int ret = MX;
    for (int next = last + 1; next < END; ++next) {
      if (coins[next] == null) {
        continue;
      }

      ret = Math.min(ret, solve(next, cnt + 1, dist + getDistBetween(coins[last], coins[next])));
    }

    return ret;
  }

  private static int getDistBetween(Point a, Point b) {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
  }

  private static void input() throws IOException {
    n = Integer.parseInt(br.readLine());

    coins = new Point[11];
    for (int y = 0; y < n; y++) {
      char[] line = br.readLine().toCharArray();
      for (int x = 0; x < n; x++) {
        if (Character.isDigit(line[x])) {
          coins[line[x] - '0'] = new Point(y, x);
          continue;
        }

        if (line[x] == 'S') {
          coins[START] = new Point(y, x);
          continue;
        }

        if (line[x] == 'E') {
          coins[END] = new Point(y, x);
        }

      }
    }
  }

  private static class Point {

    int y;
    int x;

    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class StrongExplosion {

  private static final int[][][] BLOCKS = {
      {
          {-2, 0}, {-1, 0}, {0, 0}, {1, 0}, {2, 0}
      },
      {
          {0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}
      },
      {
          {0, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
      }
  };

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] exploded;
  private static List<Point> bombs;


  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    bombs = new ArrayList<>();
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        if (Integer.parseInt(st.nextToken()) != 0) {
          bombs.add(new Point(y, x));
        }
      }
    }

    exploded = new int[n][n];

    bw.write(String.valueOf(cntMaxExplosions(0, 0)));

    br.close();
    bw.close();

  }

  private static int cntMaxExplosions(int idx, int cnt) {
    if (idx == bombs.size()) {
      return cnt;
    }

    int ret = 0;
    for (int i = 0; i < 3; ++i) {
      int toAdd = draw(idx, i, 1);
      ret = Math.max(ret, cntMaxExplosions(idx + 1, cnt + toAdd));
      draw(idx, i, -1);
    }
    return ret;
  }

  private static int draw(int bombIdx, int blockIdx, int delta) {
    int[][] block = BLOCKS[blockIdx];
    Point bomb = bombs.get(bombIdx);

    int cnt = 0;
    for (int[] pos : block) {
      int ny = bomb.y + pos[0];
      int nx = bomb.x + pos[1];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      exploded[ny][nx] += delta;
      if (exploded[ny][nx] == 1) {
        cnt++;
      }
    }

    return cnt;
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

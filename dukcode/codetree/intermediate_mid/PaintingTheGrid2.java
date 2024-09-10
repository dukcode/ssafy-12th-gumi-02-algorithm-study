import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class PaintingTheGrid2 {

  private static final int MX = 1_000_000;
  private static final int[] DELTA_Y = {0, 0, -1, 1};
  private static final int[] DELTA_X = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;
  private static int maxValue;
  private static int minValue;

  private static int target;
  private static boolean[][] discovered;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    init();

    int ans = solve();
    bw.write(String.valueOf(ans));

    br.close();
    bw.close();
  }

  private static int solve() {
    int minD = 0;
    int maxD = maxValue - minValue;

    while (minD <= maxD) {
      int halfD = (maxD + minD) / 2;

      if (getMaxCnt(halfD) < target) {
        minD = halfD + 1;
      } else {
        maxD = halfD - 1;
      }
    }

    return minD;
  }

  private static int dfs(int d, int sy, int sx) {
    Stack<Point> stk = new Stack<>();

    discovered[sy][sx] = true;
    stk.push(new Point(sy, sx));

    int cnt = 1;
    while (!stk.isEmpty()) {
      Point cur = stk.pop();

      for (int dir = 0; dir < 4; ++dir) {
        int ny = cur.y + DELTA_Y[dir];
        int nx = cur.x + DELTA_X[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (discovered[ny][nx]) {
          continue;
        }

        if (Math.abs(board[ny][nx] - board[cur.y][cur.x]) > d) {
          continue;
        }

        discovered[ny][nx] = true;
        cnt++;
        stk.push(new Point(ny, nx));
      }
    }

    return cnt;
  }

  private static int getMaxCnt(int d) {
    discovered = new boolean[n][n];
    int ret = 0;
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        if (discovered[y][x]) {
          continue;
        }
        ret = Math.max(ret, dfs(d, y, x));
        if (ret >= target) {
          return ret;
        }
      }
    }

    return ret;
  }

  private static void input() throws IOException {
    n = Integer.parseInt(br.readLine());

    minValue = MX;
    maxValue = MX;
    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
        minValue = Math.min(board[y][x], minValue);
        maxValue = Math.max(board[y][x], maxValue);
      }
    }
  }

  private static void init() {
    target = (n * n + 1) / 2;
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

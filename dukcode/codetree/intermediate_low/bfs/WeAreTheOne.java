import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class WeAreTheOne {

  private static final int[] DY = {-1, 0, 0, 1};
  private static final int[] DX = {0, -1, 1, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int u;
  private static int d;

  private static boolean[] picked;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    init();
    bw.write(String.valueOf(getMaxCnt()));

    br.close();
    bw.close();

  }

  private static void init() {
    picked = new boolean[n * n];
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());
    u = Integer.parseInt(st.nextToken());
    d = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }
  }

  private static int getMaxCnt() {
    return getMaxCnt(0, 0);
  }

  private static int getMaxCnt(int idx, int cnt) {
    if (cnt == k) {
      return getCnt();
    }

    if (idx == n * n) {
      return 0;
    }

    int ret = getMaxCnt(idx + 1, cnt);
    picked[idx] = true;
    ret = Math.max(ret, getMaxCnt(idx + 1, cnt + 1));
    picked[idx] = false;

    return ret;
  }

  private static int getCnt() {
    boolean[][] discovered = new boolean[n][n];
    Stack<Point> stk = new Stack<>();

    for (int i = 0; i < n * n; ++i) {
      if (picked[i]) {
        int y = i / n;
        int x = i % n;
        stk.push(new Point(y, x));
        discovered[y][x] = true;
      }
    }

    int cnt = 0;
    while (!stk.isEmpty()) {
      Point cur = stk.pop();
      cnt++;
      for (int dir = 0; dir < 4; ++dir) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        int diff = Math.abs(board[ny][nx] - board[cur.y][cur.x]);
        if (discovered[ny][nx] || diff < u || diff > d) {
          continue;
        }

        discovered[ny][nx] = true;
        stk.push(new Point(ny, nx));
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

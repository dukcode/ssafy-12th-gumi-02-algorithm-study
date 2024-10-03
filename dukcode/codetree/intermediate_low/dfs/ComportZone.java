import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class ComportZone {

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;

  private static int[][] board;

  private static int maxK;

  private static boolean[][] discovered;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());
    board = new int[h][w];
    for (int y = 0; y < h; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
        maxK = Math.max(maxK, board[y][x]);
      }
    }

    int[] ans = solve();
    bw.write(String.valueOf(ans[0]));
    bw.write(' ');
    bw.write(String.valueOf(ans[1]));

    br.close();
    bw.close();

  }

  private static int[] solve() {
    int cnt = 0;
    int ansK = 1;
    for (int k = 1; k <= maxK; k++) {
      int cntZone = cntComportZone(k);
      if (cnt < cntZone) {

        cnt = cntZone;
        ansK = k;
      }
    }
    return new int[]{ansK, cnt};
  }


  private static int cntComportZone(int k) {
    discovered = new boolean[h][w];
    int cnt = 0;
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        if (discovered[y][x] || board[y][x] <= k) {
          continue;
        }

        cnt++;
        dfs(y, x, k);

      }
    }

    return cnt;
  }

  private static void dfs(int y, int x, int k) {
    Stack<Point> stk = new Stack<>();

    stk.push(new Point(y, x));
    discovered[y][x] = true;

    while (!stk.isEmpty()) {
      Point cur = stk.pop();
      for (int dir = 0; dir < 4; dir++) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
          continue;
        }

        if (discovered[ny][nx] || board[ny][nx] <= k) {
          continue;
        }

        discovered[ny][nx] = true;
        stk.push(new Point(ny, nx));
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


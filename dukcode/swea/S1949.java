import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 등산로 조성
public class S1949 {

  private static final int[] DY = {-1, 1, 0, 0};
  private static final int[] DX = {0, 0, -1, 1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int k;
  private static int[][] board;


  private static int top;
  private static boolean[][] visited;
  private static int ans;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      st = new StringTokenizer(br.readLine());
      n = Integer.parseInt(st.nextToken());
      k = Integer.parseInt(st.nextToken());

      board = new int[n][n];
      top = 0;
      for (int y = 0; y < n; y++) {
        st = new StringTokenizer(br.readLine());
        for (int x = 0; x < n; x++) {
          board[y][x] = Integer.parseInt(st.nextToken());
          top = Math.max(top, board[y][x]);
        }
      }

      ans = 0;
      solve();

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(ans));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static void solve() {
    visited = new boolean[n][n];
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (board[y][x] == top) {
          getLongestPath(y, x, 1, false);
        }
      }
    }
  }


  private static void getLongestPath(int y, int x, int dist, boolean used) {
    visited[y][x] = true;

    if (ans < dist) {
      ans = dist;
    }

    for (int dir = 0; dir < 4; dir++) {
      int ny = y + DY[dir];
      int nx = x + DX[dir];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      if (visited[ny][nx]) {
        continue;
      }

      if (board[ny][nx] < board[y][x]) {
        getLongestPath(ny, nx, dist + 1, used);
        continue;
      }

      if (!used && board[ny][nx] - k < board[y][x]) {
        int temp = board[ny][nx];
        board[ny][nx] = board[y][x] - 1;
        getLongestPath(ny, nx, dist + 1, true);
        board[ny][nx] = temp;
      }

    }

    visited[y][x] = false;
  }

}

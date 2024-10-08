import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class OrangesHaveGoneBad {

  private static final int MX = 987_654_321;

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    int[][] ans = solve();
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        bw.write(String.valueOf(
            ans[y][x] == -1 && board[y][x] == 1 ? -2 : ans[y][x]
        ));
        bw.write(' ');
      }
      bw.newLine();
    }
    bw.newLine();

    br.close();
    bw.close();

  }

  private static int[][] solve() {
    int[][] times = new int[n][n];
    for (int y = 0; y < n; y++) {
      Arrays.fill(times[y], -1);
    }

    Queue<Point> q = new LinkedList<>();
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (board[y][x] == 2) {
          q.offer(new Point(y, x));
          times[y][x] = 0;
        }
      }
    }

    while (!q.isEmpty()) {
      Point cur = q.poll();
      for (int dir = 0; dir < 4; dir++) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (board[ny][nx] == 0 || times[ny][nx] != -1) {
          continue;
        }

        q.offer(new Point(ny, nx));
        times[ny][nx] = times[cur.y][cur.x] + 1;
      }
    }

    return times;
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

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class KnightMovements {

  private static final int[] DY = {-1, -2, -2, -1, 1, 2, 2, 1};
  private static final int[] DX = {2, 1, -1, -2, -2, -1, 1, 2};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int sy;
  private static int sx;
  private static int ey;
  private static int ex;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    st = new StringTokenizer(br.readLine());
    sy = Integer.parseInt(st.nextToken()) - 1;
    sx = Integer.parseInt(st.nextToken()) - 1;
    ey = Integer.parseInt(st.nextToken()) - 1;
    ex = Integer.parseInt(st.nextToken()) - 1;

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    int[][] dist = new int[n][n];
    Point start = new Point(sy, sx);
    Queue<Point> q = new ArrayDeque<>();

    q.offer(start);
    dist[sy][sx] = 1;

    while (!q.isEmpty()) {
      Point cur = q.poll();

      if (cur.y == ey && cur.x == ex) {
        break;
      }

      for (int dir = 0; dir < 8; dir++) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (dist[ny][nx] != 0) {
          continue;
        }

        dist[ny][nx] = dist[cur.y][cur.x] + 1;
        q.offer(new Point(ny, nx));
      }
    }

    return dist[ey][ex] == 0 ? -1 : dist[ey][ex] - 1;
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

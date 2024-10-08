import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class RemoveKWalls {

  private static final int MX = 987_654_321;

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static final int WALL = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int[][] board;
  private static int sy;
  private static int sx;
  private static int ey;
  private static int ex;

  private static List<Point> walls;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    walls = new ArrayList<>();
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        int block = Integer.parseInt(st.nextToken());

        if (block == WALL) {
          walls.add(new Point(y, x));
        }

        board[y][x] = block;
      }
    }

    st = new StringTokenizer(br.readLine());
    sy = Integer.parseInt(st.nextToken()) - 1;
    sx = Integer.parseInt(st.nextToken()) - 1;

    st = new StringTokenizer(br.readLine());
    ey = Integer.parseInt(st.nextToken()) - 1;
    ex = Integer.parseInt(st.nextToken()) - 1;

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    int ret = solve(-1, 0);
    return ret == MX ? -1 : ret - 1;
  }

  private static int solve(int lastIdx, int cnt) {
    if (cnt == k) {
      return getDist();
    }

    int ret = MX;
    for (int idx = lastIdx + 1; idx < walls.size(); ++idx) {
      Point wall = walls.get(idx);

      board[wall.y][wall.x] = 0;
      ret = Math.min(ret, solve(idx, cnt + 1));
      board[wall.y][wall.x] = 1;
    }

    return ret;
  }

  private static int getDist() {
    int[][] dist = new int[n][n];

    Queue<Point> q = new LinkedList<>();
    q.offer(new Point(sy, sx));
    dist[sy][sx] = 1;

    while (!q.isEmpty()) {
      Point cur = q.poll();
      if (cur.y == ey && cur.x == ex) {
        return dist[cur.y][cur.x];
      }

      for (int dir = 0; dir < 4; ++dir) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];
        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (dist[ny][nx] != 0 || board[ny][nx] == WALL) {
          continue;
        }

        q.offer(new Point(ny, nx));
        dist[ny][nx] = dist[cur.y][cur.x] + 1;
      }
    }

    return MX;
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

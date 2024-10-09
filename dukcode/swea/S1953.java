import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

// 탈주범 검거
public class S1953 {

  private static final int[][][] TUNNELS = {
      {},
      {{-1, 0}, {1, 0}, {0, -1}, {0, 1}},
      {{-1, 0}, {1, 0}},
      {{0, -1}, {0, 1}},
      {{-1, 0}, {0, 1}},
      {{1, 0}, {0, 1}},
      {{1, 0}, {0, -1}},
      {{-1, 0}, {0, -1}}
  };

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int h;
  private static int w;
  private static int r;
  private static int c;
  private static int l;

  private static int[][] board;

  private static boolean[][] canMove;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      input();

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static int solve() {
    int[][] dist = new int[h][w];

    Queue<Point> q = new ArrayDeque<>();

    q.offer(new Point(r, c));
    dist[r][c] = 1;

    int cnt = 0;
    while (!q.isEmpty()) {
      Point cur = q.poll();

      cnt++;
      if (dist[cur.y][cur.x] == l) {
        continue;
      }

      for (int[] delta : TUNNELS[board[cur.y][cur.x]]) {
        int ny = cur.y + delta[0];
        int nx = cur.x + delta[1];

        if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
          continue;
        }

        if (board[ny][nx] == 0 || dist[ny][nx] != 0) {
          continue;
        }

        if (!canMove(board[ny][nx], delta)) {
          continue;
        }

        dist[ny][nx] = dist[cur.y][cur.x] + 1;
        q.offer(new Point(ny, nx));
      }
    }

    return cnt;
  }

  private static boolean canMove(int to, int[] delta) {
    for (int[] d : TUNNELS[to]) {
      if (delta[0] + d[0] == 0 && delta[1] + d[1] == 0) {
        return true;
      }
    }

    return false;
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());
    r = Integer.parseInt(st.nextToken());
    c = Integer.parseInt(st.nextToken());
    l = Integer.parseInt(st.nextToken());

    board = new int[h][w];
    for (int y = 0; y < h; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
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

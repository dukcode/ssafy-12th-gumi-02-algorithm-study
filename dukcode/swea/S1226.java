import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

// 미로
public class S1226 {


  private static final int T = 10;

  private static final int N = 16;

  private static final int WALL = 1;
  private static final int START = 2;
  private static final int END = 3;

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int[][] board;

  private static Point start;
  private static Point end;


  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    for (int tc = 1; tc <= T; ++tc) {
      input();
      int ans = solve();
      output(tc, ans);
    }

    br.close();
    bw.close();

  }

  private static int solve() {
    boolean possible = false;

    boolean[][] discovered = new boolean[N][N];
    Queue<Point> q = new ArrayDeque<>();

    q.offer(start);
    discovered[start.y][start.x] = true;

    while (!q.isEmpty()) {
      Point cur = q.poll();
      if (cur.equals(end)) {
        possible = true;
        break;
      }

      for (int dir = 0; dir < 4; ++dir) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= N || nx < 0 || nx >= N) {
          continue;
        }

        if (discovered[ny][nx] || board[ny][nx] == WALL) {
          continue;
        }

        discovered[ny][nx] = true;
        q.offer(new Point(ny, nx));
      }
    }

    return possible ? 1 : 0;
  }

  private static void output(int tc, int ans) throws IOException {
    bw.write("#" + tc + " ");
    bw.write(String.valueOf(ans));
    bw.newLine();
  }

  private static void input() throws IOException {
    br.readLine();

    board = new int[N][N];
    for (int y = 0; y < N; y++) {
      String line = br.readLine();
      for (int x = 0; x < N; x++) {
        int block = line.charAt(x) - '0';
        if (block == START) {
          start = new Point(y, x);
          continue;
        }

        if (block == END) {
          end = new Point(y, x);
          continue;
        }

        board[y][x] = block;
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

    public boolean equals(Point point) {
      return y == point.y && x == point.x;
    }
  }
}

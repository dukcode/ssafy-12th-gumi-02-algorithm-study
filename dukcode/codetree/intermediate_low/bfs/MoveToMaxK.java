import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class MoveToMaxK {

  // 상 좌 우 하
  private static final int[] DY = {-1, 0, 0, 1};
  private static final int[] DX = {0, -1, 1, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int[][] board;
  private static Point start;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    Point end = makeMoves();

    bw.write(end.toString());

    br.close();
    bw.close();

  }

  private static Point makeMoves() {
    Point now = start;
    for (int i = 0; i < k; i++) {
      if (!move(now)) {
        break;
      }
    }

    return now;
  }

  private static boolean move(Point now) {
    int pivot = board[now.y][now.x];

    boolean[][] discovered = new boolean[n][n];
    Queue<Point> q = new ArrayDeque<>();

    q.offer(now);

    boolean canMove = false;
    while (!q.isEmpty()) {
      Point cur = q.poll();
      for (int dir = 0; dir < 4; dir++) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (discovered[ny][nx] || board[ny][nx] >= pivot) {
          continue;
        }

        canMove = true;
        q.offer(new Point(ny, nx));
        discovered[ny][nx] = true;

      }
    }

    if (!canMove) {
      return false;
    }

    int maxVal = 0;
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (!discovered[y][x]) {
          continue;
        }

        if (board[y][x] > maxVal) {
          maxVal = board[y][x];
          now.y = y;
          now.x = x;
        }
      }
    }

    return true;
  }


  private static void input() throws IOException {
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

    st = new StringTokenizer(br.readLine());
    int r = Integer.parseInt(st.nextToken()) - 1;
    int c = Integer.parseInt(st.nextToken()) - 1;
    start = new Point(r, c);
  }

  private static class Point {

    int y;
    int x;

    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }

    @Override
    public String toString() {
      return (y + 1) + " " + (x + 1);
    }
  }

}

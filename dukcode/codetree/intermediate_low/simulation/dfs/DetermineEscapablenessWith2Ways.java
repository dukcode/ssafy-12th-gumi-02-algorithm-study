import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class DetermineEscapablenessWith2Ways {

  private static final int[] DY = {1, 0};
  private static final int[] DX = {0, 1};

  private static final int SNAKE = 0;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static int[][] board;

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
      }
    }

    discovered = new boolean[h][w];

    Stack<Point> stk = new Stack<>();
    stk.push(new Point(0, 0));
    discovered[0][0] = true;

    boolean possible = false;
    while (!stk.isEmpty()) {
      Point cur = stk.pop();

      if (cur.y == h - 1 && cur.x == w - 1) {
        possible = true;
        break;
      }

      for (int dir = 0; dir < 2; dir++) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
          continue;
        }

        if (discovered[ny][nx]) {
          continue;
        }

        if (board[ny][nx] == SNAKE) {
          continue;
        }

        discovered[ny][nx] = true;
        stk.push(new Point(ny, nx));
      }
    }

    bw.write(String.valueOf(possible ? 1 : 0));

    br.close();
    bw.close();

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

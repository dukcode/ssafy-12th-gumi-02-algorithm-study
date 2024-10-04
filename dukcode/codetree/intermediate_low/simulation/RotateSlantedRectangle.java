import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class RotateSlantedRectangle {

  private static final int[] DY = {-1, -1, 1, 1};
  private static final int[] DX = {1, -1, -1, 1};
  private static final int CCW = 0;
  private static final int CW = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  private static int r;
  private static int c;
  private static int[] moves;
  private static int rot;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    input();
    rotate(r, c, moves, rot);
    printBoard();

    br.close();
    bw.close();
  }

  private static void printBoard() throws IOException {
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        bw.write(String.valueOf(board[y][x]));
        bw.write(' ');
      }
      bw.newLine();
    }
    bw.newLine();
  }

  private static void rotate(int r, int c, int[] moves, int rot) {
    int delta = rot == CCW ? 1 : -1;
    int[][] tmp = copy(board);
    int y = r;
    int x = c;
    for (int i = 0; i < 4; i++) {
      int dir = (rot == CCW ? 0 : 3) + i * delta;
      for (int move = 0; move < moves[dir]; ++move) {
        int ny = y + DY[dir];
        int nx = x + DX[dir];
        tmp[ny][nx] = board[y][x];
        y = ny;
        x = nx;
      }
    }

    board = copy(tmp);
  }

  private static int[][] copy(int[][] board) {
    int n = board.length;
    int[][] ret = new int[n][n];
    for (int y = 0; y < n; ++y) {
      System.arraycopy(board[y], 0, ret[y], 0, n);
    }

    return ret;
  }

  private static void input() throws IOException {
    n = Integer.parseInt(br.readLine());

    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    st = new StringTokenizer(br.readLine());
    r = Integer.parseInt(st.nextToken()) - 1;
    c = Integer.parseInt(st.nextToken()) - 1;

    moves = new int[4];
    for (int i = 0; i < 4; ++i) {
      moves[i] = Integer.parseInt(st.nextToken());
    }

    rot = Integer.parseInt(st.nextToken());
  }


}

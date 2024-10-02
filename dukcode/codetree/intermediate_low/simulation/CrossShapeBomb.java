import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class CrossShapeBomb {

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    st = new StringTokenizer(br.readLine());
    int bombY = Integer.parseInt(st.nextToken()) - 1;
    int bombX = Integer.parseInt(st.nextToken()) - 1;

    boom(bombY, bombX);

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

  private static void boom(int y, int x) throws IOException {
    int cnt = board[y][x];
    board[y][x] = 0;
    for (int dir = 0; dir < 4; ++dir) {
      for (int i = 0; i < cnt; ++i) {
        int ny = y + DY[dir] * i;
        int nx = x + DX[dir] * i;

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          break;
        }

        board[ny][nx] = 0;
      }
    }

    drop();
  }

  private static void drop() {
    for (int x = 0; x < n; ++x) {
      dropCol(x);
    }
  }

  private static void dropCol(int x) {
    int[] res = new int[n];
    int idx = n - 1;
    for (int y = n - 1; y >= 0; --y) {
      if (board[y][x] == 0) {
        continue;
      }

      res[idx--] = board[y][x];
    }

    for (int y = 0; y < n; ++y) {
      board[y][x] = res[y];
    }
  }


}

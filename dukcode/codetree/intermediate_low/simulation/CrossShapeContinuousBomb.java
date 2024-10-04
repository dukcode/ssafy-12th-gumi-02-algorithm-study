import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class CrossShapeContinuousBomb {

  private static final int[] DY = {-1, 1, 0, 0};
  private static final int[] DX = {0, 0, -1, 1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    for (int i = 0; i < m; ++i) {
      int col = Integer.parseInt(br.readLine()) - 1;
      boom(col);
    }

    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        bw.write(String.valueOf(board[y][x]));
        bw.write(' ');
      }
      bw.newLine();
    }
    bw.newLine();

    br.close();
    bw.close();
  }

  private static void boom(int col) {
    int row = findBomb(col);
    if (row == -1) {
      return;
    }

    boom(row, col);
    drop();
  }

  private static void drop() {
    for (int x = 0; x < n; ++x) {
      int end = n - 1;
      for (int y = n - 1; y >= 0; --y) {
        if (board[y][x] == 0) {
          continue;
        }
        board[end--][x] = board[y][x];
      }

      for (int y = end; y >= 0; --y) {
        board[y][x] = 0;
      }
    }
  }

  private static void boom(int y, int x) {
    int cnt = board[y][x];
    for (int dir = 0; dir < 4; ++dir) {
      for (int i = 0; i < cnt; ++i) {
        int ny = y + DY[dir] * i;
        int nx = x + DX[dir] * i;

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        board[ny][nx] = 0;
      }
    }
  }

  private static int findBomb(int col) {
    for (int y = 0; y < n; ++y) {
      if (board[y][col] != 0) {
        return y;
      }
    }

    return -1;
  }


}

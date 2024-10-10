import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class S5656 {

  private static final int MX = 987_654_321;

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int w;
  private static int h;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      input();
      int ans = cntMinBlocksAfterBoom(n, copyBoard(board));

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(ans == MX ? 0 : ans));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int[][] copyBoard(int[][] board) {
    int[][] ret = new int[h][w];
    for (int y = 0; y < h; ++y) {
      System.arraycopy(board[y], 0, ret[y], 0, w);
    }

    return ret;
  }

  private static int cntMinBlocksAfterBoom(int cntRemain, int[][] board) {
    if (cntRemain == 0) {
      return cntBlock(board);
    }

    int ret = MX;
    for (int x = 0; x < w; ++x) {
      int y = findBombPos(x, board);
      if (y == -1) {
        continue;
      }

      int[][] tmpBoard = copyBoard(board);
      boom(y, x, tmpBoard[y][x], tmpBoard);
      drop(tmpBoard);
      ret = Math.min(ret, cntMinBlocksAfterBoom(cntRemain - 1, tmpBoard));
    }

    return ret;
  }

  private static int cntBlock(int[][] board) {
    int ret = 0;
    for (int y = 0; y < h; ++y) {
      for (int x = 0; x < w; ++x) {
        if (board[y][x] != 0) {
          ret++;
        }
      }
    }

    return ret;
  }

  private static void drop(int[][] board) {
    for (int x = 0; x < w; ++x) {
      dropCol(x, board);
    }
  }

  private static void dropCol(int x, int[][] board) {
    int pos = h - 1;
    for (int y = h - 1; y >= 0; --y) {
      if (board[y][x] == 0) {
        continue;
      }

      board[pos--][x] = board[y][x];
    }

    while (pos >= 0) {
      board[pos--][x] = 0;
    }
  }

  private static void boom(int y, int x, int power, int[][] board) {
    board[y][x] = 0;
    for (int p = 0; p < power; ++p) {
      for (int dir = 0; dir < 4; ++dir) {
        int ny = y + p * DY[dir];
        int nx = x + p * DX[dir];

        if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
          continue;
        }

        boom(ny, nx, board[ny][nx], board);
      }
    }
  }

  private static int findBombPos(int x, int[][] board) {
    for (int y = 0; y < h; ++y) {
      if (board[y][x] != 0) {
        return y;
      }
    }

    return -1;
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());
    h = Integer.parseInt(st.nextToken());

    board = new int[h][w];
    for (int y = 0; y < h; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }
  }


}

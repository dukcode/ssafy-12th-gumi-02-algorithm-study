import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BestCrossShapeBomb {

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

    int maxCnt = 0;
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        maxCnt = Math.max(maxCnt, boom(y, x));
      }
    }

    bw.write(String.valueOf(maxCnt));

    br.close();
    bw.close();
  }

  private static int boom(int y, int x) {
    int[][] tmpBoard = copy(board);
    int cnt = tmpBoard[y][x];
    for (int dir = 0; dir < 4; dir++) {
      for (int i = 0; i < cnt; ++i) {
        int ny = y + DY[dir] * i;
        int nx = x + DX[dir] * i;

        if (!inRange(ny, nx)) {
          break;
        }

        tmpBoard[ny][nx] = 0;
      }
    }

    drop(tmpBoard);

    return cntTuple(tmpBoard);
  }

  private static int cntTuple(int[][] board) {
    int cnt = 0;
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        if (board[y][x] == 0) {
          continue;
        }
        cnt += inRange(y, x + 1) && board[y][x] == board[y][x + 1] ? 1 : 0;
        cnt += inRange(y + 1, x) && board[y][x] == board[y + 1][x] ? 1 : 0;
      }
    }

    return cnt;
  }

  private static boolean inRange(int y, int x) {
    return 0 <= y && y < n && 0 <= x && x < n;
  }

  private static void drop(int[][] board) {
    for (int x = 0; x < n; ++x) {
      int pos = n - 1;
      for (int y = n - 1; y >= 0; --y) {
        if (board[y][x] == 0) {
          continue;
        }

        board[pos--][x] = board[y][x];
      }

      for (int y = pos; y >= 0; --y) {
        board[y][x] = 0;
      }
    }

  }

  private static int[][] copy(int[][] board) {
    int[][] ret = new int[n][n];
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        ret[y][x] = board[y][x];
      }
    }

    return ret;
  }


}

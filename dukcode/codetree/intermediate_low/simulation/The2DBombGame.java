import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class The2DBombGame {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int k;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    boom();
    for (int i = 0; i < k; ++i) {
      rotate();
      drop();
      boom();
    }

    bw.write(String.valueOf(cntBomb()));

    br.close();
    bw.close();
  }

  private static int cntBomb() {
    int cnt = 0;
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        cnt += board[y][x] != 0 ? 1 : 0;
      }
    }

    return cnt;
  }

  private static void boom() {
    for (int x = 0; x < n; ++x) {
      while (true) {
        if (!boomCol(x)) {
          break;
        }
      }
    }

  }

  private static boolean boomCol(int x) {
    boolean boomed = false;
    int pivot = board[n - 1][x];
    int pos = n - 1;
    int cnt = 0;
    for (int y = n - 1; y >= 0; --y) {
      if (board[y][x] == 0) {
        break;
      }

      if (board[y][x] == pivot) {
        cnt++;
        continue;
      }

      if (cnt < m) {
        for (int i = 0; i < cnt; ++i) {
          board[pos--][x] = pivot;
        }
      } else {
        boomed = true;
      }

      pivot = board[y][x];
      cnt = 1;
    }

    if (cnt < m) {
      for (int i = 0; i < cnt; ++i) {
        board[pos--][x] = pivot;
      }
    } else {
      boomed = true;
    }

    while (pos >= 0) {
      board[pos--][x] = 0;
    }

    return boomed;
  }

  private static void drop() {
    for (int x = 0; x < n; ++x) {
      int en = n - 1;
      for (int y = n - 1; y >= 0; --y) {
        if (board[y][x] == 0) {
          continue;
        }

        board[en--][x] = board[y][x];
      }

      for (int i = en; i >= 0; --i) {
        board[i][x] = 0;
      }
    }
  }

  private static void rotate() {
    for (int x = 0; x < n; ++x) {
      int s = 0;
      int e = n - 1;

      while (s < e) {
        int tmp = board[s][x];
        board[s][x] = board[e][x];
        board[e][x] = tmp;
        s++;
        e--;
      }
    }

    for (int y = 0; y < n; ++y) {
      for (int x = y + 1; x < n; ++x) {
        int tmp = board[y][x];
        board[y][x] = board[x][y];
        board[x][y] = tmp;
      }
    }
  }

}

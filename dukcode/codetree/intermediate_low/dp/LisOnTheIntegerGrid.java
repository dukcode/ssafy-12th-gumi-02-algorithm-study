import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class LisOnTheIntegerGrid {

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  private static int[][] cache;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());

    board = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    cache = new int[n][n];
    for (int y = 0; y < n; y++) {
      Arrays.fill(cache[y], -1);
    }

    int ret = 0;
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        ret = Math.max(ret, getMaxCnt(y, x));
      }
    }

    return ret;
  }

  private static int getMaxCnt(int y, int x) {
    if (cache[y][x] != -1) {
      return cache[y][x];
    }

    int ret = 1;
    for (int dir = 0; dir < 4; dir++) {
      int ny = y + DY[dir];
      int nx = x + DX[dir];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      if (board[ny][nx] <= board[y][x]) {
        continue;
      }

      ret = Math.max(ret, getMaxCnt(ny, nx) + 1);
    }

    return cache[y][x] = ret;
  }

}

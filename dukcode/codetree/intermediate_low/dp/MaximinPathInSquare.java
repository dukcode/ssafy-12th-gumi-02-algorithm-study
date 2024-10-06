import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MaximinPathInSquare {

  private static final int MX = 987_654_321;

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
    return getMaximin(0, 0);
  }

  private static int getMaximin(int y, int x) {
    if (y == n - 1 && x == n - 1) {
      return board[y][x];
    }

    if (cache[y][x] != 0) {
      return cache[y][x];
    }

    int ret = 0;
    for (int[] delta : new int[][]{{0, 1}, {1, 0}}) {
      int ny = y + delta[0];
      int nx = x + delta[1];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      ret = Math.max(ret, getMaximin(ny, nx));
    }

    return cache[y][x] = ret == 0 ? board[y][x] : Math.min(ret, board[y][x]);
  }


}

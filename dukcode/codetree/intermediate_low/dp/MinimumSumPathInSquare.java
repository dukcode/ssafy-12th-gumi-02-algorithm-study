import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MinimumSumPathInSquare {

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
    return getMinSum(0, n - 1);
  }

  private static int getMinSum(int y, int x) {
    if (y == n - 1 && x == 0) {
      return cache[y][x] = board[y][x];
    }

    if (cache[y][x] != 0) {
      return cache[y][x];
    }

    int ret = MX;
    for (int[] delta : new int[][]{{0, -1}, {1, 0}}) {
      int ny = y + delta[0];
      int nx = x + delta[1];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      ret = Math.min(ret, getMinSum(ny, nx) + board[y][x]);
    }

    return cache[y][x] = ret;
  }


}

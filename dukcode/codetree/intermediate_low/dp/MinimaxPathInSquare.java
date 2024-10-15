import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MinimaxPathInSquare {

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
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    cache = new int[n][n];
    bw.write(String.valueOf(getMinimax(n - 1, n - 1)));

    br.close();
    bw.close();
  }

  private static int getMinimax(int y, int x) {
    if (y == 0 && x == 0) {
      return board[y][x];
    }

    if (y < 0 || x < 0) {
      return MX;
    }

    if (cache[y][x] != 0) {
      return cache[y][x];
    }

    return cache[y][x] = Math.max(board[y][x],
        Math.min(getMinimax(y, x - 1), getMinimax(y - 1, x)));

  }

}

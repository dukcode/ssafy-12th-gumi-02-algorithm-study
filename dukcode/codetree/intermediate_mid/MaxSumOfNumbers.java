import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MaxSumOfNumbers {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;
  private static boolean[] taken;

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

    taken = new boolean[n];
    bw.write(String.valueOf(solve(0, 0)));

    br.close();
    bw.close();

  }

  private static int solve(int col, int sum) {
    if (col == n) {
      return sum;
    }

    int ret = 0;
    for (int row = 0; row < n; ++row) {
      if (taken[row]) {
        continue;
      }

      taken[row] = true;
      ret = Math.max(ret, solve(col + 1, sum + board[row][col]));
      taken[row] = false;
    }

    return ret;
  }

}

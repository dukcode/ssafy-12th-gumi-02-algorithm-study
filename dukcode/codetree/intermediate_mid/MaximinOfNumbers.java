import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MaximinOfNumbers {

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  private static boolean[] usedRow;

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

    usedRow = new boolean[n];
    bw.write(String.valueOf(solve(0, MX)));

    br.close();
    bw.close();

  }

  private static int solve(int col, int minVal) {
    if (col == n) {
      return minVal;
    }

    int ret = 0;
    for (int row = 0; row < n; row++) {
      if (usedRow[row]) {
        continue;
      }

      usedRow[row] = true;
      ret = Math.max(ret, solve(col + 1, Math.min(minVal, board[row][col])));
      usedRow[row] = false;
    }

    return ret;
  }


}

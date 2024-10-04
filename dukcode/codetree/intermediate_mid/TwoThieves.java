import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class TwoThieves {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int c;

  private static int[][] board;

  private static int[][] maxValues;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    c = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    int size = n - m + 1;
    maxValues = new int[n][size];
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < size; x++) {
        maxValues[y][x] = getMaxValue(y, x, 0, 0, 0);
      }
    }

    int ans = 0;
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < size; x++) {

        int val = maxValues[y][x];

        for (int c = x + m; c < size; c++) {
          ans = Math.max(ans, val + maxValues[y][c]);
        }

        for (int r = y + 1; r < n; r++) {
          for (int c = 0; c < size; c++) {
            ans = Math.max(ans, val + maxValues[r][c]);
          }
        }
      }
    }

    bw.write(String.valueOf(ans));

    br.close();
    bw.close();

  }

  private static int getMaxValue(int y, int x, int idx, int sumWeight, int sumValue) {
    if (idx == m) {
      if (sumWeight > c) {
        return 0;
      }
      return sumValue;
    }

    int ret = getMaxValue(y, x, idx + 1, sumWeight, sumValue);

    if (x + idx >= n) {
      return ret;
    }

    int weight = board[y][x + idx];
    ret = Math.max(ret, getMaxValue(y, x, idx + 1, sumWeight + weight, sumValue + weight * weight));
    return ret;
  }

}

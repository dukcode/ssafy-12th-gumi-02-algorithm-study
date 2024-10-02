import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class GoldMining {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = 0;
    for (int k = 0; k <= 2 * (n - 1); ++k) {
      int numArea = cntArea(k);
      for (int y = 0; y < n; ++y) {
        for (int x = 0; x < n; ++x) {
          int numCoins = cntCoins(y, x, k);
          if (numArea <= m * numCoins) {
            ret = Math.max(ret, numCoins);
          }
        }
      }
    }
    return ret;
  }

  private static int cntCoins(int cy, int cx, int k) {
    int ret = 0;
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        if (Math.abs(x - cx) + Math.abs(y - cy) <= k) {
          ret += board[y][x];
        }
      }
    }

    return ret;
  }

  private static int cntArea(int k) {
    return k * k + (k + 1) * (k + 1);
  }


}

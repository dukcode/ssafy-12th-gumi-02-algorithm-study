import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MinimumDifferenceOnTheGrid2 {

  private static final int MX = 987_654_321;
  private static final int MX_NUM = 100;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  private static int[][][] cache;

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

    cache = new int[MX_NUM + 1][n][n];
    for (int k = 1; k <= MX_NUM; k++) {
      for (int y = 0; y < n; y++) {
        for (int x = 0; x < n; x++) {
          cache[k][y][x] = MX;
        }
      }
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  public static int solve() {
    cache[board[0][0]][0][0] = board[0][0]; // 맨 왼쪽 위는 특별히 초기화
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        for (int k = 1; k <= MX_NUM; k++) { // 꼭 안쪽에 있어야 됨 순서 중요 dp가 어느 이전의 dp를 이용하는지 잘
          if (k == board[0][0] && y == 0 && x == 0) {
            continue;
          }
          int minValue = Math.min(k, board[y][x]);

          int upperMaxValue = inRange(y - 1, x) ? cache[k][y - 1][x] : MX;
          int leftMaxValue = inRange(y, x - 1) ? cache[k][y][x - 1] : MX;

          int selectedMaxValue = Math.min(leftMaxValue, upperMaxValue);

          int maxValue = Math.max(selectedMaxValue, board[y][x]);

          cache[minValue][y][x] = Math.min(cache[minValue][y][x], maxValue);
        }
      }
    }

    int ret = MX;
    for (int k = 1; k <= MX_NUM; k++) {
      if (cache[k][n - 1][n - 1] == MX) {
        continue;
      }

      ret = Math.min(ret, cache[k][n - 1][n - 1] - k);
    }

    return ret;
  }

  private static boolean inRange(int y, int x) {
    return y >= 0 && y < n && x >= 0 && x < n;
  }

}

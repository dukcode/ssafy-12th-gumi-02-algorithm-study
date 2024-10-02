import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class SlantedRectangle {

  private static final int[] DELTA_Y = {-1, -1, 1, 1};
  private static final int[] DELTA_X = {1, -1, -1, 1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

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

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = 0;
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        ret = Math.max(ret, cntMaxSum(y, x));
      }
    }

    return ret;
  }

  private static int cntMaxSum(int sy, int sx) {
    int maxSum = 0;
    for (int h = 1; h < n; ++h) {
      for (int w = 1; w < n; ++w) {
        maxSum = Math.max(maxSum, cntSum(sy, sx, h, w));
      }
    }

    return maxSum;
  }

  private static int cntSum(int y, int x, int h, int w) {
    int[] moves = {h, w, h, w};

    int sum = 0;
    for (int dir = 0; dir < 4; ++dir) {
      for (int i = 0; i < moves[dir]; ++i) {
        y += DELTA_Y[dir];
        x += DELTA_X[dir];

        if (!inRange(y, x)) {
          return 0;
        }

        sum += board[y][x];
      }
    }

    return sum;
  }

  private static boolean inRange(int y, int x) {
    return y >= 0 && y < n && x >= 0 && x < n;
  }


}

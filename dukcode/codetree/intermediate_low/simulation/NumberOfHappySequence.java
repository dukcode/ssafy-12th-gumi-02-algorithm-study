import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class NumberOfHappySequence {

  private static final int[] DELTA_Y = {0, 1};
  private static final int[] DELTA_X = {1, 0};

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
    for (int i = 0; i < n; ++i) {
      if (isHappy(board[i])) {
        ret++;
      }

      int[] col = new int[n];
      for (int j = 0; j < n; ++j) {
        col[j] = board[j][i];
      }

      if (isHappy(col)) {
        ret++;
      }
    }

    return ret;
  }

  private static boolean isHappy(int[] arr) {
    int pivot = arr[0];
    int maxCnt = 0;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
      if (pivot == arr[i]) {
        cnt++;
        continue;
      }

      maxCnt = Math.max(maxCnt, cnt);
      cnt = 1;
      pivot = arr[i];
    }

    maxCnt = Math.max(maxCnt, cnt);

    return maxCnt >= m;
  }


}

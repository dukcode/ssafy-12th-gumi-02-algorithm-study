import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class MaxMovementsWithDirection {

  private static final int[] DY = {0, -1, -1, 0, 1, 1, 1, 0, -1};
  private static final int[] DX = {0, 0, 1, 1, 1, 0, -1, -1, -1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] nums;
  private static int[][] dirs;

  private static int r;
  private static int c;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    n = Integer.parseInt(br.readLine());
    nums = inputArr();
    dirs = inputArr();

    st = new StringTokenizer(br.readLine());
    r = Integer.parseInt(st.nextToken()) - 1;
    c = Integer.parseInt(st.nextToken()) - 1;

    bw.write(String.valueOf(solve(r, c, 0)));

    br.close();
    bw.close();

  }

  private static int solve(int r, int c, int cnt) {
    int ret = cnt;
    int pivot = nums[r][c];
    int dir = dirs[r][c];
    while (true) {
      int nr = r + DY[dir];
      int nc = c + DX[dir];

      if (!inRange(nr, nc)) {
        break;
      }

      if (nums[nr][nc] > pivot) {
        ret = Math.max(ret, solve(nr, nc, cnt + 1));
      }

      r = nr;
      c = nc;
    }

    return ret;
  }

  private static boolean inRange(int r, int c) {
    return r >= 0 && r < n && c >= 0 && c < n;
  }

  private static int[][] inputArr() throws IOException {
    int[][] ret = new int[n][n];
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        ret[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    return ret;
  }

}

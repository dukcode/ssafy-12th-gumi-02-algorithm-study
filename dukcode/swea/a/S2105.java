import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

// 디저트 카페
public class S2105 {

  private static final int[] DY = {1, 1, -1, -1};
  private static final int[] DX = {1, -1, -1, 1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      n = Integer.parseInt(br.readLine());

      board = new int[n][n];
      for (int y = 0; y < n; ++y) {
        st = new StringTokenizer(br.readLine());
        for (int x = 0; x < n; ++x) {
          board[x][y] = Integer.parseInt(st.nextToken());
        }
      }

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int solve() {
    int ret = -1;
    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        ret = Math.max(ret, cntDessert(y, x));
      }
    }

    return ret;
  }

  private static int cntDessert(int y, int x) {
    int ret = -1;
    for (int h = 1; h <= n; ++h) {
      for (int w = 1; w <= n; ++w) {
        int maxY = y + h + w;
        int minX = x - h;
        int maxX = x + w;

        if (maxY >= n || minX < 0 || maxX >= n) {
          continue;
        }

        ret = Math.max(ret, cntDessert(y, x, h, w));
      }
    }

    return ret;
  }

  private static int cntDessert(int y, int x, int h, int w) {
    Set<Integer> set = new HashSet<>();

    int[] len = new int[]{w, h, w, h};
    for (int dir = 0; dir < 4; ++dir) {
      for (int i = 0; i < len[dir]; ++i) {
        y += DY[dir];
        x += DX[dir];

        if (set.contains(board[y][x])) {
          return -1;
        }

        set.add(board[y][x]);
      }
    }

    return set.size();
  }


}

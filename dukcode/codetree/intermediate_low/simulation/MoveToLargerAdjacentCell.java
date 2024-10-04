import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class MoveToLargerAdjacentCell {

  // 우좌하상
  private static final int[] DY = {0, 0, 1, -1};
  private static final int[] DX = {1, -1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int r;
  private static int c;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    r = Integer.parseInt(st.nextToken()) - 1;
    c = Integer.parseInt(st.nextToken()) - 1;

    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    List<Integer> ans = solve();
    for (Integer num : ans) {
      bw.write(String.valueOf(num));
      bw.write(' ');
    }

    br.close();
    bw.close();
  }

  private static List<Integer> solve() {
    List<Integer> ret = new ArrayList<>();
    int y = r;
    int x = c;

    ret.add(board[y][x]);

    while (true) {
      boolean canMove = false;
      int dirToMove = -1;
      for (int dir = 0; dir < 4; dir++) {
        int ny = y + DY[dir];
        int nx = x + DX[dir];

        if (!inRange(ny, nx)) {
          continue;
        }

        if (board[y][x] >= board[ny][nx]) {
          continue;
        }

        dirToMove = dir;
        canMove = true;
      }

      if (!canMove) {
        break;
      }

      y += DY[dirToMove];
      x += DX[dirToMove];
      ret.add(board[y][x]);
    }

    return ret;
  }

  private static boolean inRange(int y, int x) {
    return x >= 0 && x < n && y >= 0 && y < n;
  }

}

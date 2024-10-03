import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class SeperateVillage {

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static final int WALL = 0;
  private static final int PERSON = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int[][] board;

  private static boolean[][] visited;

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

    visited = new boolean[n][n];
    List<Integer> ans = dfsAll();

    bw.write(String.valueOf(ans.size()));
    bw.newLine();
    for (int cnt : ans) {
      bw.write(String.valueOf(cnt));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static List<Integer> dfsAll() {
    List<Integer> ret = new ArrayList<>();
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        if (visited[y][x] || board[y][x] == WALL) {
          continue;
        }

        ret.add(dfs(y, x));
      }
    }

    Collections.sort(ret);
    return ret;
  }

  private static int dfs(int y, int x) {
    visited[y][x] = true;

    int cnt = 1;
    for (int dir = 0; dir < 4; ++dir) {
      int ny = y + DY[dir];
      int nx = x + DX[dir];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      if (visited[ny][nx] || board[ny][nx] == WALL) {
        continue;
      }

      cnt += dfs(ny, nx);
    }

    return cnt;
  }

}

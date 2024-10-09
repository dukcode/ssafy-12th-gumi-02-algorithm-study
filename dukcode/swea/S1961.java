import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 정사각형 방
public class S1961 {

  private static final int MX = 987_654_321;

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int[][] rooms;

  private static boolean[][] visited;

  private static int maxDist;
  private static int minRoomNum;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      n = Integer.parseInt(br.readLine());
      rooms = new int[n][n];
      for (int y = 0; y < n; y++) {
        st = new StringTokenizer(br.readLine());
        for (int x = 0; x < n; x++) {
          rooms[y][x] = Integer.parseInt(st.nextToken());
        }
      }

      maxDist = 0;
      minRoomNum = MX;
      visited = new boolean[n][n];
      solve();

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(minRoomNum));
      bw.write(' ');
      bw.write(String.valueOf(maxDist));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static void solve() {
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        dfs(y, x, 1, rooms[y][x]);
      }
    }
  }

  private static void dfs(int y, int x, int dist, int start) {
    visited[y][x] = true;

    if (dist >= maxDist) {
      if (dist == maxDist) {
        minRoomNum = Math.min(minRoomNum, start);
      } else {
        minRoomNum = start;
      }

      maxDist = dist;
    }

    for (int dir = 0; dir < 4; dir++) {
      int ny = y + DY[dir];
      int nx = x + DX[dir];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      if (rooms[ny][nx] != rooms[y][x] + 1) {
        continue;
      }

      dfs(ny, nx, dist + 1, start);
    }

    visited[y][x] = false;
  }

}

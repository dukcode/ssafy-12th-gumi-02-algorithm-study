import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class StayOutOfRain {

  private static final int MX = 987_654_321;

  private static final int[] DY = {-1, 1, 0, 0};
  private static final int[] DX = {0, 0, -1, 1};

  private static final int BLANK = 0;
  private static final int WALL = 1;
  private static final int PERSON = 2;
  private static final int SAFE = 3;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int h;
  private static int m;
  private static int[][] board;

  private static List<Point> safeZones;
  private static List<Point> people;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    h = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    safeZones = new ArrayList<>();
    people = new ArrayList<>();
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        int block = Integer.parseInt(st.nextToken());

        if (block == SAFE) {
          safeZones.add(new Point(y, x));
        }

        if (block == PERSON) {
          people.add(new Point(y, x));
        }

        board[y][x] = block;
      }
    }

    int[][] ans = solve();
    for (int y = 0; y < n; y++) {
      for (int x = 0; x < n; x++) {
        bw.write(String.valueOf(ans[y][x]));
        bw.write(' ');
      }
      bw.newLine();
    }
    bw.newLine();

    br.close();
    bw.close();

  }

  private static int[][] solve() {
    int[][] dist = getMinDist();
    int[][] ret = new int[n][n];

    for (Point person : people) {
      ret[person.y][person.x] = dist[person.y][person.x] - 1;
    }

    return ret;
  }

  private static int[][] getMinDist() {
    int[][] dist = new int[n][n];
    Queue<Point> q = new ArrayDeque<>();

    for (Point safeZone : safeZones) {
      q.offer(safeZone);
      dist[safeZone.y][safeZone.x] = 1;
    }

    while (!q.isEmpty()) {
      Point cur = q.poll();

      for (int dir = 0; dir < 4; dir++) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (board[ny][nx] == WALL || dist[ny][nx] != 0) {
          continue;
        }

        dist[ny][nx] = dist[cur.y][cur.x] + 1;
        q.offer(new Point(ny, nx));
      }
    }

    return dist;
  }

  private static class Point {

    int y;
    int x;

    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

}

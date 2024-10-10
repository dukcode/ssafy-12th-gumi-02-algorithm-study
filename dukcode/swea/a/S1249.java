import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// 보급로
public class S1249 {

  private static final int MX = 987_654_321;

  private static int[] DY = {0, 0, -1, 1};
  private static int[] DX = {-1, 1, 0, 0};

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
        char[] line = br.readLine().toCharArray();
        for (int x = 0; x < n; ++x) {
          board[y][x] = line[x] - '0';
        }
      }
      bw.write("#" + tc + " ");
      bw.write(String.valueOf(getMinCost(0, 0)));
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static int getMinCost(int y, int x) {
    int[][] cost = new int[n][n];
    for (int i = 0; i < n; i++) {
      Arrays.fill(cost[i], MX);
    }

    PriorityQueue<Point> pq = new PriorityQueue<>((a, b) -> a.cost - b.cost);
    pq.offer(new Point(y, x, board[y][x]));
    cost[y][x] = board[y][x];

    while (!pq.isEmpty()) {
      Point cur = pq.poll();
      for (int dir = 0; dir < 4; dir++) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        int nextCost = cur.cost + board[ny][nx];
        if (cost[ny][nx] <= nextCost) {
          continue;
        }

        cost[ny][nx] = nextCost;
        pq.offer(new Point(ny, nx, nextCost));

      }
    }

    return cost[n - 1][n - 1];
  }

  private static class Point {

    int y;
    int x;
    int cost;

    public Point(int y, int x, int cost) {
      this.y = y;
      this.x = x;
      this.cost = cost;
    }

  }
}

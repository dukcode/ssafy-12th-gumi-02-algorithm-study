import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

/*
다리 만들기 2
 */
public class B17472 {

  private static final int[] DELTA_Y = {0, 0, -1, 1};
  private static final int[] DELTA_X = {-1, 1, 0, 0};

  private static final int MX = 987_654_321;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static int[][] board;
  private static int[][] island;

  private static int cntIsland;
  private static int[][] adj;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());

    board = new int[h][w];
    for (int y = 0; y < h; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    island = new int[h][w];
    cntIsland = findIsland();

    adj = new int[cntIsland + 1][cntIsland + 1];
    for (int y = 0; y <= cntIsland; ++y) {
      Arrays.fill(adj[y], MX);
    }
    makeGraph();

    bw.write(String.valueOf(prim()));

    br.close();
    bw.close();

  }

  private static int prim() {
    int ret = 0;
    int visCnt = 0;

    boolean[] vis = new boolean[cntIsland + 1];

    int start = 1;
    PriorityQueue<VisInfo> pq = new PriorityQueue<>(Comparator.comparingInt(i -> i.distBefore));
    pq.offer(new VisInfo(start, 0));

    while (!pq.isEmpty()) {
      VisInfo cur = pq.poll();
      int here = cur.numNode;

      if (vis[here]) {
        continue;
      }

      vis[here] = true;
      visCnt++;
      ret += cur.distBefore;

      for (int there = 1; there <= cntIsland; ++there) {
        if (vis[there] || adj[here][there] == MX) {
          continue;
        }

        pq.offer(new VisInfo(there, adj[here][there]));
      }
    }

    if (ret == 0 || visCnt != cntIsland) {
      return -1;
    }

    return ret;
  }

  private static void makeGraph() {
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        if (island[y][x] == 0) {
          continue;
        }
        for (int dir = 0; dir < 4; ++dir) {
          int sy = y;
          int sx = x;
          int pivot = island[sy][sx];
          int dist = 0;
          while (true) {
            dist++;
            int ny = sy + DELTA_Y[dir];
            int nx = sx + DELTA_X[dir];

            if (outOfRange(ny, nx) || island[ny][nx] == pivot) {
              break;
            }

            if (island[ny][nx] == 0) {
              sy = ny;
              sx = nx;
              continue;
            }

            if (dist - 1 <= 1) {
              break;
            }

            adj[island[ny][nx]][pivot] =
                adj[pivot][island[ny][nx]] =
                    Math.min(adj[pivot][island[ny][nx]], dist - 1);
            break;
          }
        }
      }
    }
  }

  private static int findIsland() {
    int seq = 0;
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        if (board[y][x] == 0 || island[y][x] != 0) {
          continue;
        }

        seq++;
        Queue<Point> q = new ArrayDeque<>();
        q.offer(new Point(y, x));
        island[y][x] = seq;
        while (!q.isEmpty()) {
          Point cur = q.poll();
          for (int dir = 0; dir < 4; ++dir) {
            int ny = cur.y + DELTA_Y[dir];
            int nx = cur.x + DELTA_X[dir];

            if (outOfRange(ny, nx)) {
              continue;
            }

            if (board[ny][nx] == 0 || island[ny][nx] != 0) {
              continue;
            }

            island[ny][nx] = seq;
            q.offer(new Point(ny, nx));
          }
        }
      }
    }

    return seq;
  }

  private static boolean outOfRange(int y, int x) {
    return y < 0 || y >= h || x < 0 || x >= w;
  }

  private static class Point {

    int y;
    int x;

    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }
  }

  private static class VisInfo {

    int numNode;
    int distBefore;

    public VisInfo(int numNode, int distBefore) {
      this.numNode = numNode;
      this.distBefore = distBefore;
    }
  }

}

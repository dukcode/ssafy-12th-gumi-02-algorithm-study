import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// 나무 베기
public class S22683 {

  private static final int MX = 987_654_321;

  private static final char GROUND = 'G';
  private static final char TREE = 'T';
  private static final int START = 'X';
  private static final int END = 'Y';

  // 상 우 하 좌
  private static final int[] DY = {-1, 0, 1, 0};
  private static final int[] DX = {0, 1, 0, -1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int n;
  private static int k;

  private static char[][] board;

  private static Point start;
  private static Point end;
  private static List<Point> trees;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; ++tc) {
      input();
      int minMoveCnt = solve();
      output(tc, minMoveCnt);
    }

    br.close();
    bw.close();

  }

  private static int solve() {
    int ret = getMinMove(-1, 0);
    return ret == MX ? -1 : ret;
  }

  private static int getMinMove(int lastIdx, int cnt) {
    if (cnt == k || cnt == trees.size()) {
      return calcDist();
    }

    int ret = MX;
    for (int nextIdx = lastIdx + 1; nextIdx < trees.size(); ++nextIdx) {
      Point tree = trees.get(nextIdx);
      board[tree.y][tree.x] = GROUND;
      ret = Math.min(ret, getMinMove(nextIdx, cnt + 1));
      board[tree.y][tree.x] = TREE;
    }

    return ret;
  }

  private static int calcDist() {
    int[][][] cost = new int[4][n][n];
    for (int dir = 0; dir < 4; ++dir) {
      for (int y = 0; y < n; y++) {
        Arrays.fill(cost[dir][y], MX);
      }
    }

    Queue<Point> q = new ArrayDeque<>();
    q.offer(start);
    cost[start.dir][start.y][start.x] = 0;

    while (!q.isEmpty()) {
      Point cur = q.poll();

      if (cur.equals(end)) {
        continue;
      }

      for (int rotate : new int[]{-1, 1}) {
        int nDir = (cur.dir + rotate + 4) % 4;

        int nextCost = cost[cur.dir][cur.y][cur.x] + 1;
        if (cost[nDir][cur.y][cur.x] <= nextCost) {
          continue;
        }

        cost[nDir][cur.y][cur.x] = nextCost;
        q.offer(new Point(nDir, cur.y, cur.x));
      }

      int ny = cur.y + DY[cur.dir];
      int nx = cur.x + DX[cur.dir];

      if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
        continue;
      }

      if (board[ny][nx] == TREE) {
        continue;
      }

      if (cost[cur.dir][ny][nx] <= cost[cur.dir][cur.y][cur.x] + 1) {
        continue;
      }

      cost[cur.dir][ny][nx] = cost[cur.dir][cur.y][cur.x] + 1;
      q.offer(new Point(cur.dir, ny, nx));
    }

    int ret = MX;
    for (int dir = 0; dir < 4; ++dir) {
      ret = Math.min(ret, cost[dir][end.y][end.x]);
    }

    return ret;
  }

  private static void output(int tc, int ans) throws IOException {
    bw.write("#" + tc + " ");
    bw.write(String.valueOf(ans));
    bw.newLine();
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new char[n][n];
    trees = new ArrayList<>();
    for (int y = 0; y < n; y++) {
      char[] line = br.readLine().toCharArray();
      for (int x = 0; x < n; x++) {
        char block = line[x];

        if (block == START) {
          board[y][x] = GROUND;
          start = new Point(0, y, x);
          continue;
        }

        if (block == END) {
          board[y][x] = GROUND;
          end = new Point(y, x);
          continue;
        }

        if (block == TREE) {
          trees.add(new Point(y, x));
        }

        board[y][x] = block;
      }
    }
  }

  private static class Point {

    int dir;
    int y;
    int x;

    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }

    public Point(int dir, int y, int x) {
      this.dir = dir;
      this.y = y;
      this.x = x;
    }

    public boolean equals(Point point) {
      return y == point.y && x == point.x;
    }
  }
}

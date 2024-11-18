import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// 백조
public class B3197 {

  private static final char SWAN = 'L';
  private static final char GLACIER = 'X';
  private static final char WATER = '.';

  private static final int[] DY = {-1, 1, 0, 0};
  private static final int[] DX = {0, 0, -1, 1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static char[][] board;

  private static boolean[][] waterVis;
  private static boolean[][] swanVis;

  private static List<Point> swans;

  private static Point start;
  private static Point end;

  private static Queue<Point> waterQueue;
  private static Queue<Point> swanQueue;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());

    board = new char[h][w];
    waterVis = new boolean[h][w];
    waterQueue = new LinkedList<>();
    swans = new ArrayList<>();

    for (int y = 0; y < h; y++) {
      String line = br.readLine();
      for (int x = 0; x < w; x++) {
        char block = line.charAt(x);
        board[y][x] = block;

        if (block == GLACIER) {
          continue;
        }

        waterQueue.add(new Point(y, x));
        if (block == SWAN) {
          swans.add(new Point(y, x));
        }

      }
    }

    swanVis = new boolean[h][w];

    start = swans.get(0);
    end = swans.get(1);

    swanQueue = new LinkedList<>();
    swanQueue.offer(start);

    swanVis[start.y][start.x] = true;

    int cnt = 0;
    while (!canMeet()) {
      melt();
      cnt++;
    }

    bw.write(String.valueOf(cnt));

    br.close();
    bw.close();

  }

  private static boolean canMeet() {
    Queue<Point> nextQ = new LinkedList<>();
    while (!swanQueue.isEmpty()) {
      Point here = swanQueue.poll();

      if (here.equals(end)) {
        return true;
      }

      for (int dir = 0; dir < 4; ++dir) {
        int ny = here.y + DY[dir];
        int nx = here.x + DX[dir];

        if (outOfRange(ny, nx)) {
          continue;
        }

        if (swanVis[ny][nx]) {
          continue;
        }

        swanVis[ny][nx] = true;
        if (board[ny][nx] == GLACIER) {
          nextQ.offer(new Point(ny, nx));
        } else {
          swanQueue.offer(new Point(ny, nx));
        }

      }
    }

    swanQueue = nextQ;

    return false;
  }

  private static void melt() {
    Queue<Point> nextQ = new LinkedList<>();
    while (!waterQueue.isEmpty()) {
      Point here = waterQueue.poll();
      for (int dir = 0; dir < 4; ++dir) {
        int ny = here.y + DY[dir];
        int nx = here.x + DX[dir];

        if (outOfRange(ny, nx)) {
          continue;
        }

        if (waterVis[ny][nx]) {
          continue;
        }

        waterVis[ny][nx] = true;
        if (board[ny][nx] == GLACIER) {
          nextQ.offer(new Point(ny, nx));
        } else {
          waterQueue.offer(new Point(ny, nx));
        }
      }
    }

    for (Point point : nextQ) {
      waterQueue.offer(point);
      board[point.y][point.x] = WATER;
    }
  }

  private static boolean outOfRange(int y, int x) {
    return 0 > y || y >= h || 0 > x || x >= w;
  }

  private static class Point {

    int y;
    int x;

    public Point(int y, int x) {
      this.y = y;
      this.x = x;
    }

    public boolean equals(Point other) {
      return y == other.y && x == other.x;
    }
  }
}

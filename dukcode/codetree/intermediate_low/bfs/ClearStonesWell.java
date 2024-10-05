import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class ClearStonesWell {

  private static final int[] DY = {-1, 0, 0, 1};
  private static final int[] DX = {0, -1, 1, 0};

  private static final int STONE = 1;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int k;
  private static int m;

  private static int[][] board;
  private static List<Point> stones;

  private static List<Point> starts;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    board = new int[n][n];
    stones = new ArrayList<>();
    for (int y = 0; y < n; y++) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; x++) {
        board[y][x] = Integer.parseInt(st.nextToken());
        if (board[y][x] == STONE) {
          stones.add(new Point(y, x));
        }
      }
    }

    starts = new ArrayList<>();
    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(br.readLine());
      int r = Integer.parseInt(st.nextToken()) - 1;
      int c = Integer.parseInt(st.nextToken()) - 1;
      starts.add(new Point(r, c));
    }

    bw.write(String.valueOf(solve()));

    br.close();
    bw.close();

  }

  private static int solve() {
    int cntStone = stones.size();
    int[] cleared = new int[cntStone];
    Arrays.fill(cleared, cntStone - m, cntStone, 1);

    int ret = 0;
    do {
      ret = Math.max(ret, cntCanGo(cleared));
    } while (nextPermutation(cleared));

    return ret;
  }

  private static int cntCanGo(int[] cleared) {
    clearStones(cleared, -1);
    int cnt = cntCanGo();
    clearStones(cleared, 1);
    return cnt;
  }

  private static int cntCanGo() {
    boolean[][] discovered = new boolean[n][n];

    Stack<Point> stk = new Stack<>();
    for (Point start : starts) {
      stk.push(start);
      discovered[start.y][start.x] = true;
    }

    int cnt = 0;
    while (!stk.isEmpty()) {
      Point cur = stk.pop();
      cnt++;

      for (int dir = 0; dir < 4; ++dir) {
        int ny = cur.y + DY[dir];
        int nx = cur.x + DX[dir];

        if (ny < 0 || ny >= n || nx < 0 || nx >= n) {
          continue;
        }

        if (discovered[ny][nx] || board[ny][nx] == STONE) {
          continue;
        }

        stk.push(new Point(ny, nx));
        discovered[ny][nx] = true;
      }
    }

    return cnt;
  }

  private static void clearStones(int[] cleared, int delta) {
    for (int i = 0; i < cleared.length; i++) {
      if (cleared[i] == 1) {
        Point stone = stones.get(i);
        board[stone.y][stone.x] = delta;
      }
    }
  }

  private static boolean nextPermutation(int[] arr) {
    int n = arr.length;

    if (n == 1) {
      return false;
    }

    int st = n - 2;
    while (0 <= st && arr[st] >= arr[st + 1]) {
      st--;
    }

    if (st < 0) {
      return false;
    }

    int en = n - 1;
    while (st < en && arr[st] >= arr[en]) {
      en--;
    }

    swap(arr, st, en);

    int s = st + 1;
    int e = n - 1;
    while (s < e) {
      swap(arr, s++, e--);
    }

    return true;

  }

  private static void swap(int[] arr, int a, int b) {
    int tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
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

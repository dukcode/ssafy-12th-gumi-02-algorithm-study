import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

// 줄기 세포 배양
public class S5653 {

  private static final int[] DY = {0, 0, -1, 1};
  private static final int[] DX = {-1, 1, 0, 0};

  private static final int INACTIVE = 0;
  private static final int ACTIVE = 1;
  private static final int DEAD = 2;

  private static final int MX = 500;

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int t;

  private static int h;
  private static int w;
  private static int k;

  private static Cell[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    t = Integer.parseInt(br.readLine());
    for (int tc = 1; tc <= t; tc++) {
      input();

      bw.write("#" + tc + " ");
      bw.write(String.valueOf(solve()));
      bw.newLine();
    }

    br.close();
    bw.close();
  }


  private static void next() {

    boolean[][] isNew = new boolean[MX][MX];

    for (int y = 0; y < MX; ++y) {
      for (int x = 0; x < MX; ++x) {
        if (board[y][x] == null || isNew[y][x]) {
          continue;
        }

        if (board[y][x].pregnant()) {
          for (int dir = 0; dir < 4; ++dir) {
            int ny = y + DY[dir];
            int nx = x + DX[dir];

            if (board[ny][nx] == null || (isNew[ny][nx] && board[ny][nx].x < board[y][x].x)) {
              isNew[ny][nx] = true;
              board[ny][nx] = new Cell(board[y][x].x);
            }
          }
        }

        board[y][x].next();

      }
    }
  }


  private static int cntCellNotDead() {
    int ret = 0;
    for (int y = 0; y < MX; ++y) {
      for (int x = 0; x < MX; ++x) {
        if (board[y][x] == null || board[y][x].isDead()) {
          continue;
        }

        ret++;
      }
    }

    return ret;
  }

  private static int solve() {

    for (int time = 1; time <= k; time++) {

      next();

    }

    return cntCellNotDead();
  }

  private static void input() throws IOException {
    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken());

    board = new Cell[MX][MX];
    for (int y = 0; y < h; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; ++x) {
        int t = Integer.parseInt(st.nextToken());
        if (t == 0) {
          continue;
        }
        Cell cell = new Cell(t);
        board[y + 200][x + 200] = cell;
      }
    }
  }

  private static class Cell {

    final int x;
    int status;
    int time;

    public Cell(int x) {
      this.x = x;
      this.status = INACTIVE;
      this.time = x;
    }

    public void next() {
      if (status == DEAD) {
        return;
      }

      time--;

      if (time == 0) {
        status++;
        time = x;
      }
    }

    public boolean isDead() {
      return status == DEAD;
    }

    public boolean pregnant() {
      return time == x && status == ACTIVE;
    }
  }

}

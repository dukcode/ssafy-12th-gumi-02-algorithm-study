import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class The2DWindBlows {

  private static final int[] DELTA_Y = {0, 0, -1, 1};
  private static final int[] DELTA_X = {-1, 1, 0, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int q;
  private static int h;
  private static int w;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    h = Integer.parseInt(st.nextToken());
    w = Integer.parseInt(st.nextToken());
    q = Integer.parseInt(st.nextToken());

    board = new int[h][w];
    for (int y = 0; y < h; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < w; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    for (int i = 0; i < q; i++) {
      st = new StringTokenizer(br.readLine());
      int y1 = Integer.parseInt(st.nextToken()) - 1;
      int x1 = Integer.parseInt(st.nextToken()) - 1;
      int y2 = Integer.parseInt(st.nextToken()) - 1;
      int x2 = Integer.parseInt(st.nextToken()) - 1;

      blow(y1, x1, y2, x2);
    }

    print();

    br.close();
    bw.close();
  }

  private static void print() throws IOException {
    for (int y = 0; y < h; ++y) {
      for (int x = 0; x < w; ++x) {
        bw.write(String.valueOf(board[y][x]));
        bw.write(' ');
      }
      bw.newLine();
    }
    bw.newLine();
  }

  private static void blow(int y1, int x1, int y2, int x2) {
    rotate(y1, x1, y2, x2);
    changToAvg(y1, x1, y2, x2);
  }

  private static void changToAvg(int y1, int x1, int y2, int x2) {
    int[][] tmpBoard = new int[y2 - y1 + 1][x2 - x1 + 1];
    for (int y = y1; y <= y2; ++y) {
      for (int x = x1; x <= x2; ++x) {
        tmpBoard[y - y1][x - x1] = getAvg(y, x);
      }
    }

    for (int y = y1; y <= y2; ++y) {
      System.arraycopy(tmpBoard[y - y1], 0, board[y], x1, x2 - x1 + 1);
    }
  }

  private static int getAvg(int y, int x) {
    int sum = board[y][x];
    int cnt = 1;
    for (int dir = 0; dir < 4; ++dir) {
      int ny = y + DELTA_Y[dir];
      int nx = x + DELTA_X[dir];

      if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
        continue;
      }

      cnt++;
      sum += board[ny][nx];
    }

    return sum / cnt;
  }

  private static void rotate(int y1, int x1, int y2, int x2) {
    int tmp = board[y1][x2];

    for (int x = x2; x > x1; --x) {
      board[y1][x] = board[y1][x - 1];
    }

    for (int y = y1; y < y2; ++y) {
      board[y][x1] = board[y + 1][x1];
    }

    for (int x = x1; x < x2; ++x) {
      board[y2][x] = board[y2][x + 1];
    }

    for (int y = y2; y > y1; --y) {
      board[y][x2] = board[y - 1][x2];
    }

    board[y1 + 1][x2] = tmp;
  }


}

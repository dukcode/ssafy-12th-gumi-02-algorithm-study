import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class OneTrialOf2048Game {

  private static final int N = 4;
  private static final int NONE = -1;

  // R U L D
  private static final int[] DY = {0, -1, 0, 1};
  private static final int[] DX = {1, 0, -1, 0};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    board = new int[N][N];
    for (int y = 0; y < N; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < N; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    String command = br.readLine();
    int dir = getDir(command);
    move(dir);

    for (int y = 0; y < N; ++y) {
      for (int x = 0; x < N; ++x) {
        bw.write(String.valueOf(board[y][x]));
        bw.write(' ');
      }
      bw.newLine();
    }

    br.close();
    bw.close();
  }


  private static void move(int dir) {
    rotate(dir);
    moveRight();
    rotate(4 - dir);
  }

  private static void moveRight() {
    for (int y = 0; y < N; ++y) {
      moveLineRight(y);
    }
  }

  private static void moveLineRight(int y) {
    int[] tmp = new int[N];
    int keep = NONE;
    int pos = N - 1;
    for (int i = N - 1; i >= 0; --i) {
      if (board[y][i] == 0) {
        continue;
      }

      if (keep == NONE) {
        keep = board[y][i];
        continue;
      }

      if (board[y][i] == keep) {
        tmp[pos--] = keep * 2;
        keep = NONE;
        continue;
      }

      tmp[pos--] = keep;
      keep = board[y][i];
    }

    if (keep != NONE) {
      tmp[pos] = keep;
    }

    board[y] = tmp;
  }

  private static void rotate(int cnt) {
    if (cnt == 0) {
      return;
    }

    for (int i = 0; i < cnt; ++i) {
      rotateClockwise();
    }
  }

  private static void swap(int y1, int x1, int y2, int x2) {
    int tmp = board[y1][x1];
    board[y1][x1] = board[y2][x2];
    board[y2][x2] = tmp;
  }

  private static void rotateClockwise() {
    for (int x = 0; x < N; ++x) {
      int st = 0;
      int en = N - 1;
      while (st < en) {
        swap(st, x, en, x);
        st++;
        en--;
      }
    }

    for (int y = 0; y < N; ++y) {
      for (int x = y + 1; x < N; ++x) {
        swap(y, x, x, y);
      }
    }
  }

  private static int getDir(String command) {
    switch (command) {
      case "R":
        return 0;
      case "U":
        return 1;
      case "L":
        return 2;
      case "D":
        return 3;
      default:
        break;
    }

    return -1;
  }


}

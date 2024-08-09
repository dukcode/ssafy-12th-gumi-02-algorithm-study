import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BoardCover {

  private static final int[][][] BLOCK = {
      {{0, 0}, {0, 1}, {1, 1}}, // ㄱ
      {{0, 0}, {1, 0}, {1, -1}}, // _|
      {{0, 0}, {1, 0}, {1, 1}}, // ㄴ
      {{0, 0}, {0, 1}, {1, 0}}, // |^
  };

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int h;
  private static int w;
  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      st = new StringTokenizer(br.readLine());
      h = Integer.parseInt(st.nextToken());
      w = Integer.parseInt(st.nextToken());

      board = new int[h][w];
      for (int y = 0; y < h; ++y) {
        char[] line = br.readLine().toCharArray();
        for (int x = 0; x < w; ++x) {
          board[y][x] = line[x] == '#' ? 1 : 0;
        }
      }

      bw.write(String.valueOf(countCovers()));
      bw.newLine();
    }

    br.close();
    bw.close();

  }

  private static int countCovers() {
    int firstY = -1;
    int firstX = -1;
    Loop:
    for (int y = 0; y < h; y++) {
      for (int x = 0; x < w; x++) {
        if (board[y][x] == 0) {
          firstY = y;
          firstX = x;
          break Loop;
        }
      }
    }

    if (firstY == -1) {
      return 1;
    }

    int ret = 0;
    for (int dir = 0; dir < 4; dir++) {
      if (draw(firstY, firstX, dir, 1)) {
        ret += countCovers();
      }

      draw(firstY, firstX, dir, -1);
    }

    return ret;
  }

  private static boolean draw(int startY, int startX, int dir, int delta) {
    boolean ret = true;

    for (int i = 0; i < 3; ++i) {
      int ny = startY + BLOCK[dir][i][0];
      int nx = startX + BLOCK[dir][i][1];

      if (ny < 0 || ny >= h || nx < 0 || nx >= w) {
        ret = false;
        continue;
      }

      board[ny][nx] += delta;

      if (board[ny][nx] != 1) {
        ret = false;
      }
    }

    return ret;
  }

}

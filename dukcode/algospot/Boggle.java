import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Boggle {

  private static final int BOARD_SIZE = 5;

  private static final int[] dy = {0, -1, -1, -1, 0, 1, 1, 1};
  private static final int[] dx = {1, 1, 0, -1, -1, -1, 0, 1};

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static char[][] board;
  private static int n;

  private static String word;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int c = Integer.parseInt(br.readLine());
    while (c-- > 0) {
      board = new char[5][];
      for (int i = 0; i < BOARD_SIZE; ++i) {
        char[] line = br.readLine().toCharArray();
        board[i] = line;
      }

      n = Integer.parseInt(br.readLine());
      for (int i = 0; i < n; ++i) {
        word = br.readLine();

        bw.write(word);
        bw.write(' ');
        bw.write(hasWord() ? "YES" : "NO");
        bw.newLine();
      }
    }

    br.close();
    bw.close();

  }

  private static boolean hasWord() {
    for (int y = 0; y < BOARD_SIZE; y++) {
      for (int x = 0; x < BOARD_SIZE; x++) {
        if (hasWord(y, x, 0)) {
          return true;
        }
      }
    }

    return false;
  }

  private static boolean hasWord(int y, int x, int idx) {
    if (idx == word.length()) {
      return true;
    }

    if (board[y][x] != word.charAt(idx)) {
      return false;
    }

    for (int dir = 0; dir < 8; ++dir) {
      int ny = y + dy[dir];
      int nx = x + dx[dir];

      if (ny < 0 || ny >= BOARD_SIZE || nx < 0 || nx >= BOARD_SIZE) {
        continue;
      }

      if (hasWord(ny, nx, idx + 1)) {
        return true;
      }
    }

    return false;
  }

}

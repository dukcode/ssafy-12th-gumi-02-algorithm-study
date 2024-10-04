import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class FallingHorizontalBlock {

  private static BufferedReader br;
  private static BufferedWriter bw;
  private static StringTokenizer st;

  private static int n;
  private static int m;
  private static int k;

  private static int[][] board;

  public static void main(String[] args) throws IOException {
    br = new BufferedReader(new InputStreamReader(System.in));
    bw = new BufferedWriter(new OutputStreamWriter(System.out));

    st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());
    k = Integer.parseInt(st.nextToken()) - 1;

    board = new int[n][n];
    for (int y = 0; y < n; ++y) {
      st = new StringTokenizer(br.readLine());
      for (int x = 0; x < n; ++x) {
        board[y][x] = Integer.parseInt(st.nextToken());
      }
    }

    dropBlock(k, m);

    for (int y = 0; y < n; ++y) {
      for (int x = 0; x < n; ++x) {
        bw.write(String.valueOf(board[y][x]));
        bw.write(' ');
      }
      bw.newLine();
    }

    br.close();
    bw.close();
  }

  private static void dropBlock(int pos, int size) {
    int minPos = n;
    for (int x = pos; x < pos + size; ++x) {
      minPos = Math.min(minPos, getPos(x));
    }

    for (int x = pos; x < pos + size; ++x) {
      board[minPos][x] = 1;
    }

  }

  private static int getPos(int x) {
    for (int y = 0; y < n; ++y) {
      if (board[y][x] != 0) {
        return y - 1;
      }
    }
    return n - 1;
  }


}
